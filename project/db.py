from . import mysql
from .models import Service
from typing import  List, Tuple, Dict


def get_photographer_by_email(email: str):
    cur = mysql.connection.cursor()  
    try:
        cur.execute("""
            SELECT photographer_id, email, password 
            FROM Photographer 
            WHERE email=%s
        """,(email,))
        row = cur.fetchone()  
        if not row:
            return None
        photographer_id, email_, password_ = row
        return {"id": photographer_id, "email": email_, "password": password_}
    finally:
        cur.close()

def get_client_by_email(email: str):
    cur = mysql.connection.cursor()
    try:
        cur.execute("""
            SELECT client_id, email, password 
            FROM Client 
            WHERE email=%s
        """,(email,))
        row = cur.fetchone()
        if not row:
            return None
        client_id, email_, password_ = row
        return {"id": client_id, "email": email_, "password": password_}
    finally:
        cur.close()

def get_admin_by_email(email: str):
    cur = mysql.connection.cursor()
    try:
        cur.execute("""
            SELECT admin_id, email, password 
            FROM Admin 
            WHERE email=%s
        """,(email,))
        row = cur.fetchone()
        if not row:
            return None
        admin_id, email_, password_ = row
        return {"id": admin_id, "email": email_, "password": password_}
    finally:
        cur.close()

def get_photographer(photographer_id: int):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT photographer_id, email, password, phone, firstName, lastName,
               bioDescription, location, availability, rating, profilePicture
        FROM Photographer
        WHERE photographer_id = %s
    """, (photographer_id,))
    row = cur.fetchone()
    cur.close()
    return row

def add_or_update_photographer(form, photographer_id=None, image_filename=None):
    cur = mysql.connection.cursor()
    if photographer_id:
        if image_filename:
            cur.execute("""
                UPDATE Photographer
                SET email=%s, phone=%s, firstName=%s, lastName=%s,
                    bioDescription=%s, location=%s, availability=%s, rating=%s,
                    profilePicture=%s
                WHERE photographer_id=%s
            """, (
                form.email.data, form.phone.data,
                form.firstName.data, form.lastName.data, form.bioDescription.data,
                form.location.data, form.availability.data, form.rating.data or 0.0,
                image_filename, photographer_id
            ))
        else:
            cur.execute("""
                UPDATE Photographer
                SET email=%s, phone=%s, firstName=%s, lastName=%s,
                    bioDescription=%s, location=%s, availability=%s, rating=%s
                WHERE photographer_id=%s
            """, (
                form.email.data, form.phone.data,
                form.firstName.data, form.lastName.data, form.bioDescription.data,
                form.location.data, form.availability.data, form.rating.data or 0.0,
                photographer_id
            ))
    else:
        cur.execute("""
            INSERT INTO Photographer
                (email, phone, firstName, lastName,
                 bioDescription, location, availability, rating, profilePicture)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            form.email.data, form.phone.data,
            form.firstName.data, form.lastName.data, form.bioDescription.data,
            form.location.data, form.availability.data, form.rating.data or 0.0,
            image_filename
        ))
        photographer_id = cur.lastrowid

    mysql.connection.commit()
    cur.close()
    return photographer_id

def get_all_services():
    cur = mysql.connection.cursor()
    cur.execute("SELECT service_id AS id, name AS name FROM Service ORDER BY name")
    rows = cur.fetchall()
    cur.close()
    services = []
    for r in rows:
        services.append({"id": (r["id"] if isinstance(r, dict) else r[0]),
                         "name": (r["name"] if isinstance(r, dict) else r[1])})
    return services

def insert_image(service_id: int, photographer_id: int, image_relative_path: str, image_description: str) -> int:
    cur = mysql.connection.cursor()
    try:
        cur.execute("""
            INSERT INTO Image (imageSource, image_description, service_id, photographer_id)
            VALUES (%s, %s, %s, %s)
        """, (image_relative_path, image_description, service_id, photographer_id))
        mysql.connection.commit()
        return cur.lastrowid
    finally:
        cur.close()


def ensure_photographer_service(photographer_id: int, service_id: int) -> None:
    cur = mysql.connection.cursor()
    try:
        cur.execute("""
            SELECT photographerService_id
            FROM Photographer_Service
            WHERE photographer_id=%s AND service_id=%s
        """, (photographer_id, service_id))
        row = cur.fetchone()
        if not row:
            cur.execute("""
                INSERT INTO Photographer_Service (photographer_id, service_id)
                VALUES (%s, %s)
            """, (photographer_id, service_id))
            mysql.connection.commit()
    finally:
        cur.close()


def get_images_for_photographer(photographer_id: int):
    cur = mysql.connection.cursor()
    try:
        cur.execute("""
            SELECT image_id, imageSource, image_description, service_id, photographer_id
            FROM Image
            WHERE photographer_id=%s
            ORDER BY image_id DESC
        """, (photographer_id,))
        rows = cur.fetchall()
        if rows and isinstance(rows[0], dict):
            return rows   
        cols = [c[0] for c in cur.description]
        return [dict(zip(cols, r)) for r in rows]
    finally:
        cur.close()

def delete_image_row(image_id: int, photographer_id: int) -> int:
    cur = mysql.connection.cursor()
    try:
        cur.execute("""
            DELETE FROM Image
            WHERE image_id=%s AND photographer_id=%s
        """, (image_id, photographer_id))
        mysql.connection.commit()
        return cur.rowcount
    finally:
        cur.close()