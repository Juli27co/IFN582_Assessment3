from hashlib import sha256
from . import mysql
from project.models import (
    Admin,
    Client,
    Service,
    Photographer,
    Image,
    ServiceType,
    AddOn,
    PhotographerService,
    Inquiry,
    Admin
)
from . import mysql

# def getCurrentUser(user_id):
#     client = getSingleClient(user_id) 
#     vendor = getSingleVendor(user_id)
#     admin = getSingleAdmin(user_id)
    
#     if client: 
#         return client
#     elif vendor:
#         return vendor
#     elif admin:
#         return admin
#     else:
#         return None

# def checkLoginUser(email, password):
#     client = authenticateClient(email, password) 
#     vendor = authenticateVendor(email, password)
#     admin = authenticateAdmin(email, password)
    
#     if client: 
#         return client
#     elif vendor:
#         return vendor
#     elif admin:
#         return admin
#     else:
#         return None


# def authenticateClient(email, password):
#     cur = mysql.connection.cursor()
#     cur.execute(
#         """
#         SELECT client_id, email, password, firstName, lastName
#         FROM Client
#         WHERE email = %s AND password = %s
#         """,
#         (email, password),
#     )
#     row = cur.fetchone()
#     cur.close()
#     return (
#         Client(
#             id = row['client_id'],
#             email = row['email'],
#             password = row['password'],
#             firstName = row['firstName'],
#             lastName = row['lastName'],
#             role = "client"
#         )
#     ) if row else None

# def authenticateVendor(email, password):
#     cur = mysql.connection.cursor()
#     cur.execute(
#         """
#         SELECT photographer_id, email, password, firstName, lastName
#         FROM Photographer
#         WHERE email = %s AND password = %s
#         """,
#         (email, password),
#     )
#     row = cur.fetchone()
#     cur.close()
#     return (
#         Photographer(
#             id = row['photographer_id'],
#             email = row['email'],
#             password = row['password'],
#             firstName = row['firstName'],
#             lastName = row['lastName'],
#             role = "vendor"
#         )
#     ) if row else None

# def authenticateAdmin(email, password):
#     cur = mysql.connection.cursor()
#     cur.execute(
#         """
#         SELECT admin_id, email, password, firstName, lastName
#         FROM Admin
#         WHERE email = %s AND password = %s
#         """,
#         (email, password),
#     )
#     row = cur.fetchone()
#     cur.close()
#     return (
#         Admin(
#             id = row['admin_id'],
#             email = row['email'],
#             password = row['password'],
#             firstName = row['firstName'],
#             lastName = row['lastName'],
#             role = "admin"
#         )
#     ) if row else None

# def getSingleClient(user_id):
#     cur = mysql.connection.cursor()
#     cur.execute(
#         """
#         SELECT client_id, email, password, firstName, lastName
#         FROM Client
#         WHERE client_id = %s
#         """,
#         (user_id),
#     )
#     row = cur.fetchone()
#     cur.close()
#     return (
#         Client(
#             id = row['client_id'],
#             email = row['email'],
#             password = row['password'],
#             firstName = row['firstName'],
#             lastName = row['lastName'],
#             role = "client"
#         )
#     ) if row else None

# def getSingleVendor(user_id):
#     cur = mysql.connection.cursor()
#     cur.execute(
#         """
#         SELECT photographer_id, email, password, firstName, lastName
#         FROM Photographer
#         WHERE photographer_id = %s
#         """,
#         (user_id),
#     )
#     row = cur.fetchone()
#     cur.close()
#     return (
#         Photographer(
#             id = row['photographer_id'],
#             email = row['email'],
#             password = row['password'],
#             firstName = row['firstName'],
#             lastName = row['lastName'],
#             role = "vendor"
#         )
#     ) if row else None

# def getSingleAdmin(user_id):
#     cur = mysql.connection.cursor()
#     cur.execute(
#         """
#         SELECT admin_id, email, password, firstName, lastName
#         FROM Admin
#         WHERE admin_id = %s
#         """,
#         (user_id),
#     )
#     row = cur.fetchone()
#     cur.close()
#     return (
#         Admin(
#             id = row['admin_id'],
#             email = row['email'],
#             password = row['password'],
#             firstName = row['firstName'],
#             lastName = row['lastName'],
#             role = "admin"
#         )
#     ) if row else None


