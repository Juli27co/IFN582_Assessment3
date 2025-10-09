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
    photos: Image[]
    type: str
    addOns: str
    price: float

@classdata
class User:
    id: str
    email: str
    password: str
    telephone: str
    firstName: str
    lastName: str
