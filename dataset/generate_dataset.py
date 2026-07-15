import pandas as pd
import random

# Number of Patients
TOTAL_PATIENTS = 500

first_names = [
    "Aarav", "Vivaan", "Aditya", "Rahul", "Rohan",
    "Priya", "Ananya", "Sneha", "Pooja", "Neha",
    "Karan", "Arjun", "Diya", "Meera", "Ishita",
    "Sanjay", "Ritika", "Kavya", "Aisha", "Nikhil"
]

last_names = [
    "Sharma", "Patel", "Gupta", "Singh", "Joshi",
    "Kulkarni", "Patil", "Reddy", "Naik", "Verma"
]

genders = [
    "Male",
    "Female"
]

diseases = [
    "Diabetes",
    "Hypertension",
    "Asthma",
    "Heart Disease",
    "Cancer",
    "Fever",
    "Migraine",
    "COVID-19",
    "Kidney Disease",
    "Arthritis"
]

statuses = [
    "Active",
    "Inactive"
]

patients = []

for i in range(1, TOTAL_PATIENTS + 1):

    patient = {
        "Patient ID": f"P{i:04d}",
        "Name": f"{random.choice(first_names)} {random.choice(last_names)}",
        "Gender": random.choice(genders),
        "Age": random.randint(1, 85),
        "Phone": f"9{random.randint(100000000, 999999999)}",
        "Disease": random.choice(diseases),
        "Status": random.choice(statuses)
    }

    patients.append(patient)

# Create DataFrame
df = pd.DataFrame(patients)

# Save CSV
df.to_csv("patients.csv", index=False)

print("=" * 50)
print("Patients Dataset Generated Successfully")
print(f"Total Patients : {TOTAL_PATIENTS}")
print("File Name      : patients.csv")
print("=" * 50)

print(df.head())