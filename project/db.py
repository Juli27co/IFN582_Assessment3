from project.models import Client, Service, Photographer, PhotographerService, Portpholio, Image, Type, AddOn
from . import mysql


#To show item_detail page
def get_types():
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  typeID,
                type, 
                shortDescription,
                price
        FROM    Type
        """
    )
    results = cur.fetchall()
    cur.close()
    return [Type(row['typeID'],row['type'],row['shortDescription'],row['price']) for row in results]    

def get_single_type(type_id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  typeID,
                type, 
                shortDescription,
                price
        FROM    Type
        WHERE   typeID = %s
        """, 
        (type_id,)
    )
    row = cur.fetchone()
    cur.close()
    return Type(row['typeID'],row['type'],row['shortDescription'],row['price']) if row else None    

def get_addOns():
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  addOnID,
                addOn, 
                price
        FROM    AddOn
        """
    )
    results = cur.fetchall()
    cur.close()
    return [AddOn(row['addOnID'],row['addOn'],row['price']) for row in results]    


def get_single_service(service_id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  serviceID,
                name, 
                shortDescription,
                longDescription
        FROM    Service
        WHERE   serviceID = %s
        """,
        (service_id,)
    )
    row = cur.fetchone()
    cur.close()
    return Service(row['serviceID'],row['name'],row['shortDescription'],row['longDescription']) if row else None   


def get_photographer_service(photographer_service_id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  photographerServiceID,
                photographerID, 
                serviceID
        FROM    Photographer_Service
        WHERE   photographerServiceID = %s
        """,
        (photographer_service_id,)
    )
    row = cur.fetchone()
    cur.close()
    return PhotographerService(row['photographerServiceID'],row['photographerID'],row['serviceID']) if row else None   


def get_portfolio_by_service(photographer_service):
    ph_id = photographer_service.photographerId
    ser_id = photographer_service.serviceId

    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT  imageID,
                imageSource, 
                imageDescription,
                serviceID,
                portfolioID
        FROM    Images
        WHERE serviceID = %s
        AND	portfolioID IN (
            SELECT  portfolioID
            FROM    Portfolio
            WHERE   photographerID = %s
        )
        """,
        (ser_id, ph_id)
    )
    results = cur.fetchall()
    cur.close()
    return [Image(row['imageID'],row['imageSource'],row['imageDescription'],row['serviceID'],row['portfolioID']) for row in results] 


#For form on item_detail page
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
        )
    )
    mysql.connection.commit()
    cur.close()