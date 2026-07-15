"""
=========================================================
    Modernized Web Portal for Healthcare (PBM)
    AI-Powered UX

    Flask Extensions
=========================================================
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail


mail = Mail()

# =========================================================
# Database
# =========================================================

db = SQLAlchemy()


# =========================================================
# Database Migration
# =========================================================

migrate = Migrate()


# =========================================================
# Login Manager
# =========================================================

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.login_message = (
    "Please login to continue."
)

login_manager.login_message_category = "warning"


# =========================================================
# Cross-Origin Resource Sharing
# =========================================================

cors = CORS()


# =========================================================
# Initialize Extensions
# =========================================================

def init_extensions(app):
    """
    Initialize all Flask extensions.
    """

    db.init_app(app)

    migrate.init_app(
        app,
        db
    )

    login_manager.init_app(app)

    cors.init_app(app)

    mail.init_app(app)