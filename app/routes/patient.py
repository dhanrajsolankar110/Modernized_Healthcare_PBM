"""
=========================================================
        Patient Management Routes
    Modernized Healthcare PBM Web Portal
=========================================================
"""

from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import login_required

from sqlalchemy import or_

from app.extensions import db
from app.models.patient import Patient

# =========================================================
# Blueprint
# =========================================================

patient_bp = Blueprint(
    "patient",
    __name__,
    url_prefix="/patient"
)

# =========================================================
# Helper Functions
# =========================================================

def generate_patient_id():
    """
    Generate next Patient ID
    Example:
    P0001
    P0002
    """

    last_patient = (
        Patient.query
        .order_by(Patient.id.desc())
        .first()
    )

    if last_patient:

        try:
            last_id = int(
                last_patient.patient_id.replace("P", "")
            )

            return f"P{last_id + 1:04d}"

        except Exception:
            return "P0001"

    return "P0001"


# =========================================================
# Patient List
# =========================================================

@patient_bp.route("/")
@login_required
def index():

    search = request.args.get(
        "search",
        ""
    ).strip()

    page = request.args.get(
        "page",
        1,
        type=int
    )

    query = Patient.query

    if search:

        query = query.filter(

            or_(

                Patient.patient_id.ilike(
                    f"%{search}%"
                ),

                Patient.first_name.ilike(
                    f"%{search}%"
                ),

                Patient.last_name.ilike(
                    f"%{search}%"
                ),

                Patient.email.ilike(
                    f"%{search}%"
                ),

                Patient.phone.ilike(
                    f"%{search}%"
                ),

                Patient.disease.ilike(
                    f"%{search}%"
                )

            )

        )

    patients = (

        query.order_by(

            Patient.created_at.desc()

        ).paginate(

            page=page,

            per_page=10,

            error_out=False

        )

    )

    statistics = {

        "total": Patient.query.count(),

        "active": Patient.query.filter_by(
            status="Active"
        ).count(),

        "inactive": Patient.query.filter_by(
            status="Inactive"
        ).count()

    }

    return render_template(

        "patient/index.html",

        page_title="Patient Management",

        patients=patients,

        statistics=statistics,

        search=search

    )


# =========================================================
# Add Patient
# =========================================================

@patient_bp.route(
    "/add",
    methods=["GET", "POST"]
)
@login_required
def add():

    if request.method == "POST":

        dob = request.form.get(
            "date_of_birth"
        )

        patient = Patient(

            patient_id=generate_patient_id(),

            first_name=request.form.get(
                "first_name"
            ),

            last_name=request.form.get(
                "last_name"
            ),

            gender=request.form.get(
                "gender"
            ),

            age=int(
                request.form.get(
                    "age"
                )
            ),

            date_of_birth=(
                datetime.strptime(
                    dob,
                    "%Y-%m-%d"
                ).date()
                if dob else None
            ),

            blood_group=request.form.get(
                "blood_group"
            ),

            phone=request.form.get(
                "phone"
            ),

            email=request.form.get(
                "email"
            ),

            address=request.form.get(
                "address"
            ),

            city=request.form.get(
                "city"
            ),

            state=request.form.get(
                "state"
            ),

            pincode=request.form.get(
                "pincode"
            ),

            disease=request.form.get(
                "disease"
            ),

            insurance_provider=request.form.get(
                "insurance_provider"
            ),

            insurance_number=request.form.get(
                "insurance_number"
            ),

            emergency_contact=request.form.get(
                "emergency_contact"
            ),

            emergency_contact_name=request.form.get(
                "emergency_contact_name"
            ),

            status=request.form.get(
                "status"
            ) or "Active"

        )

        db.session.add(patient)
        db.session.commit()

        flash(
            "Patient added successfully.",
            "success"
        )

        return redirect(
            url_for("patient.index")
        )

    return render_template(

        "patient/add.html",

        page_title="Add Patient",

        patient_id=generate_patient_id()

    )


# =========================================================
# Patient Details
# =========================================================

