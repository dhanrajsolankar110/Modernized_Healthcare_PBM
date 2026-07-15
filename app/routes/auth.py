"""
=========================================================
    Authentication Blueprint

    Modernized Web Portal for Healthcare (PBM)
=========================================================
"""

import logging

logger = logging.getLogger(__name__)

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from app.services.token_service import TokenService
from app.extensions import mail
from flask_mail import Message


# =========================================================
# Blueprint
# =========================================================

auth_bp = Blueprint(

    "auth",

    __name__,

    url_prefix="/auth"

)


# =========================================================
# Login
# =========================================================

from flask_login import current_user
from werkzeug.security import check_password_hash
from flask import render_template
from datetime import datetime
from app.models.user import User
from app.extensions import db

@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.index"))

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(
            username=username
        ).first()

        if user and user.check_password(password):

            login_user(user)

            user.last_login = datetime.utcnow()
            db.session.commit()

            flash(
                "Login successful.",
                "success"
            )

            return redirect(
                url_for("dashboard.index")
            )

        flash(
            "Invalid username or password.",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )


# =========================================================
# Register
# =========================================================

from app.models.user import User
from app.extensions import db

@auth_bp.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")

        if User.query.filter_by(username=username).first():

            flash(
                "Username already exists.",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        if User.query.filter_by(email=email).first():

            flash(
                "Email already exists.",
                "danger"
            )

            return redirect(
                url_for("auth.register")
            )

        user = User(

            full_name=full_name,

            username=username,

            email=email,

            role=role

        )

        user.set_password(password)

        db.session.add(user)

        db.session.commit()

        flash(
            "Registration successful. Please login.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/register.html"
    )


# =========================================================
# Logout
# =========================================================

@auth_bp.route(

    "/logout"

)

@login_required

def logout():

    logout_user()

    session.clear()

    flash(

        "Logged out successfully.",

        "success"

    )

    return redirect(

        url_for(

            "auth.login"

        )

    )


# =========================================================
# Forgot Password
# =========================================================

@auth_bp.route(
    "/forgot-password",
    methods=["GET", "POST"]
)
def forgot_password():

    if current_user.is_authenticated:

        return redirect(

        url_for("dashboard.index")

        )

    if request.method == "POST":

        email = request.form.get("email", "").strip()

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:

            flash(
                "No account found with that email.",
                "danger"
            )

            return redirect(
                url_for("auth.forgot_password")
            )

        token = TokenService.generate_reset_token(
            email
        )

        reset_link = url_for(
            "auth.reset_password",
            token=token,
            _external=True
        )

        msg = Message(

            subject="Password Reset",

            recipients=[email]

        )

        msg.html = render_template(

    "emails/reset_password.html",

    user=user,

    reset_link=reset_link,

    year=datetime.now().year

)
        
        msg.body = f"""

Password Reset

Open this link:

{reset_link}

This link expires in 15 minutes.

"""

        mail.send(msg)

        flash(

            "Password reset link has been sent to your email.",

            "success"

        )

        return redirect(

            url_for("auth.login")

        )

    return render_template(

        "auth/forgot_password.html"

    )

@auth_bp.route(
    "/reset-password/<token>",
    methods=["GET", "POST"]
)
def reset_password(token):

    if current_user.is_authenticated:

        return redirect(

        url_for("dashboard.index")

        )

    email = TokenService.verify_reset_token(
        token
    )

    if not email:

        flash(

            "Reset link is invalid or has expired.",

            "danger"

        )

        return redirect(

            url_for("auth.forgot_password")

        )

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        flash(

            "User account not found.",

            "danger"

        )

        return redirect(

            url_for("auth.login")

        )

    if request.method == "POST":

        password = request.form.get(
            "password",
            ""
        )

        confirm_password = request.form.get(
            "confirm_password",
            ""
        )

        if password != confirm_password:

            flash(

                "Passwords do not match.",

                "danger"

            )

            return redirect(

                url_for(
                    "auth.reset_password",
                    token=token
                )

            )

        if len(password) < 8:

            flash(

                "Password must be at least 8 characters.",

                "warning"

            )

            return redirect(

                url_for(
                    "auth.reset_password",
                    token=token
                )

            )

        if check_password_hash(user.password_hash, password):

            flash(

            "Your new password must be different from your current password.",

            "warning"

            )

            return redirect(

                url_for(

                "auth.reset_password",

                token=token

                )

            )

        user.set_password(password)

        db.session.commit()

        msg = Message(

            subject="Password Changed Successfully",

            recipients=[user.email]

        )

        msg.html = f"""
        <h2>Password Changed</h2>

        <p>Hello <strong>{user.full_name}</strong>,</p>

        <p>Your password has been changed successfully.</p>

        <p>If you did not make this change, please contact the administrator immediately.</p>

        <hr>

        <p>Healthcare PBM Portal</p>
        """

        mail.send(msg)

        flash(

            "Your password has been updated successfully. Please log in using your new password.",

            "success"

        )

        return redirect(

            url_for("auth.login")

        )

    return render_template(

        "auth/reset_password.html"

    )

@auth_bp.route("/profile")
@login_required
def profile():

    return render_template(
        "auth/profile.html"
    )

    # =====================================================
# CHANGE PASSWORD
# =====================================================

    from werkzeug.security import check_password_hash

    if "change_password" in request.form:

        current_password = request.form.get(
            "current_password"
        )

        new_password = request.form.get(
            "new_password"
        )

        confirm_password = request.form.get(
            "confirm_password"
        )

        if not check_password_hash(

        current_user.password_hash,

        current_password

        ):

            flash(

            "Current password is incorrect.",

            "danger"

            )

            return redirect(

            url_for("auth.profile")

            )

        if new_password != confirm_password:

            flash(

            "New passwords do not match.",

            "danger"

            )

            return redirect(

            url_for("auth.profile")

            )

        if len(new_password) < 8:

            flash(

            "Password must be at least 8 characters.",

            "warning"

            )

            return redirect(

            url_for("auth.profile")

            )

        current_user.set_password(

        new_password

        )

        db.session.commit()

        flash(

        "Password changed successfully.",

        "success"

        )

        return redirect(

        url_for("auth.profile")

        )

@auth_bp.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():

    if request.method == "POST":

        # Your password changing logic

        pass

    return render_template(
        "auth/change_password.html"
    )

    url_for("auth.change_password")