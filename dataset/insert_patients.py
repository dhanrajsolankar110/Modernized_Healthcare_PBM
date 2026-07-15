import random
from datetime import datetime, timedelta

from app import create_app
from app.extensions import db
from app.models.patient import Patient

app = create_app()

first_names = [
    "Rahul","Amit","Priya","Sneha","Rohan","Pooja","Akash","Neha",
    "Vikas","Anjali","Suresh","Meena","Karan","Riya","Aditya",
    "Kavita","Vivek","Nikita","Ramesh","Aarti"
]

last_names = [
    "Sharma","Patil","Joshi","Gupta","Verma","Singh","Yadav",
    "Kulkarni","More","Deshmukh","Pawar","Jadhav","Patel",
    "Kumar","Shinde","Naik"
]

diseases = [
    "Fever",
    "Diabetes",
    "Asthma",
    "Cancer",
    "Heart Disease",
    "Hypertension",
    "Migraine"
]

blood_groups = [
    "A+","A-","B+","B-","AB+","AB-","O+","O-"
]

cities = [
    "Pune",
    "Mumbai",
    "Nagpur",
    "Nashik",
    "Kolhapur",
    "Aurangabad",
    "Solapur"
]

states = ["Maharashtra"]

insurance = [
    "Star Health",
    "ICICI Lombard",
    "HDFC ERGO",
    "Care Health",
    "Niva Bupa"
]

with app.app_context():

    if Patient.query.count() > 0:
        print("Patients already exist.")
        exit()

    for i in range(1,501):

        first = random.choice(first_names)
        last = random.choice(last_names)

        age = random.randint(18,80)

        patient = Patient(

            patient_id=f"P{i:04d}",

            first_name=first,

            last_name=last,

            gender=random.choice(["Male","Female"]),

            age=age,

            date_of_birth=datetime.now().date() - timedelta(days=age*365),

            blood_group=random.choice(blood_groups),

            phone=f"9{random.randint(100000000,999999999)}",

            email=f"{first.lower()}{i}@gmail.com",

            address=f"House No. {random.randint(1,500)}",

            city=random.choice(cities),

            state=random.choice(states),

            pincode=str(random.randint(400001,444999)),

            disease=random.choice(diseases),

            insurance_provider=random.choice(insurance),

            insurance_number=f"INS{random.randint(100000,999999)}",

            emergency_contact=f"9{random.randint(100000000,999999999)}",

            emergency_contact_name=random.choice(first_names),

            status=random.choice(["Active","Inactive"])

        )

        db.session.add(patient)

    db.session.commit()

    print("500 Patients Inserted Successfully!")