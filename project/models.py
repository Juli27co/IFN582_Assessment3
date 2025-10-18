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
class Image:
    id: str
    service_id: str
    photographer_id: str
    imageSource: str = "foobar"
    imageDescription: str = "foobar"
    


