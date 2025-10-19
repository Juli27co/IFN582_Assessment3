from project.db import get_single_service, get_single_type, get_single_addOn
from project.models import Cart, Cart_Service
from flask import session


def add_to_cart(serviceId, typeId, addOnId):
    # get current session data
    cart = get_cart()
    # create a new data (append a new item to the list in the cart)
    cart.add_item(
        Cart_Service(
            service = get_single_service(serviceId),
            type = get_single_type(typeId),
            addon = get_single_addOn(addOnId)
        )
    )
    # store the updated data back into session
    _save_cart_to_session(cart)

def get_cart():
    # get current session data (when it doesn't exist: None)
    cart_data = session.get("cart")
    cart = Cart()
    if isinstance(cart_data, dict):
        for item in cart_data.get("items", []):
            # Search each items from DB 
            serviceSearched = get_single_service(item["service"]["id"])
            typeSearched = get_single_type(item["type"]["id"])
            addonSearched = get_single_addOn(item["addon"]["id"])
            # Add the results into cart item
            if serviceSearched and typeSearched and addonSearched:
                cart.add_item(Cart_Service(
                    id = str(item["id"]),
                    service = serviceSearched,
                    type = typeSearched,
                    addon = addonSearched
                ))
    return cart

def _save_cart_to_session(cart):
    session["cart"] = {
        "items" : [
            {
                "id": item.id,
                "service": {
                    "id": item.service.service_id
                },
                "type": {
                    "id": item.type.id
                }
                ,
                "addon": {
                    "id": (item.addon.id) if item.addon else None
                }
            } for item in cart.items
        ]
    }