from . import mysql
from .models import Client, Photographer, Service, Inquiry, Portfolio


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


def get_photographers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Photographer")
    results = cur.fetchall()
    cur.close()
    return [
        Photographer(
            row["photographer_id"],
            row["email"],
            row["password"],
            row["phone"],
            row["firstName"],
            row["lastName"],
            row["bioDescription"],
            row["location"],
            row["availability"],
            row["rating"],
        )
        for row in results
    ]


def get_services():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Service")
    results = cur.fetchall()
    cur.close()
    return [
        Service(
            row["service_id"],
            row["name"],
            row["shortDescription"],
            row["longDescription"],
            row["price"],
        )
        for row in results
    ]


def get_portfolio():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Portfolio, Images")
    results = cur.fetchall()
    cur.close()
    return [
        Portfolio(
            row["portfolio_id"],
            row["photographer_id"],
            row["imageSource"],
            row["imageDescription"],
        )
        for row in results
    ]


def get_inquiries():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Inquiry")
    results = cur.fetchall()
    cur.close()
    return [
        Inquiry(
            row["inquiry_id"],
            row["fullName"],
            row["email"],
            row["phone"],
            row["message"],
            row["createdDate"],
        )
        for row in results
    ]


def add_inquiry(inquiry: Inquiry):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO Inquiry (fullName, email, phone, message) VALUES (%s, %s, %s, %s)",
        (inquiry.fullName, inquiry.email, inquiry.phone, inquiry.message),
    )
    mysql.connection.commit()
    cur.close()


def check_for_user(username, password):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT client_id, password, email, firstName, lastName, phone
        FROM Client
        WHERE email = %s AND password = %s
    """,
        (username, password),
    )
    row = cur.fetchone()
    cur.close()
    if row:
        return UserAccount(
            row["username"],
            row["user_password"],
            row["email"],
            UserInfo(
                str(row["user_id"]),
                row["firstname"],
                row["surname"],
                row["email"],
                row["phone"],
            ),
        )
    return None


def is_admin(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admins WHERE user_id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    return True if row else False


def add_user(form):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        INSERT INTO users (username, user_password, email, firstname, surname, phone)
        VALUES (%s, %s, %s, %s, %s, %s)
    """,
        (
            form.username.data,
            form.password.data,
            form.email.data,
            form.firstname.data,
            form.surname.data,
            form.phone.data,
        ),
    )
    mysql.connection.commit()
    cur.close()
