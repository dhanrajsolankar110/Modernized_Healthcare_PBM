"""
=========================================================
                    CLAIM MODEL
        Modernized Healthcare PBM Portal
=========================================================
"""

from datetime import datetime

from app.extensions import db


class Claim(db.Model):
    """
    Claim Management Model
    """

    __tablename__ = "claims"

    # =====================================================
    # Primary Key
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # =====================================================
    # Claim Information
    # =====================================================

    claim_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        index=True
    )

    patient_id = db.Column(
        db.String(20),
        db.ForeignKey("patients.patient_id"),
        nullable=False,
        index=True
    )

    hospital_name = db.Column(
        db.String(150),
        nullable=False
    )

    doctor_name = db.Column(
        db.String(150),
        nullable=False
    )

    disease = db.Column(
        db.String(120),
        nullable=False
    )

    claim_amount = db.Column(
        db.Float,
        nullable=False
    )

    treatment_date = db.Column(
        db.Date,
        nullable=False
    )

    submission_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Pending",
        nullable=False
    )

    predicted_risk = db.Column(
    db.Float,
    default=0.0
    )

    risk_level = db.Column(
        db.String(20),
        default="Not Predicted"
    )

    duplicate_claim = db.Column(
        db.Boolean,
        default=False
    )

    ai_remark = db.Column(
        db.Text
    )

    prediction_date = db.Column(
        db.DateTime
    )

    remarks = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # =====================================================
    # Relationship
    # =====================================================

    patient = db.relationship(
        "Patient",
        backref=db.backref(
            "claims",
            lazy=True
        )
    )

    # =====================================================
    # Helper Methods
    # =====================================================

    @property
    def formatted_amount(self):
        return f"₹{self.claim_amount:,.2f}"

    @property
    def is_pending(self):
        return self.status == "Pending"

    @property
    def is_approved(self):
        return self.status == "Approved"

    @property
    def is_rejected(self):
        return self.status == "Rejected"

    def to_dict(self):
        return {
            "id": self.id,
            "claim_id": self.claim_id,
            "patient_id": self.patient_id,
            "hospital_name": self.hospital_name,
            "doctor_name": self.doctor_name,
            "disease": self.disease,
            "claim_amount": self.claim_amount,
            "treatment_date": self.treatment_date.strftime("%Y-%m-%d"),
            "submission_date": self.submission_date.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status,
            "remarks": self.remarks
        }

    def __repr__(self):
        return f"<Claim {self.claim_id}>"