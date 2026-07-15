
"""
=========================================================
                APPLICATION CONSTANTS
    Modernized Healthcare PBM Web Portal
=========================================================
"""

APP_NAME = "Modernized Healthcare PBM Web Portal"
VERSION = "1.0.0"

DEFAULT_COUNTRY = "India"

CLAIM_STATUS = [
    "Pending",
    "Approved",
    "Rejected"
]

INSURANCE_STATUS = [
    "Active",
    "Inactive",
    "Expired"
]

REPORT_STATUS = [
    "Generated",
    "Reviewed",
    "Archived"
]

USER_ROLES = [
    "Admin",
    "Analyst",
    "Doctor",
    "Pharmacist"
]

GENDERS = [
    "Male",
    "Female",
    "Other"
]

RISK_LEVELS = {
    "LOW": 0,
    "MEDIUM": 50,
    "HIGH": 80
}

DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

ALLOWED_EXTENSIONS = {
    "pdf",
    "png",
    "jpg",
    "jpeg",
    "csv",
    "xlsx"
}

SECRET_KEY_ENV = "SECRET_KEY"
DATABASE_ENV = "DATABASE_URL"

DATE_FORMAT = "%d-%m-%Y"
DATETIME_FORMAT = "%d-%m-%Y %H:%M:%S"

CURRENCY_SYMBOL = "₹"

FLASH_SUCCESS = "success"
FLASH_WARNING = "warning"
FLASH_DANGER = "danger"
FLASH_INFO = "info"
