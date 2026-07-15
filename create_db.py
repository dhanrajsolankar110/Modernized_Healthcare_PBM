from app import create_app
from app.extensions import db

# Import ALL models
from app.models.user import User
from app.models.patient import Patient
from app.models.claim import Claim
from app.models.pharmacy import Pharmacy
from app.models.report import Report

app = create_app()

with app.app_context():
    db.create_all()
    print("=" * 50)
    print("Database created successfully!")
    print("=" * 50)