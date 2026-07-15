"""
=========================================================
                PHARMACY MODEL
        Modernized Healthcare PBM Portal
=========================================================
"""

from datetime import datetime

from app.extensions import db


class Pharmacy(db.Model):

    __tablename__ = "pharmacy"

    # ==========================================
    # Primary Key
    # ==========================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # ==========================================
    # Medicine Information
    # ==========================================

    medicine_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        index=True
    )

    medicine_name = db.Column(
        db.String(150),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=False
    )

    manufacturer = db.Column(
        db.String(150),
        nullable=False
    )

    batch_number = db.Column(
        db.String(50),
        nullable=False
    )

    expiry_date = db.Column(
        db.Date,
        nullable=False
    )

    stock_quantity = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    unit_price = db.Column(
        db.Float,
        nullable=False
    )

    supplier_name = db.Column(
        db.String(150)
    )

    status = db.Column(
        db.String(20),
        default="Available"
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

    # ==========================================
    # Helper Methods
    # ==========================================

    @property
    def formatted_price(self):
        return f"₹{self.unit_price:,.2f}"

    def __repr__(self):
        return f"<Medicine {self.medicine_name}>"