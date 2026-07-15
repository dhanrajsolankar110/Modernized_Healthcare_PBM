
"""
=========================================================
            REPORT DATABASE MODEL
    Modernized Healthcare PBM Web Portal
=========================================================
"""

from datetime import datetime
from app.extensions import db


class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)

    report_id = db.Column(db.String(20), unique=True, nullable=False, index=True)

    patient_id = db.Column(
        db.String(20),
        db.ForeignKey("patients.patient_id"),
        nullable=False,
        index=True
    )

    report_title = db.Column(db.String(200), nullable=False)
    report_type = db.Column(db.String(100), nullable=False)

    generated_by = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(100))

    hospital_id = db.Column(db.String(20), nullable=False)
    hospital_name = db.Column(db.String(150), nullable=False)

    report_status = db.Column(
        db.String(50),
        nullable=False,
        default="Generated"
    )

    ai_summary = db.Column(db.Text)
    findings = db.Column(db.Text)
    recommendations = db.Column(db.Text)

    risk_score = db.Column(db.Float, default=0.0)
    fraud_probability = db.Column(db.Float, default=0.0)

    file_name = db.Column(db.String(255))
    file_path = db.Column(db.String(500))

    remarks = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    @property
    def is_high_risk(self):
        return self.risk_score >= 80

    def to_dict(self):
        return {
            "id": self.id,
            "report_id": self.report_id,
            "patient_id": self.patient_id,
            "report_title": self.report_title,
            "report_type": self.report_type,
            "generated_by": self.generated_by,
            "department": self.department,
            "hospital_id": self.hospital_id,
            "hospital_name": self.hospital_name,
            "report_status": self.report_status,
            "ai_summary": self.ai_summary,
            "findings": self.findings,
            "recommendations": self.recommendations,
            "risk_score": self.risk_score,
            "fraud_probability": self.fraud_probability,
            "file_name": self.file_name,
            "file_path": self.file_path,
            "remarks": self.remarks,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f"<Report {self.report_id}>"
