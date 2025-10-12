from . import mysql
from .models import Client


def get_clients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Client")
    results = cur.fetchall()
    cur.close()
    return [
        Client(
            row["client_id"],
            row["email"],
            row["password"],
            row["phone"],
            row["firstName"],
            row["lastName"],
            row["preferredPaymentMethod"],
            row["address"],
        )
        for row in results
    ]
