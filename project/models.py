from dataclasses import dataclass, field
from datetime import datetime   
from enum import Enum

# this class is about customer information, which does not related to my path. however, someone may use this class.
@dataclass
class Address:
    id: str
    address1: str
    address2: str
    location: str
    state: str
    zip: str

# for using in the form.available

class AvailabilityStatus(Enum):
    weekly_only = "Weekdays only"
    weekend_only = "Weekends only"
    short_notice_booking = "Short notice booking"

# for using in the service type

class ServiceType(Enum):
    new_born = "New Born"
    weddings = "Weddings"
    pets = "Pets"
    products = "Products"


@dataclass
class Photographer:
    Photographer_id: str
    email: str
    password: str
    phone: str
    firstName: str
    lastName: str
    bioDescription: str = ''
    location: str = ''
    availability: AvailabilityStatus
    rating: float = 0


@dataclass
class Service:
    service_id: str
    name: str
    shortDescription: str
    longDescription: str
    price: float
    type: ServiceType

@dataclass
class Portfolio:
    portfolio_id: str
    photographer_id: str

@dataclass
class Image:
    image_id: str
    imageSource: str
    image_description: str = ''
    service_id: str =''
    portfolio_id: str = ''


