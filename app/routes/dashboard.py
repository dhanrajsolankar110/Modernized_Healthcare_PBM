"""
=========================================================
    Dashboard Blueprint

    Modernized Healthcare PBM Portal
=========================================================
"""

from flask import Blueprint, render_template
from flask_login import login_required

# =========================================================
# Models
# =========================================================

from app.models.user import User

# Import these models when they are created
#
# from app.models.patient import Patient
# from app.models.claim import Claim
# from app.models.fraud import FraudClaim

# =========================================================
# Blueprint
# =========================================================

dashboard_bp = Blueprint(

    "dashboard",

    __name__,

    url_prefix="/dashboard"

)

# =========================================================
# Dashboard
# =========================================================

@dashboard_bp.route("/")

@login_required

def index():

    """
    Dashboard Home
    """

    # -----------------------------------------------------
    # Temporary Statistics
    # (Replace with database queries later)
    # -----------------------------------------------------

    statistics = {

        "total_patients": 1284,

        "total_claims": 824,

        "approved_claims": 693,

        "fraud_claims": 27,

        "monthly_revenue": "₹4.2 Cr",

        "ai_accuracy": "92%"

    }

    # -----------------------------------------------------
    # Recent Claims
    # -----------------------------------------------------

    recent_claims = [

        {

            "claim_id": "C1021",

            "patient": "Rahul Sharma",

            "hospital": "City Hospital",

            "amount": "₹45,200",

            "status": "Approved",

            "risk": "Low"

        },

        {

            "claim_id": "C1022",

            "patient": "Priya Patil",

            "hospital": "Apollo Hospital",

            "amount": "₹82,100",

            "status": "Pending",

            "risk": "Medium"

        },

        {

            "claim_id": "C1023",

            "patient": "Amit Singh",

            "hospital": "Ruby Hall",

            "amount": "₹2,45,000",

            "status": "Review",

            "risk": "High"

        },

        {

            "claim_id": "C1024",

            "patient": "Neha Verma",

            "hospital": "Sunrise Hospital",

            "amount": "₹58,900",

            "status": "Approved",

            "risk": "Low"

        }

    ]

    # -----------------------------------------------------
    # AI Summary
    # -----------------------------------------------------

    ai_summary = {

        "accuracy": 92,

        "high_risk": 3,

        "duplicate_claims": 18,

        "fraud_prevented": "₹78 Lakh"

    }

    # -----------------------------------------------------
    # Render Dashboard
    # -----------------------------------------------------

    return render_template(

        "dashboard/index.html",

        page_title="Dashboard",

        statistics=statistics,

        recent_claims=recent_claims,

        ai_summary=ai_summary

    )