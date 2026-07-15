
"""
=========================================================
                HELPER FUNCTIONS
    Modernized Healthcare PBM Web Portal
=========================================================
"""

import random
import string
from datetime import datetime


def generate_patient_id():
    return "P" + str(random.randint(100000, 999999))


def generate_claim_id():
    return "C" + str(random.randint(100000, 999999))


def generate_report_id():
    return "R" + str(random.randint(100000, 999999))


def generate_pharmacy_id():
    return "PH" + str(random.randint(100000, 999999))


def calculate_bmi(height_cm, weight_kg):
    if not height_cm or not weight_kg:
        return 0.0

    height_m = height_cm / 100

    if height_m <= 0:
        return 0.0

    return round(weight_kg / (height_m ** 2), 2)


def format_currency(amount):
    return f"₹ {amount:,.2f}"


def format_datetime(value):
    if value is None:
        return ""
    return value.strftime("%d-%m-%Y %I:%M %p")


def format_date(value):
    if value is None:
        return ""
    return value.strftime("%d-%m-%Y")


def generate_random_password(length=10):
    chars = (
        string.ascii_letters +
        string.digits +
        "@#$%&!"
    )

    return "".join(
        random.choice(chars)
        for _ in range(length)
    )


def calculate_fraud_percentage(total, fraud):
    if total == 0:
        return 0.0

    return round((fraud / total) * 100, 2)


def current_timestamp():
    return datetime.utcnow()


def status_badge(status):
    mapping = {
        "Approved": "success",
        "Pending": "warning",
        "Rejected": "danger",
        "Generated": "primary",
        "Active": "success",
        "Inactive": "secondary"
    }

    return mapping.get(status, "info")


def risk_level(score):
    if score >= 80:
        return "High"

    if score >= 50:
        return "Medium"

    return "Low"


def truncate_text(text, length=100):
    if not text:
        return ""

    if len(text) <= length:
        return text

    return text[:length] + "..."
