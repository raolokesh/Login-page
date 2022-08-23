"""Logged-in page routes."""
from ast import main
from crypt import methods
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required, logout_user

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/home")
def home():
    return render_template(
        "layout.html"
    )

@main_bp.route("/user", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        "dashboard.html",
        title="Flask-Login Tutorial",
        current_user=current_user,
        body="You are now logged in!",
    )



@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))
