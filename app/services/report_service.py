
"""
=========================================================
            REPORT SERVICE
    Modernized Healthcare PBM Web Portal
=========================================================
"""

from datetime import datetime

from app.extensions import db
from app.models.report import Report
from app.models.claim import Claim


class ReportService:
    """Service class for report management."""

    @staticmethod
    def create_report(data):
        report = Report(
            report_id=data.get("report_id"),
            patient_id=data.get("patient_id"),
            report_title=data.get("report_title"),
            report_type=data.get("report_type"),
            generated_by=data.get("generated_by"),
            department=data.get("department"),
            hospital_id=data.get("hospital_id"),
            hospital_name=data.get("hospital_name"),
            report_status=data.get("report_status", "Generated"),
            ai_summary=data.get("ai_summary"),
            findings=data.get("findings"),
            recommendations=data.get("recommendations"),
            risk_score=float(data.get("risk_score", 0)),
            fraud_probability=float(data.get("fraud_probability", 0)),
            file_name=data.get("file_name"),
            file_path=data.get("file_path"),
            remarks=data.get("remarks")
        )

        db.session.add(report)
        db.session.commit()

        return report

    @staticmethod
    def update_report(report, data):
        report.report_title = data.get("report_title", report.report_title)
        report.report_type = data.get("report_type", report.report_type)
        report.report_status = data.get("report_status", report.report_status)
        report.ai_summary = data.get("ai_summary", report.ai_summary)
        report.findings = data.get("findings", report.findings)
        report.recommendations = data.get("recommendations", report.recommendations)
        report.risk_score = float(data.get("risk_score", report.risk_score))
        report.fraud_probability = float(
            data.get("fraud_probability", report.fraud_probability)
        )
        report.file_name = data.get("file_name", report.file_name)
        report.file_path = data.get("file_path", report.file_path)
        report.remarks = data.get("remarks", report.remarks)
        report.updated_at = datetime.utcnow()

        db.session.commit()

        return report

    @staticmethod
    def delete_report(report):
        db.session.delete(report)
        db.session.commit()

    @staticmethod
    def get_high_risk_reports():
        return Report.query.filter(
            Report.risk_score >= 80
        ).all()

    @staticmethod
    def generate_ai_summary():
        claims = Claim.query.all()

        total = len(claims)
        fraud = len([c for c in claims if c.fraud_flag])

        return {
            "generated_on": datetime.utcnow().isoformat(),
            "total_claims": total,
            "fraud_detected": fraud,
            "fraud_percentage": round((fraud / total) * 100, 2) if total else 0
        }
