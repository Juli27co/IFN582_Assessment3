from dataclasses import dataclass, field
from typing import List
from uuid import uuid4

@dataclass
class Image:
    id: str
    imageSource: str
    description: str
    serviceId: str
    portpholioId: str

@dataclass
class Service:
    id: str
    name: str
    shortDescription: str
    longDescription: str
    price: float

@dataclass
class Type:
    id: str
    type: str
    shortDescription: str
    price: float

@dataclass
class AddOn:
    id: str 
    addOn: str
    price: float

@dataclass
class Cart_Service:
    service: Service
    type: Type
    addon: AddOn
    # generate unique identifier
    id: str = field(default_factory=lambda: str(uuid4))

@dataclass
class Cart:
    items: List[Cart_Service] = field(default_factory=lambda: [])

    def add_item(self, item: Cart_Service):
        self.items.append(item)

@dataclass
class Address:
    address1: str
    address2: str
    location: str
    state: str
    zip: str

@dataclass
class Client:
    preferedPaymentMethod: str
    address: Address

@dataclass
class Photographer:
    id: str 
    email:str
    password:str
    telephone: str
    firstName:str
    lastName:str
    bioDescription: str
    location: str
    availability: str
    rating: float

@dataclass
class PhotographerService:
    id: str
    photographerId: str
    serviceId: str

@dataclass
class Portpholio:
    id: str
    photographerId: str