def get_clients():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Client")
    results = cur.fetchall()
    cur.close()
    return [
        Client(
            "client",
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


def get_photographers(filters):
    cur = mysql.connection.cursor()

    # Base query - use JOIN if filtering by service_type
    if filters.get("service_type"):
        query = """
            SELECT DISTINCT p.photographer_id, p.email, p.password, p.phone, p.firstName, p.lastName, 
                   p.bioDescription, p.location, p.availability, p.rating, p.profilePicture
            FROM Photographer p
            INNER JOIN Photographer_Service ps ON p.photographer_id = ps.photographer_id
            INNER JOIN Service s ON ps.service_id = s.service_id
            WHERE s.name = %s
        """
        params = [filters["service_type"]]
    else:
        query = "SELECT * FROM Photographer WHERE 1=1"
        params = []

    # Add location filter
    if filters.get("location"):
        if "WHERE" in query and "s.name" in query:
            query += " AND p.location = %s"
        else:
            query += " AND location = %s"
        params.append(filters["location"])

    # Add availability filter
    if filters.get("availability"):
        if "WHERE" in query and "s.name" in query:
            query += " AND p.availability = %s"
        else:
            query += " AND availability = %s"
        params.append(filters["availability"])

    print(f"Executing query: {query}")
    print(f"With params: {params}")

    cur.execute(query, params)
    results = cur.fetchall()
    cur.close()

    print(f"Found {len(results)} photographers")

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
            row["profilePicture"],
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

# def check_for_user(username, password):
#     cur = mysql.connection.cursor()
#     cur.execute(
#         """
#         SELECT client_id, password, email, firstName, lastName, phone
#         FROM Client
#         WHERE email = %s AND password = %s
#         """,
#         (username, password),
#     )
#     row = cur.fetchone()
#     cur.close()
#     if row:
#         return UserAccount(
#             row["username"],
#             row["user_password"],
#             row["email"],
#             UserInfo(
#                 str(row["user_id"]),
#                 row["firstname"],
#                 row["surname"],
#                 row["email"],
#                 row["phone"],
#             ),
#         )
#     return None

def check_for_client(email, password):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT client_id, password, email, firstName, lastName, phone
        FROM Client
        WHERE email = %s AND password = %s
    """,
        (email, password),
    )
    row = cur.fetchone()
    cur.close()
    if row:
        return Client(
            "client",
            row["client_id"],
            row["email"],
            row["password"],
            row["phone"],
            row["firstName"],
            row["lastName"],
            "",
            "",
        )
    return None


def check_for_photographer(email, password):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT photographer_id, password, email, firstName, lastName, phone, bioDescription, location, availability, rating, profilePicture
        FROM Photographer
        WHERE email = %s AND password = %s
    """,
        (email, password),
    )
    row = cur.fetchone()
    cur.close()
    if row:
        return Photographer(
            "photographer",
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
            row["profilePicture"],
        )
    return None


def check_for_admin(email, password):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT admin_id, password, email, firstName, lastName, phone
        FROM Admin
        WHERE email = %s AND password = %s
    """,
        (email, password),
    )
    row = cur.fetchone()
    cur.close()
    if row:
        return Admin(
            "admin",
            row["admin_id"],
            row["email"],
            row["password"],
            row["phone"],
            row["firstName"],
            row["lastName"],
        )
    return None


# To show item_detail page
def get_types():
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  type_id,
                type_name, 
                shortDescription,
                price
        FROM    ServiceType
        """
    )
    results = cur.fetchall()
    cur.close()
    return [
        ServiceType(
            row['type_id'],
            row['type_name'],
            row['shortDescription'],
            row['price']
        )
        for row in results
    ]    

def get_single_type(typeId):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  type_id,
                type_name, 
                shortDescription,
                price
        FROM    ServiceType
        WHERE   type_id = %s
        """,
        (typeId,),
    )
    row = cur.fetchone()
    cur.close()
    return (
        ServiceType(
            row['type_id'],
            row['type_name'],
            row['shortDescription'],
            row['price']
        ) 
        if row else None
    )    

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
    return [
        AddOn(
            row["addOn_id"],
            row["addOn"], 
            row["price"]
        )
        for row in results
    ]


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
        (addonId,),
    )
    row = cur.fetchone()
    cur.close()
    return (
        AddOn(
            row['addOn_id'],
            row['addOn'],
            row['price']
        ) 
        if row else None
    )


def get_single_service(serviceId):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  service_id,
                name, 
                shortDescription,
                longDescription,
                price,
                coverImage
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
            row["coverImage"]
        )
        if row else None
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
            row["photographerService_id"],
            row["photographer_id"], 
            row["service_id"]
        )
        if row else None
    )


def get_images_by_photographer_service(photographer_service):
    ph_id = photographer_service.photographer_id
    ser_id = photographer_service.service_id

    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  image_id,
                imageSource, 
                image_description,
                service_id,
                photographer_id
        FROM    Image
        WHERE   service_id = %s
        AND     photographer_id = %s
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
            row["photographer_id"],
        )
        for row in results
    ]


# for form on item_detail page
def add_inquiry(form):
    cur = mysql.connection.cursor()
    
    cur.execute(
        """
        INSERT INTO Inquiry (
            fullName, 
            email, 
            telephone, 
            message
        ) VALUES (%s, %s, %s, %s)
        """,
        (
            form.fullName.data,
            form.email.data,
            form.phone.data,
            form.message.data,
        ),
    )
    mysql.connection.commit()
    cur.close()


def add_user(form):
    cur = mysql.connection.cursor()

    hashedPassword = sha256(form.password.data.encode()).hexdigest()

    if form.user_type.data == "client":
        cur.execute(
            """
            INSERT INTO Client (email, password, firstName, lastName, phone, preferredPaymentMethod, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
            (
                form.email.data,
                hashedPassword,
                form.firstName.data,
                form.lastName.data,
                form.phone.data,
                "",
                "",
            ),
        )
    elif form.user_type.data == "photographer":
        cur.execute(
            """
            INSERT INTO Photographer (email, password, firstName, lastName, phone, bioDescription, location, availability, rating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            (
                form.email.data,
                hashedPassword,
                form.firstName.data,
                form.lastName.data,
                form.phone.data,
                "",
                "",
                "",
                0,
            ),
        )
    mysql.connection.commit()
    cur.close()
