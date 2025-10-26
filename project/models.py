from dataclasses import dataclass, field
from typing import List
from uuid import uuid4
from datetime import datetime


@dataclass
class Image:
    image_id: str
    imageSource: str
    description: str
    service_id: str
    photographer_id: str


@dataclass
class ServiceType:
    id: str
    name: str
    shortDescription: str
    price: float


@dataclass
class AddOn:
    id: str
    addOn: str
    price: float


@dataclass
class Service:
    id: str
    name: str
    shortDescription: str
    longDescription: str
    price: float = 0.00
    coverImage: str = "foobar"
    photographer_service_id: int = None

@dataclass
class User:
    role: str
    id: str
    email: str
    password: str
    phone: str
    firstName: str
    lastName: str

@dataclass
class Client(User):
    pass

@dataclass
class Photographer(User):
    bioDescription: str
    location: str
    availability: str
    rating: float
    profilePicture: str = "placeholder-image.png"


@dataclass
class Admin(User):
    pass

@dataclass
class Cart_Service:
    service: Service
    photographer: Photographer
    type: ServiceType
    addon: AddOn
    id: str = field(default_factory=lambda: str(uuid4()))
    subtotal: float = 0.00


@dataclass
class Cart:
    items: List[Cart_Service] = field(default_factory=lambda: [])

    def add_item(self, item: Cart_Service):
        self.items.append(item)

    def get_item(self, item_id: str):
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def remove_cart_item(self, item_id: str):
        self.items = [item for item in self.items if item.id != item_id]

    def total_cost(self):
        return sum( float(item.subtotal) for item in self.items)

@dataclass 
class Orders:
    id: str
    client_id: str
    address: str
    payment_method: str
    items: List[Cart_Service] = field(default_factory=list)


@dataclass
class OrderService:
    id: str
    order_id: str
    service_id: str
    type_id: str
    addOn_id: str 
    photographer_id: str
    subtotal: float = 0.00

@dataclass
class PhotographerService:
    id: str
    photographer_id: str
    service_id: str


@dataclass
class Inquiry:
    inquiry_id: int
    fullName: str
    email: str
    phone: str
    message: str
    createdDate: str