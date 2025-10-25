from flask import session, redirect, flash, url_for
from functools import wraps


def only_photographers(func):
    """Decorator to check if the user is a photographer or admin."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session or session["user"]["id"] == 0:
            flash("Please log in before moving on.", "error")
            return redirect(url_for("main.login"))
        # Allow photographers and admins
        if session["user"]["role"] not in ["photographer", "admin"]:
            flash("You do not have permission to view this page.", "error")
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)

    return wrapper


def only_admins(func):
    """Decorator to check if the user is an admin."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session or session["user"]["id"] == 0:
            flash("Please log in before moving on.", "error")
            return redirect(url_for("main.login"))
        # Only allow admins
        if session["user"]["role"] != "admin":
            flash("You do not have permission to view this page.", "error")
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)

    return wrapper


def photographer_private(func):
    """Decorator to ensure photographers can only access their own data."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session or session["user"]["id"] == 0:
            flash("Please log in before moving on.", "error")
            return redirect(url_for("main.login"))
        
        if session["user"]["role"] != "admin":
            photographer_id = kwargs.get("photographer_id")
            if photographer_id is None or int(photographer_id) != session["user"]["id"]:
                flash("You do not have permission to view this page.", "error")
                return redirect(url_for("main.index"))
        return func(*args, **kwargs)

    return wrapper
