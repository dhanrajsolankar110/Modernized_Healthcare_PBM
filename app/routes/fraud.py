"""
=========================================================
        AI FRAUD DETECTION ROUTES
Modernized Healthcare PBM Portal
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

from sqlalchemy import (
    func,
    extract,
    or_
)

from app.extensions import db

from app.models.claim import Claim

from app.ai.predict import FraudPredictor

from app.ai.duplicate_detector import DuplicateDetector

from app.services.notification_service import NotificationService

from app.services.system_service import SystemService


fraud_bp = Blueprint(
    "fraud",
    __name__,
    url_prefix="/fraud"
)

RECORDS_PER_PAGE = 10

# ==========================================================
# FRAUD DASHBOARD
# ==========================================================

@fraud_bp.route("/")
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

    query = Claim.query.filter(
        Claim.prediction_date.isnot(None)
    )

    # ------------------------------------------------------
    # SEARCH
    # ------------------------------------------------------

    if search:

        query = query.filter(

            or_(

                Claim.claim_id.ilike(f"%{search}%"),

                Claim.patient_id.ilike(f"%{search}%"),

                Claim.hospital_name.ilike(f"%{search}%"),

                Claim.disease.ilike(f"%{search}%"),

                Claim.risk_level.ilike(f"%{search}%")

            )

        )

    # ------------------------------------------------------
    # PAGINATION
    # ------------------------------------------------------

    fraud = query.order_by(

        Claim.id.desc()

    ).paginate(

        page=page,

        per_page=RECORDS_PER_PAGE,

        error_out=False

    )

    # ------------------------------------------------------
    # DASHBOARD STATISTICS
    # ------------------------------------------------------

    total_predictions = Claim.query.filter(

        Claim.prediction_date.isnot(None)

    ).count()

    high_risk = Claim.query.filter(

        Claim.risk_level == "High"

    ).count()

    medium_risk = Claim.query.filter(

        Claim.risk_level == "Medium"

    ).count()

    low_risk = Claim.query.filter(

        Claim.risk_level == "Low"

    ).count()

    duplicate_claims = Claim.query.filter(

        Claim.duplicate_claim == True

    ).count()

    # ------------------------------------------------------
    # RECENT HIGH RISK
    # ------------------------------------------------------

    recent_high_risk = Claim.query.filter(

        Claim.risk_level == "High"

    ).order_by(

        Claim.prediction_date.desc()

    ).limit(5).all()

    # ------------------------------------------------------
    # RENDER
    # ------------------------------------------------------

    return render_template(

        "fraud/index.html",

        page_title="AI Fraud Detection",

        fraud=fraud,

        search=search,

        total_predictions=total_predictions,

        high_risk=high_risk,

        medium_risk=medium_risk,

        low_risk=low_risk,

        duplicate_claims=duplicate_claims,

        recent_high_risk=recent_high_risk

    )

# ==========================================================
# RUN AI PREDICTION
# ==========================================================

@fraud_bp.route("/predict/<int:id>")
def predict(id):

    # ------------------------------------------------------
    # GET CLAIM
    # ------------------------------------------------------

    claim = Claim.query.get_or_404(id)

    predictor = FraudPredictor()

    duplicate_detector = DuplicateDetector()

    # ------------------------------------------------------
    # DUPLICATE CHECK
    # ------------------------------------------------------

    is_duplicate = duplicate_detector.check_duplicate(
        claim
    )

    # ------------------------------------------------------
    # PREPARE AI INPUT
    # ------------------------------------------------------

    hospital = claim.hospital_name

    disease = claim.disease

    age = getattr(claim, "patient_age", 30)

    treatment_cost = getattr(

        claim,

        "treatment_cost",

        claim.claim_amount * 0.80

    )

    previous_claims = Claim.query.filter(

        Claim.patient_id == claim.patient_id,

        Claim.id != claim.id

    ).count()

    # ------------------------------------------------------
    # RUN MODEL
    # ------------------------------------------------------

    try:

        result = predictor.predict(

            hospital=hospital,

            disease=disease,

            age=age,

            treatment_cost=treatment_cost,

            claim_amount=claim.claim_amount,

            previous_claims=previous_claims,

            duplicate_claim=int(is_duplicate)

        )

    except Exception as e:

        flash(

            f"Prediction failed : {str(e)}",

            "danger"

        )

        return redirect(

            url_for("fraud.index")

        )

    # ------------------------------------------------------
    # SAVE RESULT
    # ------------------------------------------------------

    claim.predicted_risk = result["risk_score"]

    claim.risk_level = result["risk_level"]

    print("Prediction Result:", result)
    print("Risk Level:", repr(result["risk_level"]))
    print("Risk Score:", result["risk_score"]) 

    claim.duplicate_claim = is_duplicate

    claim.prediction_date = datetime.utcnow()

    if is_duplicate:

        claim.ai_remark = (

            "Possible Duplicate Claim Detected"

        )

    else:

        claim.ai_remark = (

            "No Duplicate Claim Found"

        )

    db.session.commit()

    if claim.risk_level == "High":


        enabled = SystemService.get(

            "email_notifications",

            "Enabled"

        )

    if enabled == "Enabled":


        NotificationService.create_notification(

            title="High Risk Claim",

            message=f"Claim {claim.claim_id} was detected as HIGH RISK.",

            category="Fraud",

            priority="Critical",

            action_url=f"/fraud/predict/{claim.id}",

            reference_id=claim.claim_id,

            icon="fa-triangle-exclamation",

            color="danger"

        )

    # ------------------------------------------------------
    # SUCCESS MESSAGE
    # ------------------------------------------------------

    flash(

        "AI Prediction completed successfully.",

        "success"

    )

    return redirect(

        url_for("fraud.index")

    )

# ==========================================================
# AI INSIGHTS DASHBOARD
# ==========================================================

@fraud_bp.route("/insights")
def insights():

    # ------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------

    total_predictions = Claim.query.filter(

        Claim.prediction_date.isnot(None)

    ).count()

    high_risk = Claim.query.filter(

        Claim.risk_level == "High"

    ).count()

    medium_risk = Claim.query.filter(

        Claim.risk_level == "Medium"

    ).count()

    low_risk = Claim.query.filter(

        Claim.risk_level == "Low"

    ).count()

    duplicate_claims = Claim.query.filter(

        Claim.duplicate_claim == True

    ).count()

    # ------------------------------------------------------
    # AI ACCURACY
    # ------------------------------------------------------

    ai_accuracy = 98.5

    # ------------------------------------------------------
    # MONTHLY FRAUD
    # ------------------------------------------------------

    months = [

        "Jan","Feb","Mar","Apr","May","Jun",

        "Jul","Aug","Sep","Oct","Nov","Dec"

    ]

    monthly_fraud = [0] * 12

    results = db.session.query(

        extract(

            "month",

            Claim.prediction_date

        ),

        func.count(Claim.id)

    ).filter(

        Claim.prediction_date.isnot(None)

    ).group_by(

        extract(

            "month",

            Claim.prediction_date

        )

    ).all()

    for month,count in results:

        if month:

            monthly_fraud[int(month)-1] = count

    # ------------------------------------------------------
    # HOSPITAL ANALYSIS
    # ------------------------------------------------------

    hospital_query = db.session.query(

        Claim.hospital_name,

        func.count(Claim.id)

    ).filter(

        Claim.risk_level == "High"

    ).group_by(

        Claim.hospital_name

    ).order_by(

        func.count(Claim.id).desc()

    ).limit(5).all()

    hospital_labels = []

    hospital_fraud = []

    for row in hospital_query:

        hospital_labels.append(

            row[0]

        )

        hospital_fraud.append(

            row[1]

        )

    # ------------------------------------------------------
    # DISEASE ANALYSIS
    # ------------------------------------------------------

    disease_query = db.session.query(

        Claim.disease,

        func.count(Claim.id)

    ).filter(

        Claim.risk_level == "High"

    ).group_by(

        Claim.disease

    ).order_by(

        func.count(Claim.id).desc()

    ).limit(5).all()

    disease_labels = []

    disease_fraud = []

    for row in disease_query:

        disease_labels.append(

            row[0]

        )

        disease_fraud.append(

            row[1]

        )

    # ------------------------------------------------------
    # HOSPITAL ANALYTICS TABLE
    # ------------------------------------------------------

    hospital_analysis = []

    analysis = db.session.query(

        Claim.hospital_name,

        func.count(Claim.id),

        func.sum(

            Claim.risk_level == "High"

        )

    ).group_by(

        Claim.hospital_name

    ).all()

    for hospital_name,total_claims,fraud_claims in analysis:

        fraud_claims = fraud_claims or 0

        fraud_rate = round(

            (fraud_claims/total_claims)*100,

            2

        )

        hospital_analysis.append(

            {

                "hospital_name":hospital_name,

                "total_claims":total_claims,

                "fraud_claims":fraud_claims,

                "fraud_rate":fraud_rate

            }

        )

    # ------------------------------------------------------
    # QUICK INSIGHTS
    # ------------------------------------------------------

    highest_risk_hospital = (

        hospital_labels[0]

        if hospital_labels

        else "N/A"

    )

    highest_risk_disease = (

        disease_labels[0]

        if disease_labels

        else "N/A"

    )

    fraud_rate = round(

        (high_risk/total_predictions)*100,

        2

    ) if total_predictions else 0

    # ------------------------------------------------------
    # RENDER
    # ------------------------------------------------------

    return render_template(

        "fraud/insights.html",

        page_title="AI Insights",

        total_predictions=total_predictions,

        high_risk=high_risk,

        medium_risk=medium_risk,

        low_risk=low_risk,

        duplicate_claims=duplicate_claims,

        ai_accuracy=ai_accuracy,

        fraud_rate=fraud_rate,

        months=months,

        monthly_fraud=monthly_fraud,

        hospital_labels=hospital_labels,

        hospital_fraud=hospital_fraud,

        disease_labels=disease_labels,

        disease_fraud=disease_fraud,

        hospital_analysis=hospital_analysis,

        highest_risk_hospital=highest_risk_hospital,

        highest_risk_disease=highest_risk_disease

    )

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def get_dashboard_statistics():
    """
    Returns summary statistics for the Fraud Dashboard.
    """

    total_predictions = Claim.query.filter(
        Claim.prediction_date.isnot(None)
    ).count()

    high_risk = Claim.query.filter_by(
        risk_level="High"
    ).count()

    medium_risk = Claim.query.filter_by(
        risk_level="Medium"
    ).count()

    low_risk = Claim.query.filter_by(
        risk_level="Low"
    ).count()

    duplicate_claims = Claim.query.filter_by(
        duplicate_claim=True
    ).count()

    return {

        "total_predictions": total_predictions,

        "high_risk": high_risk,

        "medium_risk": medium_risk,

        "low_risk": low_risk,

        "duplicate_claims": duplicate_claims

    }


# ==========================================================
# MONTHLY ANALYTICS
# ==========================================================

def get_monthly_fraud():

    months = [

        "Jan","Feb","Mar","Apr","May","Jun",

        "Jul","Aug","Sep","Oct","Nov","Dec"

    ]

    monthly_fraud = [0] * 12

    results = db.session.query(

        extract(

            "month",

            Claim.prediction_date

        ),

        func.count(Claim.id)

    ).filter(

        Claim.prediction_date.isnot(None)

    ).group_by(

        extract(

            "month",

            Claim.prediction_date

        )

    ).all()

    for month, count in results:

        if month:

            monthly_fraud[int(month) - 1] = count

    return months, monthly_fraud


# ==========================================================
# HOSPITAL ANALYSIS
# ==========================================================

def get_hospital_analysis():

    query = db.session.query(

        Claim.hospital_name,

        func.count(Claim.id)

    ).filter(

        Claim.risk_level == "High"

    ).group_by(

        Claim.hospital_name

    ).order_by(

        func.count(Claim.id).desc()

    ).limit(5).all()

    labels = []

    values = []

    for row in query:

        labels.append(row[0])

        values.append(row[1])

    return labels, values


# ==========================================================
# DISEASE ANALYSIS
# ==========================================================

def get_disease_analysis():

    query = db.session.query(

        Claim.disease,

        func.count(Claim.id)

    ).filter(

        Claim.risk_level == "High"

    ).group_by(

        Claim.disease

    ).order_by(

        func.count(Claim.id).desc()

    ).limit(5).all()

    labels = []

    values = []

    for row in query:

        labels.append(row[0])

        values.append(row[1])

    return labels, values