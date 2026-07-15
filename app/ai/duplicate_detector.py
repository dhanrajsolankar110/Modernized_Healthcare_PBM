"""
=========================================================
        DUPLICATE CLAIM DETECTOR
=========================================================
"""

from app.models.claim import Claim


class DuplicateDetector:

    def check_duplicate(self, claim):

        duplicate = Claim.query.filter(

            Claim.patient_id == claim.patient_id,

            Claim.disease == claim.disease,

            Claim.claim_amount == claim.claim_amount,

            Claim.id != claim.id

        ).first()

        if duplicate:

            return True

        return False