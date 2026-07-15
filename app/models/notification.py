"""
=========================================================
                NOTIFICATION MODEL
        Modernized Healthcare PBM Portal
=========================================================
"""

from datetime import datetime

from app.extensions import db


class Notification(db.Model):
    """
    Notification Database Model
    """

    __tablename__ = "notifications"

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # =====================================================
    # NOTIFICATION INFORMATION
    # =====================================================

    notification_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False,
        index=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=False
    )
    # Fraud
    # Claim
    # Pharmacy
    # Report
    # System

    priority = db.Column(
        db.String(20),
        default="Medium",
        nullable=False
    )
    # Critical
    # High
    # Medium
    # Low

    status = db.Column(
        db.String(20),
        default="Unread",
        nullable=False
    )
    # Read
    # Unread

    action_url = db.Column(
        db.String(255)
    )

    reference_id = db.Column(
        db.String(50)
    )

    icon = db.Column(
        db.String(50),
        default="fa-bell"
    )

    color = db.Column(
        db.String(20),
        default="primary"
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
    # HELPER PROPERTIES
    # =====================================================

    @property
    def is_read(self):
        return self.status == "Read"

    @property
    def is_unread(self):
        return self.status == "Unread"

    @property
    def is_high_priority(self):
        return self.priority in [
            "Critical",
            "High"
        ]

    # =====================================================
    # HELPER METHODS
    # =====================================================

    def mark_as_read(self):
        self.status = "Read"

    def mark_as_unread(self):
        self.status = "Unread"

    # =====================================================
    # SERIALIZATION
    # =====================================================

    def to_dict(self):

        return {

            "id": self.id,

            "notification_id": self.notification_id,

            "title": self.title,

            "message": self.message,

            "category": self.category,

            "priority": self.priority,

            "status": self.status,

            "action_url": self.action_url,

            "reference_id": self.reference_id,

            "icon": self.icon,

            "color": self.color,

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

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __repr__(self):
        return (
            f"<Notification "
            f"{self.notification_id} - "
            f"{self.title}>"
        )