"""
=========================================================
            CLAIM MANAGEMENT ROUTES
    Modernized Healthcare PBM Web Portal
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
from app.models.claim import Claim
from app.models.patient import Patient
from app.services.notification_service import NotificationService
from app.services.system_service import SystemService


claim_bp = Blueprint(
    "claim",
    __name__,
    url_prefix="/claims"
)

# =====================================================
# Configuration
# =====================================================

RECORDS_PER_PAGE = 10


# =====================================================
# Claim List
# =====================================================

@claim_bp.route("/")
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

    query = Claim.query

    if search:

        query = query.filter(

            or_(

                Claim.claim_id.ilike(f"%{search}%"),

                Claim.patient_id.ilike(f"%{search}%"),

                Claim.hospital_name.ilike(f"%{search}%"),

                Claim.doctor_name.ilike(f"%{search}%"),

                Claim.disease.ilike(f"%{search}%"),

                Claim.status.ilike(f"%{search}%")

            )

        )

    total_records = query.count()

    total_pages = max(

        1,

        ceil(total_records / RECORDS_PER_PAGE)

    )

    claims = (

        query

        .order_by(Claim.id.desc())

        .offset(

            (page - 1) * RECORDS_PER_PAGE

        )

        .limit(RECORDS_PER_PAGE)

        .all()

    )

    total_claims = Claim.query.count()

    pending_claims = Claim.query.filter_by(

        status="Pending"

    ).count()

    approved_claims = Claim.query.filter_by(

        status="Approved"

    ).count()

    rejected_claims = Claim.query.filter_by(

        status="Rejected"

    ).count()

    return render_template(

        "claim/index.html",

        page_title="Claims Management",

        claims=claims,

        page=page,

        total_pages=total_pages,

        total_records=total_records,

        search=search,

        total_claims=total_claims,

        pending_claims=pending_claims,

        approved_claims=approved_claims,

        rejected_claims=rejected_claims

    )

# =====================================================
# Add New Claim
# =====================================================

@claim_bp.route("/add", methods=["GET", "POST"])
def add():

    patients = (
        Patient.query
        .order_by(Patient.first_name.asc())
        .all()
    )

    if request.method == "POST":

        claim_id = request.form.get(
            "claim_id"
        ).strip()

        patient_id = request.form.get(
            "patient_id"
        ).strip()

        hospital_name = request.form.get(
            "hospital_name"
        ).strip()

        doctor_name = request.form.get(
            "doctor_name"
        ).strip()

        disease = request.form.get(
            "disease"
        ).strip()

        claim_amount = request.form.get(
            "claim_amount"
        ).strip()

        treatment_date = request.form.get(
            "treatment_date"
        ).strip()

        status = request.form.get(
            "status"
        ).strip()

        remarks = request.form.get(
            "remarks"
        ).strip()

        # ==========================================
        # Validation
        # ==========================================

        if not claim_id:

            flash(
                "Claim ID is required.",
                "danger"
            )

            return redirect(
                url_for("claim.add")
            )

        existing_claim = Claim.query.filter_by(
            claim_id=claim_id
        ).first()

        if existing_claim:

            flash(
                "Claim ID already exists.",
                "warning"
            )

            return redirect(
                url_for("claim.add")
            )

        patient = Patient.query.filter_by(
            patient_id=patient_id
        ).first()

        if not patient:

            flash(
                "Selected patient does not exist.",
                "danger"
            )

            return redirect(
                url_for("claim.add")
            )

        try:

            treatment_date = datetime.strptime(
                treatment_date,
                "%Y-%m-%d"
            ).date()

            claim_amount = float(
                claim_amount
            )

        except Exception:

            flash(
                "Invalid claim information.",
                "danger"
            )

            return redirect(
                url_for("claim.add")
            )

        # ==========================================
        # Save Claim
        # ==========================================

        claim = Claim(

            claim_id=claim_id,

            patient_id=patient_id,

            hospital_name=hospital_name,

            doctor_name=doctor_name,

            disease=disease,

            claim_amount=claim_amount,

            treatment_date=treatment_date,

            status=status,

            remarks=remarks

        )

        db.session.add(
            claim
        )

        db.session.commit()


        enabled = SystemService.get(

            "email_notifications",

            "Enabled"

        )

        if enabled == "Enabled":


            NotificationService.create_notification(

            title="New Claim Submitted",

            message=f"Claim {claim.claim_id} has been submitted.",

            category="Claim",

            priority="Medium",

            action_url=f"/claims",

            reference_id=claim.claim_id,

            icon="fa-file-medical",

            color="primary"

        )



        flash(
            "Claim added successfully.",
            "success"
        )

        return redirect(
            url_for("claim.index")
        )

    return render_template(

        "claim/add.html",

        page_title="Add Claim",

        patients=patients

    )

    # =====================================================
# Edit Claim
# =====================================================

@claim_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    claim = Claim.query.get_or_404(id)

    patients = (
        Patient.query
        .order_by(Patient.first_name.asc())
        .all()
    )

    if request.method == "POST":

        claim_id = request.form.get(
            "claim_id"
        ).strip()

        patient_id = request.form.get(
            "patient_id"
        ).strip()

        hospital_name = request.form.get(
            "hospital_name"
        ).strip()

        doctor_name = request.form.get(
            "doctor_name"
        ).strip()

        disease = request.form.get(
            "disease"
        ).strip()

        claim_amount = request.form.get(
            "claim_amount"
        ).strip()

        treatment_date = request.form.get(
            "treatment_date"
        ).strip()

        status = request.form.get(
            "status"
        ).strip()

        remarks = request.form.get(
            "remarks"
        ).strip()

        # ==========================================
        # Validation
        # ==========================================

        duplicate_claim = Claim.query.filter(

            Claim.claim_id == claim_id,

            Claim.id != id

        ).first()

        if duplicate_claim:

            flash(

                "Claim ID already exists.",

                "warning"

            )

            return redirect(

                url_for(

                    "claim.edit",

                    id=id

                )

            )

        patient = Patient.query.filter_by(

            patient_id=patient_id

        ).first()

        if not patient:

            flash(

                "Selected patient does not exist.",

                "danger"

            )

            return redirect(

                url_for(

                    "claim.edit",

                    id=id

                )

            )

        try:

            treatment_date = datetime.strptime(

                treatment_date,

                "%Y-%m-%d"

            ).date()

            claim_amount = float(

                claim_amount

            )

        except Exception:

            flash(

                "Invalid claim information.",

                "danger"

            )

            return redirect(

                url_for(

                    "claim.edit",

                    id=id

                )

            )

        # ==========================================
        # Update Claim
        # ==========================================

        claim.claim_id = claim_id

        claim.patient_id = patient_id

        claim.hospital_name = hospital_name

        claim.doctor_name = doctor_name

        claim.disease = disease

        claim.claim_amount = claim_amount

        claim.treatment_date = treatment_date

        claim.status = status

        claim.remarks = remarks

        claim.updated_at = datetime.utcnow()

        db.session.commit()

        flash(

            "Claim updated successfully.",

            "success"

        )

        return redirect(

            url_for(

                "claim.index"

            )

        )

    return render_template(

        "claim/edit.html",

        page_title="Edit Claim",

        claim=claim,

        patients=patients

    )

# =====================================================
# Claim Details
# =====================================================

@claim_bp.route("/details/<int:id>")
def details(id):

    claim = Claim.query.get_or_404(id)

    return render_template(

        "claim/details.html",

        page_title="Claim Details",

        claim=claim

    )


# =====================================================
# Delete Claim
# =====================================================

@claim_bp.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):

    claim = Claim.query.get_or_404(id)

    if request.method == "POST":

        try:

            db.session.delete(claim)

            db.session.commit()

            flash(

                "Claim deleted successfully.",

                "success"

            )

        except Exception:

            db.session.rollback()

            flash(

                "Unable to delete claim.",

                "danger"

            )

        return redirect(

            url_for(

                "claim.index"

            )

        )

    return render_template(

        "claim/delete.html",

        page_title="Delete Claim",

        claim=claim

    )


# =====================================================
# Change Claim Status
# =====================================================

@claim_bp.route("/status/<int:id>/<status>")
def change_status(id, status):

    claim = Claim.query.get_or_404(id)

    valid_status = [

        "Pending",

        "Approved",

        "Rejected"

    ]

    if status not in valid_status:

        flash(

            "Invalid claim status.",

            "danger"

        )

        return redirect(

            url_for(

                "claim.index"

            )

        )

    claim.status = status

    claim.updated_at = datetime.utcnow()

    db.session.commit()

    flash(

        f"Claim status changed to {status}.",

        "success"

    )

    return redirect(

        url_for(

            "claim.index"

        )

    )


# =====================================================
# Claim Statistics
# =====================================================

@claim_bp.route("/statistics")
def statistics():

    data = {

        "total_claims":

            Claim.query.count(),

        "pending_claims":

            Claim.query.filter_by(

                status="Pending"

            ).count(),

        "approved_claims":

            Claim.query.filter_by(

                status="Approved"

            ).count(),

        "rejected_claims":

            Claim.query.filter_by(

                status="Rejected"

            ).count(),

        "total_amount":

            db.session.query(

                db.func.sum(

                    Claim.claim_amount

                )

            ).scalar() or 0

    }

    return data


# =====================================================
# End of File
# =====================================================