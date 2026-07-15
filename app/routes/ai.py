
"""
=========================================================
                AI ROUTES
    Modernized Healthcare PBM Web Portal
=========================================================
"""

from flask import Blueprint, jsonify, render_template, flash, redirect, url_for
from flask_login import login_required

from app.models.claim import Claim
from app.models.report import Report

ai_bp = Blueprint(
    "ai",
    __name__,
    url_prefix="/ai"
)


@ai_bp.route("/")
@login_required
def index():
    high_risk_claims = Claim.query.filter(
        Claim.risk_score >= 80
    ).all()

    reports = Report.query.order_by(
        Report.created_at.desc()
    ).limit(10).all()

    return render_template(
        "ai/index.html",
        high_risk_claims=high_risk_claims,
        reports=reports
    )


@ai_bp.route("/fraud-insights")
@login_required
def fraud_insights():
    claims = Claim.query.all()

    total = len(claims)
    high_risk = len([c for c in claims if c.risk_score >= 80])
    fraud = len([c for c in claims if c.fraud_flag])

    return jsonify({
        "total_claims": total,
        "high_risk_claims": high_risk,
        "fraud_detected": fraud,
        "safe_claims": total - fraud
    })


@ai_bp.route("/high-risk")
@login_required
def high_risk():
    claims = Claim.query.filter(
        Claim.risk_score >= 80
    ).order_by(
        Claim.risk_score.desc()
    ).all()

    return render_template(
        "ai/high_risk.html",
        claims=claims
    )


@ai_bp.route("/duplicate-claims")
@login_required
def duplicate_claims():
    claims = Claim.query.filter_by(
        duplicate_claim=True
    ).all()

    return render_template(
        "ai/duplicate_claims.html",
        claims=claims
    )


@ai_bp.route("/approve/<claim_id>")
@login_required
def approve_ai(claim_id):
    claim = Claim.query.filter_by(
        claim_id=claim_id
    ).first_or_404()

    claim.approve(claim.claim_amount)

    from app.extensions import db
    db.session.commit()

    flash("AI recommendation approved successfully.", "success")

    return redirect(url_for("claims.view", claim_id=claim.claim_id))


@ai_bp.route("/dashboard-data")
@login_required
def dashboard_data():

    claims = Claim.query.all()

    return jsonify({
        "total": len(claims),
        "pending": len([c for c in claims if c.claim_status == "Pending"]),
        "approved": len([c for c in claims if c.claim_status == "Approved"]),
        "rejected": len([c for c in claims if c.claim_status == "Rejected"]),
        "high_risk": len([c for c in claims if c.risk_score >= 80]),
        "duplicates": len([c for c in claims if c.duplicate_claim]),
    })
