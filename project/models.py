from dataclasses import dataclass
from enum import Enum
from flask_login import UserMixin

from dataclasses import dataclass

@dataclass 
class Client:
    id: str
    email: str
    password: str
    phone: str
    firstName: str
    lastName: str
    preferredPaymentMethod: str
    address: str

@dataclass
class Service:
    id: str
    name: str
    shortDescription: str
    longDescription: str
    price: float = 0.00
    coverImage: str = "foobar"

@dataclass
class Photographer:
    id: str
    email: str
    password: str
    phone: str
    firstName: str
    lastName: str
    bioDescription: str 
    location: str
    availability: str 
    rating: float = 0.0
    profilePicture: str = "foobar"

@dataclass
class Photographer_Service:
    photographerService_id: str
    photographer_id: str
    service_id: str
    
@dataclass
class Image:
    id: str
    service_id: str
    photographer_id: str
    imageSource: str = "foobar"
    imageDescription: str = "foobar"

class User(UserMixin):
    def __init__(self, id, email, role, photographer_id=None):
        self.id = str(id)
        self.email = email
        self.role = role
        self.photographer_id = photographer_id