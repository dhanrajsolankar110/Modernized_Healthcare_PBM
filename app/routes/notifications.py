"""
=========================================================
            NOTIFICATION ROUTES
    Modernized Healthcare PBM Portal
=========================================================
"""

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from app.extensions import db
from app.models.notification import Notification

notifications_bp = Blueprint(
    "notifications",
    __name__,
    url_prefix="/notifications"
)

@notifications_bp.route("/")
def index():

    notifications = Notification.query.order_by(
        Notification.created_at.desc()
    ).all()

    total_notifications = len(notifications)

    unread_notifications = Notification.query.filter_by(
        status="Unread"
    ).count()

    read_notifications = Notification.query.filter_by(
        status="Read"
    ).count()

    high_priority = Notification.query.filter(
        Notification.priority.in_(["Critical", "High"])
    ).count()

    return render_template(

        "notifications/index.html",

        notifications=notifications,

        total_notifications=total_notifications,

        unread_notifications=unread_notifications,

        read_notifications=read_notifications,

        high_priority=high_priority

    )

@notifications_bp.route("/read/<int:id>")
def mark_read(id):

    notification = Notification.query.get_or_404(id)

    notification.status = "Read"

    db.session.commit()

    flash(

        "Notification marked as read.",

        "success"

    )

    return redirect(

        url_for("notifications.index")

    )

@notifications_bp.route("/unread/<int:id>")
def mark_unread(id):

    notification = Notification.query.get_or_404(id)

    notification.status = "Unread"

    db.session.commit()

    flash(

        "Notification marked as unread.",

        "success"

    )

    return redirect(

        url_for("notifications.index")

    )

@notifications_bp.route("/read-all")
def mark_all_read():

    Notification.query.filter_by(

        status="Unread"

    ).update(

        {

            "status": "Read"

        }

    )

    db.session.commit()

    flash(

        "All notifications marked as read.",

        "success"

    )

    return redirect(

        url_for("notifications.index")

    )

@notifications_bp.route("/delete/<int:id>")
def delete(id):

    notification = Notification.query.get_or_404(id)

    db.session.delete(notification)

    db.session.commit()

    flash(

        "Notification deleted successfully.",

        "success"

    )

    return redirect(

        url_for("notifications.index")

    )

@notifications_bp.route("/delete-all")
def delete_all():

    Notification.query.delete()

    db.session.commit()

    flash(

        "All notifications deleted successfully.",

        "success"

    )

    return redirect(

        url_for("notifications.index")

    )