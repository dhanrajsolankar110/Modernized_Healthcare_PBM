"""
=========================================================
    User Model

    Modernized Web Portal for Healthcare (PBM)
=========================================================
"""

from datetime import datetime

from flask_login import UserMixin

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.extensions import (
    db,
    login_manager
)


# =========================================================
# User Loader
# =========================================================

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


# =========================================================
# User Model
# =========================================================

class User(UserMixin, db.Model):

    __tablename__ = "users"

    # -----------------------------------------------------
    # Primary Key
    # -----------------------------------------------------

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # -----------------------------------------------------
    # Personal Information
    # -----------------------------------------------------

    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    # -----------------------------------------------------
    # Security
    # -----------------------------------------------------

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    # -----------------------------------------------------
    # Role
    # -----------------------------------------------------

    role = db.Column(
        db.String(30),
        default="Administrator"
    )

    # -----------------------------------------------------
    # Account Status
    # -----------------------------------------------------

    is_active_account = db.Column(
        db.Boolean,
        default=True
    )

    # -----------------------------------------------------
    # Dates
    # -----------------------------------------------------

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    last_login = db.Column(
        db.DateTime
    )

    # =====================================================
    # Password Methods
    # =====================================================

    def set_password(self, password):

        self.password_hash = generate_password_hash(
            password
        )

    def check_password(self, password):

        return check_password_hash(
            self.password_hash,
            password
        )

    # =====================================================
    # Login
    # =====================================================

    @property
    def is_active(self):

        return self.is_active_account

    # =====================================================
    # Dictionary
    # =====================================================

    def to_dict(self):

        return {

            "id": self.id,

            "full_name": self.full_name,

            "username": self.username,

            "email": self.email,

            "role": self.role,

            "is_active": self.is_active_account,

            "created_at": self.created_at,

            "last_login": self.last_login

        }

    # =====================================================
    # String
    # =====================================================

    def __repr__(self):

        return (

            f"<User {self.username}>"

        )