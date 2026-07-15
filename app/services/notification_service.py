"""
=========================================================
        NOTIFICATION SERVICE
Modernized Healthcare PBM Portal
=========================================================
"""

from datetime import datetime

from app.extensions import db
from app.models.notification import Notification


class NotificationService:

    @staticmethod
    def create_notification(

        title,

        message,

        category,

        priority="Medium",

        action_url=None,

        reference_id=None,

        icon="fa-bell",

        color="primary"

    ):

        notification = Notification(

            notification_id=f"NTF-{int(datetime.utcnow().timestamp())}",

            title=title,

            message=message,

            category=category,

            priority=priority,

            status="Unread",

            action_url=action_url,

            reference_id=reference_id,

            icon=icon,

            color=color

        )

        db.session.add(notification)

        db.session.commit()

        return notification