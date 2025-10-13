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
    price: float


# @dataclass
# class User:
#     id: str
#     email: str
#     password: str
#     telephone: str
#     firstName: str
#     lastName: str

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
