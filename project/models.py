from dataclasses import dataclass, field
from typing import List
from uuid import uuid4
from datetime import datetime
from enum import Enum
from flask_login import UserMixin


# for using in the form.available
class AvailabilityStatus(Enum):
    weekly_only = "Weekdays only"
    weekend_only = "Weekends only"
    short_notice_booking = "Short notice booking"

# @dataclass
# class User:
#     id: str
#     email: str
#     password: str
#     phone: str
#     firstName: str
#     lastName: str

@dataclass
class User(UserMixin):
    id: str
    email: str
    password: str
    firstName: str
    lastName: str
    phone: str = None
    role: str = None


@dataclass
class Image:
    image_id: str
    imageSource: str
    description: str
    serviceId: str
    portpholioId: str


@dataclass
class ServiceType:
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
class Service:
    service_id: str
    name: str
    shortDescription: str
    longDescription: str
    price: float

@dataclass
class Cart_Service:
    service: Service
    type: ServiceType
    addon: AddOn
    # generate unique identifier
    id: str = field(default_factory=lambda: str(uuid4))

@dataclass
class Cart:
    items: List[Cart_Service] = field(default_factory=lambda: [])

    def add_item(self, item: Cart_Service):
        self.items.append(item)


@dataclass
class Admin(User):
    pass

@dataclass
class Client(User):
    preferredPaymentMethod: str = None
    address: str = None

@dataclass
class Photographer(User):
    bioDescription: str = None
    location: str = None
    availability: str = None
    rating: float = 0.0

# @dataclass
# class Photographer:
#     photographer_id: str
#     email: str
#     password: str
#     phone: str
#     firstName: str
#     lastName: str
#     availability: AvailabilityStatus
#     bioDescription: str = ""
#     location: str = ""
#     rating: float = 0

@dataclass
class Portfolio:
    portfolio_id: str
    photographer_id: str
    images: list[Image]

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







