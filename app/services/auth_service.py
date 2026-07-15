"""
=========================================================
    Authentication Service

    Modernized Web Portal for Healthcare (PBM)
=========================================================
"""

from datetime import datetime

from app.extensions import db
from app.models.user import User


class AuthService:
    """
    Authentication Business Logic
    """

    # =====================================================
    # Register User
    # =====================================================

    @staticmethod
    def register_user(
        full_name,
        username,
        email,
        password,
        role="Administrator"
    ):

        # Check username

        if User.query.filter_by(
            username=username
        ).first():

            return False, "Username already exists."

        # Check email

        if User.query.filter_by(
            email=email
        ).first():

            return False, "Email already exists."

        # Create user

        user = User(

            full_name=full_name,

            username=username,

            email=email,

            role=role

        )

        user.set_password(password)

        db.session.add(user)

        db.session.commit()

        return True, "Registration successful."

    # =====================================================
    # Login User
    # =====================================================

    @staticmethod
    def login_user(username, password):

        user = User.query.filter_by(

            username=username

        ).first()

        if not user:

            return False, "User not found.", None

        if not user.is_active_account:

            return False, "Account is disabled.", None

        if not user.check_password(password):

            return False, "Invalid password.", None

        user.last_login = datetime.utcnow()

        db.session.commit()

        return True, "Login successful.", user

    # =====================================================
    # Find User
    # =====================================================

    @staticmethod
    def get_user(user_id):

        return User.query.get(user_id)

    # =====================================================
    # Find by Username
    # =====================================================

    @staticmethod
    def get_user_by_username(username):

        return User.query.filter_by(

            username=username

        ).first()

    # =====================================================
    # Find by Email
    # =====================================================

    @staticmethod
    def get_user_by_email(email):

        return User.query.filter_by(

            email=email

        ).first()

    # =====================================================
    # Update Password
    # =====================================================

    @staticmethod
    def update_password(user, new_password):

        user.set_password(new_password)

        db.session.commit()

        return True

    # =====================================================
    # Activate Account
    # =====================================================

    @staticmethod
    def activate(user):

        user.is_active_account = True

        db.session.commit()

    # =====================================================
    # Deactivate Account
    # =====================================================

    @staticmethod
    def deactivate(user):

        user.is_active_account = False

        db.session.commit()

    # =====================================================
    # Delete User
    # =====================================================

    @staticmethod
    def delete(user):

        db.session.delete(user)

        db.session.commit()