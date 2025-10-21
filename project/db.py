from . import mysql
from .models import Service
from MySQLdb.cursors import DictCursor


def get_photographer_management(photographer_id: int):
    cur = mysql.connection.cursor(DictCursor)
    cur.execute(
        """
        SELECT photographer_id, email, password, phone, firstName, lastName,
               bioDescription, location, availability, rating, profilePicture
        FROM Photographer
        WHERE photographer_id = %s
    """,
        (photographer_id,),
    )
    row = cur.fetchone()
    cur.close()
    return row


def add_or_update_photographer(form, photographer_id=None, image_filename=None):
    cur = mysql.connection.cursor()
    if photographer_id:
        params = [
            form.email.data,
            form.phone.data,
            form.firstName.data,
            form.lastName.data,
            form.bioDescription.data,
            form.location.data,
            form.availability.data,
            (form.rating.data or 0.0),
        ]

        set_cols = """
            email=%s, phone=%s, firstName=%s, lastName=%s,
            bioDescription=%s, location=%s, availability=%s, rating=%s
        """
        if getattr(form, "password", None) and (form.password.data or ""):
            set_cols += ", password=%s"
            params.append(form.password.data)

        if image_filename:
            set_cols += ", profilePicture=%s"
            params.append(image_filename)

        params.append(photographer_id)

        cur.execute(
            f"UPDATE Photographer SET {set_cols} WHERE photographer_id=%s", params
        )
    else:
        cur.execute(
            """
            INSERT INTO Photographer
                (email, password, phone, firstName, lastName,
                 bioDescription, location, availability, rating, profilePicture)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
            (
                form.email.data,
                (getattr(form, "password", None) and form.password.data) or "",
                form.phone.data,
                form.firstName.data,
                form.lastName.data,
                form.bioDescription.data,
                form.location.data,
                form.availability.data,
                form.rating.data or 0.0,
                image_filename,
            ),
        )
        photographer_id = cur.lastrowid

    mysql.connection.commit()
    cur.close()
    return photographer_id


def get_all_services():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT service_id AS id, name AS name FROM Service ORDER BY name")
    rows = cur.fetchall()
    cur.close()
    services = []
    for r in rows or []:
        services.append({"id": r["id"], "name": r["name"]})
    return services


def insert_image(
    service_id: int,
    photographer_id: int,
    image_relative_path: str,
    image_description: str,
) -> int:
    cur = mysql.connection.cursor()
    try:
        cur.execute(
            """
            INSERT INTO Image (imageSource, image_description, service_id, photographer_id)
            VALUES (%s, %s, %s, %s)
        """,
            (image_relative_path, image_description, service_id, photographer_id),
        )
        mysql.connection.commit()
        return cur.lastrowid
    finally:
        cur.close()


def ensure_photographer_service(photographer_id: int, service_id: int) -> None:
    cur = mysql.connection.cursor(DictCursor)
    try:
        cur.execute(
            """
            SELECT photographerService_id
            FROM Photographer_Service
            WHERE photographer_id=%s AND service_id=%s
        """,
            (photographer_id, service_id),
        )
        row = cur.fetchone()
        if not row:
            cur.execute(
                """
                INSERT INTO Photographer_Service (photographer_id, service_id)
                VALUES (%s, %s)
            """,
                (photographer_id, service_id),
            )
            mysql.connection.commit()
    finally:
        cur.close()


def get_images_for_photographer(photographer_id: int):
    cur = mysql.connection.cursor(DictCursor)
    try:
        cur.execute(
            """
            SELECT image_id, imageSource, image_description, service_id, photographer_id
            FROM Image
            WHERE photographer_id=%s
            ORDER BY image_id DESC
        """,
            (photographer_id,),
        )
        rows = cur.fetchall() or []
        return rows
    finally:
        cur.close()


def delete_image_row(image_id: int, photographer_id: int) -> int:
    cur = mysql.connection.cursor()
    try:
        cur.execute(
            """
            DELETE FROM Image
            WHERE image_id=%s AND photographer_id=%s
        """,
            (image_id, photographer_id),
        )
        mysql.connection.commit()
        return cur.rowcount
    finally:
        cur.close()


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
    Admin,
)
from . import mysql


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
    cur = mysql.connection.cursor(DictCursor)

    # Base query - use JOIN if filtering by service_type
    if filters.get("service_type"):
        query = """
            SELECT DISTINCT p.photographer_id, p.email, p.password, p.phone, p.firstName, p.lastName, 
                   p.bioDescription, p.location, p.availability, p.rating, p.profilePicture
            FROM Photographer p
            INNER JOIN Photographer_Service ps ON p.photographer_id = ps.photographer_id
            INNER JOIN Service s ON ps.service_id = s.service_id
            WHERE s.service_id = %s
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

    if filters.get("min_rating"):
        if "WHERE" in query and "s.name" in query:
            query += " AND p.rating >= %s"
        else:
            query += " AND rating >= %s"
        params.append(filters["min_rating"])

    if filters.get("search"):
        if "WHERE" in query and "s.name" in query:
            query += " AND (p.firstName LIKE %s OR p.lastName LIKE %s)"
        else:
            query += " AND (firstName LIKE %s OR lastName LIKE %s)"
        search_term = f"%{filters['search']}%"
        params.extend([search_term, search_term])

    print(f"Executing query: {query}")
    print(f"With params: {params}")

    cur.execute(query, params)
    results = cur.fetchall()
    cur.close()

    print(f"Found {len(results)} photographers")

    return [
        Photographer(
            role="photographer",
            id=str(row["photographer_id"]),
            email=row["email"],
            password=row["password"],
            phone=row["phone"],
            firstName=row["firstName"],
            lastName=row["lastName"],
            bioDescription=row.get("bioDescription") or "",
            location=row.get("location") or "",
            availability=row.get("availability") or "",
            rating=float(row.get("rating") or 0.0),
            profilePicture=(row.get("profilePicture") or None),
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


def check_for_client(email, password):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT client_id, password, email, firstName, lastName, phone, preferredPaymentMethod
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
    rows = cur.fetchall()
    cur.close()
    return [
        ServiceType(
            id=row["type_id"],
            name=row["type_name"],
            shortDescription=row["shortDescription"],
            price=float(row["price"]),
        )
        for row in rows
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
            row["type_id"], row["type_name"], row["shortDescription"], row["price"]
        )
        if row
        else None
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
        (addonId,),
    )
    row = cur.fetchone()
    cur.close()
    return AddOn(row["addOn_id"], row["addOn"], row["price"]) if row else None


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
            row["coverImage"],
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
            INSERT INTO Client (email, password, firstName, lastName, phone, preferredPaymentMethod)
            VALUES (%s, %s, %s, %s, %s, %s)
        """,
            (
                form.email.data,
                hashedPassword,
                form.firstName.data,
                form.lastName.data,
                form.phone.data,
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


def get_photographer(photographer_id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT photographer_id, email, password, phone, firstName, lastName,
               bioDescription, location, availability, rating, profilePicture
        FROM Photographer
        WHERE photographer_id = %s
    """,
        (photographer_id,),
    )
    row = cur.fetchone()
    cur.close()

    if not row:
        return None

    return Photographer(
        "photographer",
        str(row["photographer_id"]),
        row["email"],
        row["password"],
        row["phone"],
        row["firstName"],
        row["lastName"],
        row["bioDescription"],
        row["location"],
        row["availability"],
        float(row["rating"] or 0.0),
        row["profilePicture"] or "placeholder-image.png",
    )


def get_images_for_photographer(photographer_id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT image_id, imageSource, image_description, service_id, photographer_id
        FROM Image
        WHERE photographer_id = %s
    """,
        (photographer_id,),
    )
    results = cur.fetchall()
    cur.close()

    return [
        Image(
            str(row["image_id"]),
            row["imageSource"],
            row["image_description"],
            str(row["service_id"]),
            str(row["photographer_id"]),
        )
        for row in results
    ]


def get_services_for_photographer(photographer_id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT
            ps.photographerService_id AS photographer_service_id,
            s.service_id, s.name, s.shortDescription, s.longDescription, s.price
        FROM Photographer_Service ps
        JOIN Service s ON s.service_id = ps.service_id
        WHERE ps.photographer_id = %s
    """,
        (photographer_id,),
    )
    rows = cur.fetchall()
    cur.close()

    return [
        Service(
            id=row["service_id"],
            name=row["name"],
            shortDescription=row["shortDescription"],
            longDescription=row["longDescription"],
            price=float(row["price"]),
            coverImage=row.get("coverImage", "foobar"),
            photographer_service_id=row["photographer_service_id"],
        )
        for row in rows
    ]


def admin_insert_service(name, short_desc, long_desc, price, cover_image=None):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        INSERT INTO Service (name, shortDescription, longDescription, price, coverImage)
        VALUES (%s, %s, %s, %s, %s)
    """,
        (name, short_desc, long_desc, price, cover_image),
    )
    mysql.connection.commit()
    cur.close()


def admin_add_type(name, short_desc, price):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        INSERT INTO ServiceType (type_name, shortDescription, price)
        VALUES (%s, %s, %s)
    """,
        (name, short_desc, price),
    )
    mysql.connection.commit()
    cur.close()


