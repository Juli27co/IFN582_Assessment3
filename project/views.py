from flask import Blueprint, render_template, request, session, flash
from .db import get_clients
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    clients = get_clients()
    print(clients)
    return render_template('index.html', title = 'Home Page')