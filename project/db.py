from project.models import Photographer, Image, Service
from . import mysql


def get_photographer(photographer_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT photographer_id, email, password, phone, firstName, lastName,
               bioDescription, location, availability, rating, profilePicture
        FROM Photographer
        WHERE photographer_id = %s
    """, (photographer_id,))
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
        row["profilePicture"] or "placeholder-image.png"
    )


def get_images_for_photographer(photographer_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT image_id, imageSource, image_description, service_id, photographer_id
        FROM Image
        WHERE photographer_id = %s
    """, (photographer_id,))
    results = cur.fetchall()
    cur.close()

    return [
        Image(
            str(row["image_id"]),
            row["imageSource"],
            row["image_description"],
            str(row["service_id"]),
            str(row["photographer_id"])
        )
        for row in results
    ]



def get_services_for_photographer(photographer_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT
            ps.photographerService_id AS photographer_service_id,  -- << สำคัญ
            s.service_id, s.name, s.shortDescription, s.longDescription, s.price
        FROM Photographer_Service ps
        JOIN Service s ON s.service_id = ps.service_id
        WHERE ps.photographer_id = %s
    """, (photographer_id,))
    rows = cur.fetchall()
    cur.close()

    services = []
    for row in rows:
        s = Service(
            row['service_id'],
            row['name'],
            row['shortDescription'],
            row['longDescription'],
            float(row['price'])
        )
        
        s.photographer_service_id = row['photographer_service_id']
        services.append(s)
    return services

def insert_order_detail(client_id, address, payment_method):
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Orders (client_id, address, payment_method)
        VALUES (%s, %s, %s)
    """, (client_id, address, payment_method))
    mysql.connection.commit()
    cur.close()


