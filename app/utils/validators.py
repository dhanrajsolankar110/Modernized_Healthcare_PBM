
"""
=========================================================
                VALIDATORS
    Modernized Healthcare PBM Web Portal
=========================================================
"""

import re


def validate_email(email):
    if not email:
        return False
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def validate_phone(phone):
    if not phone:
        return False
    return re.fullmatch(r"[0-9]{10}", phone) is not None


def validate_patient_id(patient_id):
    return bool(re.fullmatch(r"P[0-9]{6}", patient_id or ""))


def validate_claim_id(claim_id):
    return bool(re.fullmatch(r"C[0-9]{6}", claim_id or ""))


def validate_report_id(report_id):
    return bool(re.fullmatch(r"R[0-9]{6}", report_id or ""))


def validate_pharmacy_id(pharmacy_id):
    return bool(re.fullmatch(r"PH[0-9]{6}", pharmacy_id or ""))


def validate_amount(amount):
    try:
        return float(amount) >= 0
    except (TypeError, ValueError):
        return False


def validate_age(age):
    try:
        age = int(age)
        return 0 < age <= 120
    except (TypeError, ValueError):
        return False


def validate_risk_score(score):
    try:
        score = float(score)
        return 0 <= score <= 100
    except (TypeError, ValueError):
        return False


def validate_required(value):
    return value is not None and str(value).strip() != ""


def validate_password(password):
    if not password or len(password) < 8:
        return False

    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    return all([has_upper, has_lower, has_digit, has_special])


def validate_policy_number(policy):
    return bool(policy and len(policy.strip()) >= 5)
