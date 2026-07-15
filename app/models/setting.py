"""
=========================================================
                    SETTINGS MODEL
        Modernized Healthcare PBM Portal
=========================================================
"""

from datetime import datetime

from app.extensions import db


class Setting(db.Model):
    """
    System Settings Model
    """

    __tablename__ = "settings"

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # =====================================================
    # SETTING INFORMATION
    # =====================================================

    setting_key = db.Column(
        db.String(100),
        unique=True,
        nullable=False,
        index=True
    )

    setting_value = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False,
        default="General"
    )

    description = db.Column(
        db.Text
    )

    data_type = db.Column(
        db.String(20),
        nullable=False,
        default="string"
    )
    # string
    # integer
    # float
    # boolean

    is_editable = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

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
    # HELPER METHODS
    # =====================================================

    def to_dict(self):

        return {

            "id": self.id,

            "setting_key": self.setting_key,

            "setting_value": self.setting_value,

            "category": self.category,

            "description": self.description,

            "data_type": self.data_type,

            "is_editable": self.is_editable,

            "created_at": (
                self.created_at.isoformat()
                if self.created_at
                else None
            ),

            "updated_at": (
                self.updated_at.isoformat()
                if self.updated_at
                else None
            )

        }

    def __repr__(self):

        return (

            f"<Setting "

            f"{self.setting_key}>"

        )