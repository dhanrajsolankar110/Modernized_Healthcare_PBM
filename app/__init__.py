
"""
=========================================================
        APPLICATION FACTORY
    Modernized Healthcare PBM Web Portal
=========================================================
"""

from flask import Flask, redirect, url_for

from config import config
from app.extensions import (
    init_extensions,
    login_manager
)

# Models
# Models
import app.models
from app.models.notification import Notification
from app.services.system_service import SystemService
from datetime import timedelta

# Blueprints
from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp
from app.routes.patient import patient_bp
from app.routes.claim import claim_bp
from app.routes.pharmacy import pharmacy_bp
from app.routes.reports import reports_bp
from app.routes.fraud import fraud_bp
from app.routes.notifications import notifications_bp
from app.routes.settings import settings_bp



@login_manager.user_loader
def load_user(user_id):
    return app.models.User.query.get(int(user_id))


def create_app(config_name="development"):
    app = Flask(__name__)

    app.config.from_object(
        config.get(
            config_name,
            config["default"]
        )
    )

    print("MAIL_USERNAME:", app.config["MAIL_USERNAME"])
    print("MAIL_PASSWORD:", app.config["MAIL_PASSWORD"])

    init_extensions(app)

    with app.app_context():

        app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(

            minutes=int(

                SystemService.get(

                    "session_timeout",

                    30

                )

            )

        )


    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(claim_bp)
    app.register_blueprint(pharmacy_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(fraud_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(settings_bp)

    @app.context_processor
    def inject_globals():
        return {
            "APP_NAME": app.config.get("APP_NAME"),
            "VERSION": app.config.get("VERSION")
        }

    @app.route("/")
    def home():
        return redirect(url_for("auth.login"))
    
    @app.context_processor
    def inject_notifications():

        unread_notifications = Notification.query.filter_by(
            status="Unread"
        ).count()

        return dict(

            unread_notifications=unread_notifications

        )

    return app
