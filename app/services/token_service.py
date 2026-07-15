"""
=========================================================
        PASSWORD RESET TOKEN SERVICE
=========================================================
"""

from itsdangerous import URLSafeTimedSerializer
from flask import current_app


class TokenService:

    @staticmethod
    def generate_reset_token(email):

        serializer = URLSafeTimedSerializer(

            current_app.config["SECRET_KEY"]

        )

        return serializer.dumps(

            email,

            salt="password-reset"

        )

    @staticmethod
    def verify_reset_token(token, expires=900):
        """
        expires = 900 seconds (15 minutes)
        """

        serializer = URLSafeTimedSerializer(

            current_app.config["SECRET_KEY"]

        )

        try:

            email = serializer.loads(

                token,

                salt="password-reset",

                max_age=expires

            )

            return email

        except Exception:

            return None