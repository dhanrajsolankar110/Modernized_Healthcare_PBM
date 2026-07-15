
"""
=========================================================
            AI SERVICE
    Modernized Healthcare PBM Web Portal
=========================================================
"""

from app.models.claim import Claim


class AIService:
    """Service for AI-related business logic."""

    @staticmethod
    def calculate_risk_score(claim):
        score = 0

        if claim.claim_amount > claim.treatment_cost * 2:
            score += 40

        if claim.duplicate_claim:
            score += 30

        if claim.fraud_probability >= 0.80:
            score += 30

        return min(score, 100)

    @staticmethod
    def evaluate_claim(claim):
        claim.risk_score = AIService.calculate_risk_score(claim)

        if claim.risk_score >= 80:
            claim.fraud_flag = True
            claim.ai_prediction = "High Risk"
        elif claim.risk_score >= 50:
            claim.ai_prediction = "Medium Risk"
        else:
            claim.ai_prediction = "Low Risk"

        return claim

    @staticmethod
    def get_dashboard_summary():
        claims = Claim.query.all()

        return {
            "total_claims": len(claims),
            "approved": len([c for c in claims if c.claim_status == "Approved"]),
            "pending": len([c for c in claims if c.claim_status == "Pending"]),
            "rejected": len([c for c in claims if c.claim_status == "Rejected"]),
            "high_risk": len([c for c in claims if c.risk_score >= 80]),
            "fraud_detected": len([c for c in claims if c.fraud_flag])
        }
