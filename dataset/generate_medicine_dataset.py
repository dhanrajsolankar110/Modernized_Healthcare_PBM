import pandas as pd
import random
from datetime import datetime, timedelta

medicine_names = [
    "Paracetamol","Amoxicillin","Azithromycin","Metformin","Aspirin",
    "Ibuprofen","Cetirizine","Omeprazole","Pantoprazole","Atorvastatin",
    "Diclofenac","Ciprofloxacin","Dolo 650","Crocin","Augmentin",
    "Monocef","ORS","Vitamin C","Vitamin D","Calcium Tablets"
]

categories = [
    "Tablet",
    "Capsule",
    "Syrup",
    "Injection",
    "Cream"
]

manufacturers = [
    "Sun Pharma",
    "Cipla",
    "Dr. Reddy's",
    "Mankind",
    "Lupin",
    "Alkem",
    "Torrent",
    "Abbott",
    "Pfizer",
    "Glenmark"
]

suppliers = [
    "Apollo Distributor",
    "MedPlus Supplier",
    "HealthCare Pharma",
    "Wellness Pharma",
    "ABC Medicals"
]

rows = []

for i in range(1,501):

    medicine_id = f"M{i:04d}"

    name = random.choice(medicine_names)

    category = random.choice(categories)

    manufacturer = random.choice(manufacturers)

    batch = f"B{random.randint(10000,99999)}"

    expiry = (
        datetime.today() +
        timedelta(days=random.randint(180,1500))
    ).date()

    stock = random.randint(0,500)

    price = round(random.uniform(10,2500),2)

    supplier = random.choice(suppliers)

    if stock == 0:

        status = "Out of Stock"

    elif stock < 20:

        status = "Low Stock"

    else:

        status = "Available"

    rows.append({

        "Medicine ID": medicine_id,

        "Medicine Name": name,

        "Category": category,

        "Manufacturer": manufacturer,

        "Batch Number": batch,

        "Expiry Date": expiry,

        "Stock Quantity": stock,

        "Unit Price": price,

        "Supplier Name": supplier,

        "Status": status

    })

df = pd.DataFrame(rows)

df.to_csv("dataset/medicines.csv", index=False)

print("="*50)
print("Medicine Dataset Generated Successfully")
print("Total Medicines :", len(df))
print("File Name       : medicines.csv")
print("="*50)
print(df.head())