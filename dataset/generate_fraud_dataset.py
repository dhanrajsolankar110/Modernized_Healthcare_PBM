"""
=========================================================
        FRAUD DATASET GENERATOR
=========================================================
"""

import random
import pandas as pd
from datetime import datetime, timedelta

random.seed(42)

diseases = [

    "Diabetes",
    "Heart Disease",
    "Cancer",
    "Asthma",
    "Hypertension",
    "Kidney Failure",
    "Fracture",
    "COVID-19"

]

hospitals = [

    "Apollo Hospital",
    "Fortis Hospital",
    "AIIMS",
    "Ruby Hall",
    "Max Hospital",
    "KEM Hospital"

]

rows = []

for i in range(1000):

    claim_id = f"C{i+1:05d}"

    patient_id = f"P{random.randint(1,500):04d}"

    hospital = random.choice(hospitals)

    disease = random.choice(diseases)

    age = random.randint(18,80)

    treatment_cost = random.randint(5000,150000)

    claim_amount = treatment_cost + random.randint(-3000,60000)

    previous_claims = random.randint(0,8)

    duplicate = random.randint(0,1)

    days = random.randint(1,365)

    claim_date = datetime.now()-timedelta(days=days)

    fraud = 0

    if(

        claim_amount > treatment_cost*1.45

        or duplicate==1

        or previous_claims>=5

    ):

        fraud=1

    rows.append({

        "Claim_ID":claim_id,

        "Patient_ID":patient_id,

        "Hospital":hospital,

        "Disease":disease,

        "Age":age,

        "Treatment_Cost":treatment_cost,

        "Claim_Amount":claim_amount,

        "Previous_Claims":previous_claims,

        "Duplicate_Claim":duplicate,

        "Fraud":fraud,

        "Claim_Date":claim_date.strftime("%Y-%m-%d")

    })

df=pd.DataFrame(rows)

df.to_csv(

    "dataset/fraud_claims.csv",

    index=False

)

print(df.head())

print()

print("Dataset Generated Successfully")

print("Total Records :",len(df))