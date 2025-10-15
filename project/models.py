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