def admin_add_addon(name, price):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        INSERT INTO Addon (AddOn, price)
        VALUES (%s, %s)
    """,
        (name, price),
    )
    mysql.connection.commit()
    cur.close()


def admin_delete_service(service_id: int):
    cur = mysql.connection.cursor()
    try:
        cur.execute("DELETE FROM Service WHERE service_id=%s", (service_id,))
        mysql.connection.commit()
        return cur.rowcount
    finally:
        cur.close()


def admin_delete_type(type_id: int):
    cur = mysql.connection.cursor()
    try:
        cur.execute("DELETE FROM ServiceType WHERE type_id=%s", (type_id,))
        mysql.connection.commit()
        return cur.rowcount
    finally:
        cur.close()


def admin_delete_addon(addon_id: int):
    cur = mysql.connection.cursor()
    try:
        cur.execute("DELETE FROM AddOn WHERE addOn_id=%s", (addon_id,))
        mysql.connection.commit()
        return cur.rowcount
    finally:
        cur.close()

# def insert_order_detail(client_id, address, payment_method):
#     cur = mysql.connection.cursor()
#     cur.execute("""
#         INSERT INTO Orders (client_id, address, payment_method)
#         VALUES (%s, %s, %s)
#     """, (client_id, address, payment_method))
#     mysql.connection.commit()
#     cur.close()

def insert_order_detail(order):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Orders (client_id, address, payment_method)
        VALUES (%s, %s, %s)
    """, (order.client_id, order.address, order.payment_method))
    order_id = cur.lastrowid

    for item in order.items:
        cur.execute("""
        INSERT INTO Order_Service (order_id, service_id, type_id, addOn_id, photographer_id, subtotal)
        VALUES (%s, %s, %s, %s, %s, %s)
    """,(order_id, item.service.id, item.type.id, item.addOn.id, item.photographer.id, item.subtotal))
    
    mysql.connection.commit()
    cur.close()
