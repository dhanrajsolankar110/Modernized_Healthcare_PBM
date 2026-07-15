"""
=========================================================
                SETTINGS ROUTES
        Modernized Healthcare PBM Portal
=========================================================
"""

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from app.extensions import db
from app.models.setting import Setting
from app.services.backup_service import BackupService
from flask import send_file

settings_bp = Blueprint(
    "settings",
    __name__,
    url_prefix="/settings"
)

@settings_bp.route("/")
def index():

    settings = Setting.query.order_by(
        Setting.category.asc(),
        Setting.setting_key.asc()
    ).all()

    total_settings = len(settings)

    editable_settings = Setting.query.filter_by(
        is_editable=True
    ).count()

    locked_settings = Setting.query.filter_by(
        is_editable=False
    ).count()

    categories = db.session.query(
        Setting.category
    ).distinct().count()

    return render_template(

        "settings/index.html",

        settings=settings,

        total_settings=total_settings,

        editable_settings=editable_settings,

        locked_settings=locked_settings,

        categories=categories

    )

@settings_bp.route(
    "/edit/<int:id>",
    methods=["GET", "POST"]
)
def edit(id):

    setting = Setting.query.get_or_404(id)

    if request.method == "POST":

        if setting.is_editable:

            setting.setting_value = request.form.get(
                "setting_value"
            )

            db.session.commit()

            flash(

                "Setting updated successfully.",

                "success"

            )

        else:

            flash(

                "This setting is locked.",

                "warning"

            )

        return redirect(

            url_for("settings.index")

        )

    return render_template(

        "settings/edit.html",

        setting=setting

    )

@settings_bp.route("/reset/<int:id>")
def reset(id):

    setting = Setting.query.get_or_404(id)

    if setting.is_editable:

        setting.setting_value = ""

        db.session.commit()

        flash(

            "Setting reset successfully.",

            "success"

        )

    else:

        flash(

            "Locked settings cannot be reset.",

            "warning"

        )

    return redirect(

        url_for("settings.index")

    )

@settings_bp.route("/delete/<int:id>")
def delete(id):

    setting = Setting.query.get_or_404(id)

    if not setting.is_editable:

        flash(

            "Locked settings cannot be deleted.",

            "danger"

        )

        return redirect(

            url_for("settings.index")

        )

    db.session.delete(setting)

    db.session.commit()

    flash(

        "Setting deleted successfully.",

        "success"

    )

    return redirect(

        url_for("settings.index")

    )

@settings_bp.route("/initialize")
def initialize():

    if Setting.query.count() == 0:

        defaults = [

            {
                "setting_key": "portal_name",
                "setting_value": "Modernized Healthcare PBM",
                "category": "General",
                "description": "Portal Name"
            },

            {
                "setting_key": "hospital_name",
                "setting_value": "City Hospital",
                "category": "General",
                "description": "Hospital Name"
            },

            {
                "setting_key": "fraud_threshold",
                "setting_value": "80",
                "category": "AI",
                "description": "Fraud Detection Threshold"
            },

            {
                "setting_key": "session_timeout",
                "setting_value": "30",
                "category": "Security",
                "description": "Session Timeout (Minutes)"
            },

            {
                "setting_key": "email_notifications",
                "setting_value": "Enabled",
                "category": "Notifications",
                "description": "Email Notifications"
            }

        ]

        for item in defaults:

            db.session.add(

                Setting(

                    setting_key=item["setting_key"],

                    setting_value=item["setting_value"],

                    category=item["category"],

                    description=item["description"],

                    data_type="string",

                    is_editable=True

                )

            )

        db.session.commit()

        flash(

            "Default settings created successfully.",

            "success"

        )

    else:

        flash(

            "Settings already initialized.",

            "info"

        )

    return redirect(

        url_for("settings.index")

    )

@settings_bp.route("/backup")
def backup():

    backup_path, filename = BackupService.create_backup()

    return send_file(

        backup_path,

        as_attachment=True,

        download_name=filename,

        mimetype="application/octet-stream"

    )

@settings_bp.route(
    "/backup-manager",
    methods=["GET", "POST"]
)
def backup_manager():

    if request.method == "POST":

        flash(

            "Backup restore feature will be available in the next version.",

            "info"

        )

        return redirect(

            url_for(

                "settings.backup_manager"

            )

        )

    return render_template(

        "settings/backup.html"

    )