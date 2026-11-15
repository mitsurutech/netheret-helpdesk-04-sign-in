"""Signing in and out, and the checks that protect pages.

We write this by hand, without Flask-Login, so you can see how it works:
after a good sign in the user's id is saved in the session (a signed
cookie), and before every request we look that id up again.
"""
from functools import wraps

from flask import Blueprint, abort, flash, g, redirect, render_template, request, session, url_for

from .extensions import db
from .models import User

bp = Blueprint("auth", __name__)


@bp.before_app_request
def load_signed_in_user():
    """Runs before every request, so every page can use g.user."""
    user_id = session.get("user_id")
    g.user = db.session.get(User, user_id) if user_id else None


def login_required(view):
    """Put @login_required above a page that needs a signed-in user."""
    @wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            flash("Please sign in to see that page.")
            return redirect(url_for("auth.signin"))
        return view(*args, **kwargs)
    return wrapped


def role_required(*roles):
    """Put @role_required("manager") above a page for some roles only.

    It also checks the user is signed in, so you do not need both.
    """
    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if g.user is None:
                flash("Please sign in to see that page.")
                return redirect(url_for("auth.signin"))
            if g.user.role not in roles:
                abort(403)  # 403 means "Forbidden": signed in, but not allowed
            return view(*args, **kwargs)
        return wrapped
    return decorator


@bp.route("/signin", methods=["GET", "POST"])
def signin():
    error = None
    email = ""
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        given_password = request.form.get("password", "")
        user = db.session.scalar(db.select(User).where(User.email == email))
        # The same message whether the email or the password is wrong, so the
        # page does not tell a stranger which emails have accounts.
        if user is None or not user.check_password(given_password):
            error = "The email address or password is not right."
        else:
            # Start a fresh session, so nothing from before signing in is kept.
            session.clear()
            session["user_id"] = user.id
            flash(f"Signed in as {user.name}.")
            return redirect(url_for("main.dashboard"))
    return render_template("signin.html", error=error, email=email)


@bp.route("/signout", methods=["POST"])
def signout():
    # A POST form, not a link, so that a page elsewhere cannot sign you out
    # just by showing an image or link to this address.
    session.clear()
    flash("You have signed out.")
    return redirect(url_for("main.home"))
