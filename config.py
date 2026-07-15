"""
=========================================================
        Modernized Web Portal for Healthcare (PBM)
        AI-Powered UX

        Configuration File
=========================================================
"""

import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Base Configuration
    """

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    APP_NAME = "Healthcare PBM Portal"

    VERSION = "1.0.0"

    DEBUG = False

    TESTING = False

    # --------------------------------------------------
    # Security
    # --------------------------------------------------

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "pbm-healthcare-secret-key-2026"
    )

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    BASE_DIR = os.path.abspath(
        os.path.dirname(__file__)
    )

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" +
        os.path.join(
            BASE_DIR,
            "instance",
            "healthcare.db"
        )
    )

    # =====================================================
    # MAIL CONFIGURATION
    # =====================================================

    MAIL_SERVER = "smtp.gmail.com"

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USE_SSL = False

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")

    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    MAIL_DEFAULT_SENDER = os.getenv("MAIL_USERNAME")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------------------------------
    # Session
    # --------------------------------------------------

    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)

    SESSION_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SAMESITE = "Lax"

    # --------------------------------------------------
    # Uploads
    # --------------------------------------------------

    UPLOAD_FOLDER = os.path.join(
        BASE_DIR,
        "uploads"
    )

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = {

        "pdf",

        "png",

        "jpg",

        "jpeg",

        "csv",

        "xlsx"

    }

    # --------------------------------------------------
    # AI Configuration
    # --------------------------------------------------

    MODEL_FOLDER = os.path.join(

        BASE_DIR,

        "models"

    )

    REPORT_FOLDER = os.path.join(

        BASE_DIR,

        "reports"

    )

    CHART_FOLDER = os.path.join(

        BASE_DIR,

        "charts"

    )

    # --------------------------------------------------
    # Pagination
    # --------------------------------------------------

    RECORDS_PER_PAGE = 10

    # --------------------------------------------------
    # Dashboard Refresh
    # --------------------------------------------------

    DASHBOARD_REFRESH = 30

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    LOG_LEVEL = "INFO"

    # --------------------------------------------------
    # CORS
    # --------------------------------------------------

    CORS_HEADERS = "Content-Type"


class DevelopmentConfig(Config):

    DEBUG = True


class ProductionConfig(Config):

    DEBUG = False


class TestingConfig(Config):

    TESTING = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


config = {

    "development": DevelopmentConfig,

    "production": ProductionConfig,

    "testing": TestingConfig,

    "default": DevelopmentConfig

}