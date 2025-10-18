from flask import session, redirect, flash, url_for
from functools import wraps


def only_clients(func):
    """Decorator to check if the user is a client or admin."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session or session["user"]["id"] == 0:
            flash("Please log in before moving on.", "error")
            return redirect(url_for("main.login"))
        # Allow clients and admins
        if session["user"]["role"] not in ["client", "admin"]:
            flash("You do not have permission to view this page.", "error")
            return redirect(url_for("main.index"))
        return func(*args, **kwargs)

    return wrapper


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
