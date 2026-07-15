"""
=========================================================
            AI MODEL TRAINING
=========================================================
"""

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(

    "dataset/fraud_claims.csv"

)


hospital_encoder = LabelEncoder()

disease_encoder = LabelEncoder()

df["Hospital"] = hospital_encoder.fit_transform(
    df["Hospital"]
)

df["Disease"] = disease_encoder.fit_transform(
    df["Disease"]
)

X = df[

    [

        "Hospital",

        "Disease",

        "Age",

        "Treatment_Cost",

        "Claim_Amount",

        "Previous_Claims",

        "Duplicate_Claim"

    ]

]

y = df["Fraud"]

X_train,X_test,y_train,y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42

)

model.fit(

    X_train,

    y_train

)

prediction=model.predict(X_test)

accuracy=accuracy_score(

    y_test,

    prediction

)

print()

print("="*45)

print("MODEL TRAINED SUCCESSFULLY")

print("="*45)

print("Accuracy :",round(accuracy*100,2),"%")

joblib.dump(

    model,

    "model/fraud_model.pkl"

)

joblib.dump(
    hospital_encoder,
    "model/hospital_encoder.pkl"
)

joblib.dump(
    disease_encoder,
    "model/disease_encoder.pkl"
)

print()

print("Model Saved Successfully")