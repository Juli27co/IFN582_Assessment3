from . import mysql
from project.models import (
    Client,
    Service,
    Photographer,
    Portfolio,
    Image,
    Type,
    AddOn,
    PhotographerService,
    Inquiry,
    
)
from . import mysql


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


# To show item_detail page
def get_types():
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  type_id,
                type_name, 
                shortDescription,
                price
        FROM    Type
        """
    )
    results = cur.fetchall()
    cur.close()
    return [Type(row['type_id'],row['type_name'],row['shortDescription'],row['price']) for row in results]    

def get_single_type(typeId):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  type_id,
                type_name, 
                shortDescription,
                price
        FROM    Type
        WHERE   type_id = %s
        """,
        (typeId,),
    )
    row = cur.fetchone()
    cur.close()
    return Type(row['type_id'],row['type_name'],row['shortDescription'],row['price']) if row else None    

def get_addOns():
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  addOn_id,
                addOn, 
                price
        FROM    AddOn
        """
    )
    results = cur.fetchall()
    cur.close()
    return [AddOn(row["addOn_id"], row["addOn"], row["price"]) for row in results]

def get_single_addOn(addonId):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  addOn_id,
                addOn, 
                price
        FROM    AddOn
        WHERE   addOn_id = %s
        """, 
        (addonId,)
    )
    row = cur.fetchone()
    cur.close()
    return AddOn(row['addOn_id'],row['addOn'],row['price']) if row else None


def get_single_service(serviceId):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  service_id,
                name, 
                shortDescription,
                longDescription,
                price
        FROM    Service
        WHERE   service_id = %s
        """,
        (serviceId,),
    )
    row = cur.fetchone()
    cur.close()
    return (
        Service(
            row["service_id"],
            row["name"],
            row["shortDescription"],
            row["longDescription"],
            row["price"],
        )
        if row
        else None
    )


def get_photographer_service(photographer_service_id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  photographerService_id,
                photographer_id, 
                service_id
        FROM    Photographer_Service
        WHERE   photographerService_id = %s
        """,
        (photographer_service_id,),
    )
    row = cur.fetchone()
    cur.close()
    return (
        PhotographerService(
            row["photographerService_id"], row["photographer_id"], row["service_id"]
        )
        if row
        else None
    )


def get_portfolio_by_service(photographer_service):
    ph_id = photographer_service.photographerId
    ser_id = photographer_service.serviceId

    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  image_id,
                imageSource, 
                image_description,
                service_id,
                portfolio_id
        FROM    Image
        WHERE service_id = %s
        AND	portfolio_id IN (
            SELECT  portfolio_id
            FROM    Portfolio
            WHERE   photographer_id = %s
        )
        """,
        (ser_id, ph_id),
    )
    results = cur.fetchall()
    cur.close()
    return [
        Image(
            row["image_id"],
            row["imageSource"],
            row["image_description"],
            row["service_id"],
            row["portfolio_id"],
        )
        for row in results
    ]


# For form on item_detail page
def add_inquiry(form):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  inquiry_id
        FROM    Inquiry
        ORDER BY inquiry_id desc LIMIT 1
        """
    )
    row = cur.fetchone()

    if row :
        lastID = row['inquiry_id']
        newID = "IQ" + "%03d" % (int(lastID[2:]) + 1)
    else:
        newID = "IQ001"
    
    cur.execute(
        """
        INSERT INTO Inquiry (
            inquiry_id,
            fullName, 
            email, 
            telephone, 
            message
        ) VALUES (%s, %s, %s, %s, %s)
        """,
        (
            newID,
            form.fullName.data,
            form.email.data,
            form.phone.data,
            form.message.data,
        ),
    )
    mysql.connection.commit()
    cur.close()
