"""
=========================================================
            PHARMACY MANAGEMENT ROUTES
=========================================================
"""

from math import ceil
from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from sqlalchemy import or_

from app.extensions import db
from app.models.pharmacy import Pharmacy
from app.services.notification_service import NotificationService
from app.services.system_service import SystemService

# =====================================================
# Blueprint
# =====================================================

pharmacy_bp = Blueprint(
    "pharmacy",
    __name__,
    url_prefix="/pharmacy"
)

# =====================================================
# Configuration
# =====================================================

RECORDS_PER_PAGE = 10

@pharmacy_bp.route("/")
def index():

    page = request.args.get(
        "page",
        1,
        type=int
    )

    search = request.args.get(
        "search",
        "",
        type=str
    ).strip()

    query = Pharmacy.query

    if search:

        query = query.filter(

            or_(

                Pharmacy.medicine_id.ilike(f"%{search}%"),

                Pharmacy.medicine_name.ilike(f"%{search}%"),

                Pharmacy.category.ilike(f"%{search}%"),

                Pharmacy.manufacturer.ilike(f"%{search}%")

            )

        )

    pharmacy = query.order_by(
        Pharmacy.id.desc()
    ).paginate(

        page=page,

        per_page=RECORDS_PER_PAGE,

        error_out=False

    )

    total_medicines = Pharmacy.query.count()

    available = Pharmacy.query.filter_by(
        status="Available"
    ).count()

    low_stock = Pharmacy.query.filter(
        Pharmacy.stock_quantity < 20
    ).count()

    out_of_stock = Pharmacy.query.filter(
        Pharmacy.stock_quantity == 0
    ).count()

    return render_template(

        "pharmacy/index.html",

        pharmacy=pharmacy,

        medicines=pharmacy.items,

        search=search,

        total_medicines=total_medicines,

        available=available,

        low_stock=low_stock,

        out_of_stock=out_of_stock

    )

@pharmacy_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        medicine = Pharmacy(

            medicine_id=request.form.get("medicine_id").strip(),

            medicine_name=request.form.get("medicine_name").strip(),

            category=request.form.get("category").strip(),

            manufacturer=request.form.get("manufacturer").strip(),

            batch_number=request.form.get("batch_number").strip(),

            expiry_date=datetime.strptime(
                request.form.get("expiry_date"),
                "%Y-%m-%d"
            ).date(),

            stock_quantity=int(
                request.form.get("stock_quantity")
            ),

            unit_price=float(
                request.form.get("unit_price")
            ),

            supplier_name=request.form.get(
                "supplier_name"
            ).strip(),

            status=request.form.get("status").strip()

        )

        db.session.add(medicine)

        db.session.commit()

        if medicine.stock_quantity <= 10:


            enabled = SystemService.get(

            "email_notifications",

            "Enabled"

            )

        if enabled == "Enabled":


            NotificationService.create_notification(

                title="Low Medicine Stock",

                message=f"{medicine.medicine_name} stock is low.",

                category="Pharmacy",

                priority="High",

                action_url="/pharmacy",

                reference_id=medicine.medicine_id,

                icon="fa-capsules",

                color="warning"

            )

        flash(
            "Medicine added successfully!",
            "success"
        )

        return redirect(
            url_for("pharmacy.index")
        )

    last = Pharmacy.query.order_by(
        Pharmacy.id.desc()
    ).first()

    if last:

        number = int(
            last.medicine_id.replace("M", "")
        ) + 1

    else:

        number = 1

    medicine_id = f"M{number:04d}"

    return render_template(

        "pharmacy/add.html",

        page_title="Add Medicine",

        medicine_id=medicine_id

    )

@pharmacy_bp.route("/details/<int:id>")
def details(id):

    medicine = Pharmacy.query.get_or_404(id)

    return render_template(

        "pharmacy/details.html",

        page_title="Medicine Details",

        medicine=medicine

    )

@pharmacy_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    medicine = Pharmacy.query.get_or_404(id)

    if request.method == "POST":

        medicine.medicine_name = request.form.get(
            "medicine_name"
        ).strip()

        medicine.category = request.form.get(
            "category"
        ).strip()

        medicine.manufacturer = request.form.get(
            "manufacturer"
        ).strip()

        medicine.batch_number = request.form.get(
            "batch_number"
        ).strip()

        medicine.expiry_date = datetime.strptime(
            request.form.get("expiry_date"),
            "%Y-%m-%d"
        ).date()

        medicine.stock_quantity = int(
            request.form.get("stock_quantity")
        )

        medicine.unit_price = float(
            request.form.get("unit_price")
        )

        medicine.supplier_name = request.form.get(
            "supplier_name"
        ).strip()

        medicine.status = request.form.get(
            "status"
        ).strip()

        db.session.commit()

        flash(
            "Medicine updated successfully!",
            "success"
        )

        return redirect(
            url_for("pharmacy.index")
        )

    return render_template(

        "pharmacy/edit.html",

        page_title="Edit Medicine",

        medicine=medicine

    )

@pharmacy_bp.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):

    medicine = Pharmacy.query.get_or_404(id)

    if request.method == "POST":

        db.session.delete(medicine)

        db.session.commit()

        flash(
            "Medicine deleted successfully!",
            "success"
        )

        return redirect(
            url_for("pharmacy.index")
        )

    return render_template(

        "pharmacy/delete.html",

        page_title="Delete Medicine",

        medicine=medicine

    )