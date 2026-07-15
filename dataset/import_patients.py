import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from datetime import datetime

from app import create_app
from app.extensions import db
from app.models.patient import Patient

app = create_app()

CSV_FILE = "dataset/patients.csv"

with app.app_context():

    df = pd.read_csv(CSV_FILE)

    print(f"Found {len(df)} records.")

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():

        existing = Patient.query.filter_by(
            patient_id=str(row["Patient ID"])
        ).first()

        if existing:
            skipped += 1
            continue

        dob = None

        if "Date of Birth" in df.columns:

            try:
                dob = pd.to_datetime(
                    row["Date of Birth"]
                ).date()
            except:
                dob = None

        patient = Patient(

            patient_id=str(row["Patient ID"]),

            first_name=str(row["Name"]).split()[0],

            last_name=" ".join(
                str(row["Name"]).split()[1:]
            ) or "Unknown",

            gender=str(row["Gender"]),

            age=int(row["Age"]),

            date_of_birth=dob,

            blood_group=str(row["Blood Group"])
            if "Blood Group" in df.columns else None,

            phone=str(row["Phone"]),

            email=str(row["Email"])
            if "Email" in df.columns else None,

            address=str(row["Address"])
            if "Address" in df.columns else None,

            city=str(row["City"])
            if "City" in df.columns else None,

            state=str(row["State"])
            if "State" in df.columns else None,

            pincode=str(row["Pincode"])
            if "Pincode" in df.columns else None,

            disease=str(row["Disease"]),

            insurance_provider=str(row["Insurance Provider"])
            if "Insurance Provider" in df.columns else None,

            insurance_number=str(row["Insurance Number"])
            if "Insurance Number" in df.columns else None,

            emergency_contact=str(row["Emergency Contact"])
            if "Emergency Contact" in df.columns else None,

            emergency_contact_name=str(row["Emergency Contact Name"])
            if "Emergency Contact Name" in df.columns else None,

            status=str(row["Status"])

        )

        db.session.add(patient)

        inserted += 1

    db.session.commit()

    print("=" * 50)
    print(f"Inserted : {inserted}")
    print(f"Skipped  : {skipped}")
    print("Patients imported successfully!")
    print("=" * 50)