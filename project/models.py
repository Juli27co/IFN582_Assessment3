from dataclasses import dataclass

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
    photos: list[Image]
    type: str
    addOns: str
    price: float

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
    

