from dataclasses import dataclass

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
    # photos: Image
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

# @dataclass
# class Photographer:
#     portpholio: str
#     bioDescription: str
#     services: Service
#     location: str
#     availability: str
#     rating: int

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
    rating: int = 0

#Need to check
@dataclass
class PhotographerService:
    id: str
    photographerId: str
    serviceId: str

#Need to check
@dataclass
class Portpholio:
    id: str
    photographerId: str

#Need to check
@dataclass
class Type:
    id: str
    type: str
    shortDescription: str
    price: float

#Need to check
@dataclass
class addOn:
    id: str 
    addOn: str
