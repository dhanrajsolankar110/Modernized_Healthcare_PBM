"""
=========================================================
    Patient Model
    Modernized Healthcare PBM Portal
=========================================================
"""

from datetime import datetime

from app.extensions import db


class Patient(db.Model):
    """
    Patient Database Model
    """

    __tablename__ = "patients"

    # =====================================================
    # Primary Key
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # =====================================================
    # Patient Information
    # =====================================================

    patient_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        index=True
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    gender = db.Column(
        db.String(20),
        nullable=False
    )

    age = db.Column(
        db.Integer,
        nullable=False
    )

    date_of_birth = db.Column(
        db.Date,
        nullable=True
    )

    blood_group = db.Column(
        db.String(5),
        nullable=True
    )

    # =====================================================
    # Contact Information
    # =====================================================

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=True
    )

    address = db.Column(
        db.Text,
        nullable=True
    )

    city = db.Column(
        db.String(100),
        nullable=True
    )

    state = db.Column(
        db.String(100),
        nullable=True
    )

    pincode = db.Column(
        db.String(10),
        nullable=True
    )

    # =====================================================
    # Medical Information
    # =====================================================

    disease = db.Column(
        db.String(150),
        nullable=True
    )

    insurance_provider = db.Column(
        db.String(150),
        nullable=True
    )

    insurance_number = db.Column(
        db.String(100),
        nullable=True
    )

    emergency_contact = db.Column(
        db.String(20),
        nullable=True
    )

    emergency_contact_name = db.Column(
        db.String(100),
        nullable=True
    )

    # =====================================================
    # Status
    # =====================================================

    status = db.Column(
        db.String(20),
        default="Active",
        nullable=False
    )

    # =====================================================
    # Audit Information
    # =====================================================

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

    # =====================================================
    # Helper Properties
    # =====================================================

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_address(self):

        address_parts = [
            self.address,
            self.city,
            self.state,
            self.pincode
        ]

        return ", ".join(
            str(part)
            for part in address_parts
            if part
        )

    @property
    def is_active(self):
        return self.status == "Active"

    # =====================================================
    # Utility Methods
    # =====================================================

    def activate(self):
        self.status = "Active"

    def deactivate(self):
        self.status = "Inactive"

    def to_dict(self):

        return {

            "id": self.id,
            "patient_id": self.patient_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "gender": self.gender,
            "age": self.age,
            "date_of_birth": self.date_of_birth.isoformat()
            if self.date_of_birth else None,
            "blood_group": self.blood_group,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "disease": self.disease,
            "insurance_provider": self.insurance_provider,
            "insurance_number": self.insurance_number,
            "emergency_contact": self.emergency_contact,
            "emergency_contact_name": self.emergency_contact_name,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()

        }

    # =====================================================
    # String Representation
    # =====================================================

    def __repr__(self):
        return f"<Patient {self.patient_id} - {self.full_name}>"