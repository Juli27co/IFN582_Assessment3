from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


@dataclass
class Image:
    image_id: str
    imageSource: str
    image_description: str = ""
    service_id: str = ""
    portfolio_id: str = ""


# for using in the form.available
class AvailabilityStatus(Enum):
    weekly_only = "Weekdays only"
    weekend_only = "Weekends only"
    short_notice_booking = "Short notice booking"


@dataclass
class Photographer:
    Photographer_id: str
    email: str
    password: str
    phone: str
    firstName: str
    lastName: str
    availability: AvailabilityStatus
    bioDescription: str = ""
    location: str = ""
    rating: float = 0


@dataclass
class Service:
    service_id: str
    name: str
    shortDescription: str
    longDescription: str
    photos: list[Image]
    price: float


@dataclass
class Portfolio:
    portfolio_id: str
    photographer_id: str


@dataclass
class User:
    id: str
    email: str
    password: str
    phone: str
    firstName: str
    lastName: str


@dataclass
class Client(User):
    preferredPaymentMethod: str
    address: str


@dataclass
class Photographer(User):
    bioDescription: str
    location: str
    availability: str
    rating: float


@dataclass
class Inquiry:
    inquiry_id: int
    fullName: str
    email: str
    phone: str
    message: str
    createdDate: str


@dataclass
class Portfolio:
    portfolio_id: int
    photographer_id: str
    imageSource: str
    imageDescription: str
