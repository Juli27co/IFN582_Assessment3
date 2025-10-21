from project.db import get_single_service, get_single_type, get_single_addOn, get_photographer
from project.models import Cart, Cart_Service, Orders
from flask import session


def add_to_cart(serviceId, pho_id, typeId, addOnId, subtotal):
    # get current session data
    cart = get_cart()
    # create a new data (append a new item to the list in the cart)
    cart.add_item(
        Cart_Service(
            service = get_single_service(serviceId),
            photographer = get_photographer(pho_id),
            type = get_single_type(typeId),
            addon = get_single_addOn(addOnId),
            subtotal = subtotal
        )
    )
    # store the updated data back into session
    _save_cart_to_session(cart)

def remove_cart_item(cart_item_id):
    # get current session data
    cart = get_cart()
    # create a new list of items that do not match the specific id
    cart.remove_cart_item(cart_item_id)
    # store the updated data back into session
    _save_cart_to_session(cart)

def get_cart():
    # get current session data (when it doesn't exist: None)
    cart_data = session.get("cart")
    cart = Cart()
    if isinstance(cart_data, dict):
        for item in cart_data.get("items", []):
            # Search each items from DB 
            serviceInCurrentSession = get_single_service(item["service"]["id"])
            photographerInCurrentSession = get_photographer(item["photographer"]["id"])
            typeInCurrentSession = get_single_type(item["type"]["id"])
            addonInCurrentSession = get_single_addOn(item["addon"]["id"])
            subtotal = item["subtotal"]
            # Add the results into cart item
            if serviceInCurrentSession and photographerInCurrentSession:
                cart.add_item(Cart_Service(
                    id = str(item["id"]),
                    service = serviceInCurrentSession,
                    photographer = photographerInCurrentSession,
                    type = typeInCurrentSession,
                    addon = addonInCurrentSession,
                    subtotal = subtotal                    
                ))
    return cart

def convert_cartItem_to_order(client_id, address, payment_method,cart):
    return Orders(
        id=None,
        client_id=client_id,
        address=address,
        payment_method=payment_method,
        items=cart.items
    )

def _save_cart_to_session(cart):
    session["cart"] = {
        "items" : [
            {
                "id": item.id,
                "service": {
                    "id": item.service.id
                },
                "photographer": {
                    "id": item.photographer.id
                },
                "type": {
                    "id": item.type.id
                },
                "addon": {
                    "id": (item.addon.id) if item.addon else None
                },
                "subtotal": item.subtotal
            } for item in cart.items
        ]
    }

def empty_cart():
    session["cart"] = {
        "items": []
    }