@patient_bp.route("/<int:id>")
@login_required
def details(id):

    patient = Patient.query.get_or_404(id)

    return render_template(
        "patient/details.html",
        page_title="Patient Details",
        patient=patient
    )


# =========================================================
# Edit Patient
# =========================================================

@patient_bp.route(
    "/edit/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def edit(id):

    patient = Patient.query.get_or_404(id)

    if request.method == "POST":

        dob = request.form.get("date_of_birth")

        patient.first_name = request.form.get("first_name")
        patient.last_name = request.form.get("last_name")
        patient.gender = request.form.get("gender")
        patient.age = int(request.form.get("age"))

        patient.date_of_birth = (
            datetime.strptime(
                dob,
                "%Y-%m-%d"
            ).date()
            if dob else None
        )

        patient.blood_group = request.form.get("blood_group")
        patient.phone = request.form.get("phone")
        patient.email = request.form.get("email")
        patient.address = request.form.get("address")
        patient.city = request.form.get("city")
        patient.state = request.form.get("state")
        patient.pincode = request.form.get("pincode")
        patient.disease = request.form.get("disease")
        patient.insurance_provider = request.form.get(
            "insurance_provider"
        )
        patient.insurance_number = request.form.get(
            "insurance_number"
        )
        patient.emergency_contact = request.form.get(
            "emergency_contact"
        )
        patient.emergency_contact_name = request.form.get(
            "emergency_contact_name"
        )
        patient.status = request.form.get("status")

        db.session.commit()

        flash(
            "Patient updated successfully.",
            "success"
        )

        return redirect(
            url_for(
                "patient.details",
                id=patient.id
            )
        )

    return render_template(
        "patient/edit.html",
        page_title="Edit Patient",
        patient=patient
    )


# =========================================================
# Delete Patient
# =========================================================

@patient_bp.route(
    "/delete/<int:id>",
    methods=["GET", "POST"]
)
@login_required
def delete(id):

    patient = Patient.query.get_or_404(id)

    if request.method == "POST":

        db.session.delete(patient)
        db.session.commit()

        flash(
            "Patient deleted successfully.",
            "success"
        )

        return redirect(
            url_for("patient.index")
        )

    return render_template(
        "patient/delete.html",
        page_title="Delete Patient",
        patient=patient
    )


# =========================================================
# Search Patients
# =========================================================

@patient_bp.route("/search")
@login_required
def search():

    keyword = request.args.get(
        "keyword",
        ""
    ).strip()

    query = Patient.query

    if keyword:

        query = query.filter(

            or_(

                Patient.patient_id.ilike(
                    f"%{keyword}%"
                ),

                Patient.first_name.ilike(
                    f"%{keyword}%"
                ),

                Patient.last_name.ilike(
                    f"%{keyword}%"
                ),

                Patient.email.ilike(
                    f"%{keyword}%"
                ),

                Patient.phone.ilike(
                    f"%{keyword}%"
                ),

                Patient.disease.ilike(
                    f"%{keyword}%"
                )

            )

        )

    patients = query.order_by(
        Patient.created_at.desc()
    ).all()

    statistics = {

        "total": Patient.query.count(),

        "active": Patient.query.filter_by(
            status="Active"
        ).count(),

        "inactive": Patient.query.filter_by(
            status="Inactive"
        ).count()

    }

    return render_template(

        "patient/index.html",

        page_title="Patient Search",

        patients=patients,

        statistics=statistics,

        search=keyword

    )


# =========================================================
# Toggle Patient Status
# =========================================================

@patient_bp.route("/status/<int:id>")
@login_required
def toggle_status(id):

    patient = Patient.query.get_or_404(id)

    if patient.status == "Active":

        patient.status = "Inactive"

        flash(
            "Patient deactivated successfully.",
            "warning"
        )

    else:

        patient.status = "Active"

        flash(
            "Patient activated successfully.",
            "success"
        )

    db.session.commit()

    return redirect(
        url_for("patient.index")
    )