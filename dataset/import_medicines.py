import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

import pandas as pd

from app import create_app
from app.extensions import db
from app.models.pharmacy import Pharmacy

app = create_app()

CSV_FILE = "dataset/medicines.csv"

with app.app_context():

    if not os.path.exists(CSV_FILE):

        print("medicines.csv not found!")

        exit()

    df = pd.read_csv(CSV_FILE)

    inserted = 0

    skipped = 0

    for _, row in df.iterrows():

        existing = Pharmacy.query.filter_by(

            medicine_id=row["Medicine ID"]

        ).first()

        if existing:

            skipped += 1

            continue

        medicine = Pharmacy(

            medicine_id=row["Medicine ID"],

            medicine_name=row["Medicine Name"],

            category=row["Category"],

            manufacturer=row["Manufacturer"],

            batch_number=row["Batch Number"],

            expiry_date=pd.to_datetime(
                row["Expiry Date"]
            ).date(),

            stock_quantity=int(
                row["Stock Quantity"]
            ),

            unit_price=float(
                row["Unit Price"]
            ),

            supplier_name=row["Supplier Name"],

            status=row["Status"]

        )

        db.session.add(medicine)

        inserted += 1

    db.session.commit()

    print("=" * 50)

    print("Medicine Import Completed")

    print(f"Inserted : {inserted}")

    print(f"Skipped  : {skipped}")

    print("=" * 50)