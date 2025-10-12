from dataclasses import dataclass
from enum import Enum


@dataclass
class Image:
    id: str
    imageSource: str
    imageDescription: str


@dataclass
class Service:
    id: str
    name: str
    shortDescription: str
    longDescription: str
    photos: Image[]
    type: str
    addOns: str
    price: float

@dataclass
class User:
    id: str
    email: str
    password: str
    telephone: str
    firstName: str
    lastName: str

@dataclass
class AvailabilityStatus(Enum):
    WEEKDAYS_ONLY = "Weekdays only"
    WEEKENDS_ONLL = "Weekends only"
    SHORT_NOTICE_BOOKING = "Short notice booking"

@dataclass
class Photographer:
    id: str
    email: str
    password: str
    telephone: str
    firstName: str
    lastName: str
    bioDescription: str 
    location: str
    availability: AvailabilityStatus
    rating: float

@dataclass
class Portfolio:
    id: str
    photographer: Photographer

