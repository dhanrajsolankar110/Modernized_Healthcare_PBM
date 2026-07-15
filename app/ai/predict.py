"""
=========================================================
            AI FRAUD PREDICTION ENGINE
=========================================================
"""

import joblib
import pandas as pd
from app.services.system_service import SystemService


class FraudPredictor:

    def __init__(self):

        self.model = joblib.load(
            "model/fraud_model.pkl"
        )

        self.hospital_encoder = joblib.load(
            "model/hospital_encoder.pkl"
        )

        self.disease_encoder = joblib.load(
            "model/disease_encoder.pkl"
        )

    def _encode_hospital(self, hospital):

        if hospital not in self.hospital_encoder.classes_:

            hospital = self.hospital_encoder.classes_[0]

        return self.hospital_encoder.transform(
            [hospital]
        )[0]

    def _encode_disease(self, disease):

        if disease not in self.disease_encoder.classes_:

            disease = self.disease_encoder.classes_[0]

        return self.disease_encoder.transform(
            [disease]
        )[0]

    def predict(

        self,

        hospital,

        disease,

        age,

        treatment_cost,

        claim_amount,

        previous_claims,

        duplicate_claim

    ):

        hospital = self._encode_hospital(
            hospital
        )

        disease = self._encode_disease(
            disease
        )

        sample = pd.DataFrame(

            [[

                hospital,

                disease,

                age,

                treatment_cost,

                claim_amount,

                previous_claims,

                duplicate_claim

            ]],

            columns=[

                "Hospital",

                "Disease",

                "Age",

                "Treatment_Cost",

                "Claim_Amount",

                "Previous_Claims",

                "Duplicate_Claim"

            ]

        )

        prediction = self.model.predict(
            sample
        )[0]

        probability = self.model.predict_proba(
            sample
        )[0][1]

        risk_score = round(
            probability * 100,
            2
        )


        threshold = float(

            SystemService.get(

                "fraud_threshold",

                80

            )

        )

        if risk_score >= threshold:

            level = "High"

        elif risk_score >= 50:

            level = "Medium"

        else:

            level = "Low"

        return {

            "prediction": int(prediction),

            "risk_score": risk_score,

            "risk_level": level

        }