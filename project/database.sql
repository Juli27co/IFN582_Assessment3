-- Drop and recreate the database
DROP DATABASE IF EXISTS sql12802431;
CREATE DATABASE sql12802431;
USE sql12802431;

CREATE TABLE Client
(
    client_id CHAR(4) PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    preferredPaymentMethod VARCHAR(50) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Service
(
    service_id CHAR(4) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    shortDescription VARCHAR(100) DEFAULT NULL,
    longDescription VARCHAR(255) DEFAULT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00
);

CREATE TABLE Photographer
(
    photographer_id CHAR(5) PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    bioDescription VARCHAR(255) DEFAULT NULL,
    location VARCHAR(50) DEFAULT NULL,
    availability ENUM('Weekends','Weekdays','Short notice bookings') DEFAULT 'Weekdays',
    rating DECIMAL(2,1) DEFAULT NULL
);

CREATE TABLE Portfolio
(
    portfolio_id CHAR(5) PRIMARY KEY,
    photographer_id CHAR(5) NOT NULL,
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

CREATE TABLE Type
(
    type_id CHAR(4) PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    shortDescription VARCHAR(100) DEFAULT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00
);

CREATE TABLE AddOn
(
    addOn_id CHAR(5) PRIMARY KEY,
    addOn VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00
);


CREATE TABLE Image
(
    image_id CHAR(6) PRIMARY KEY,
    imageSource VARCHAR(255) NOT NULL,
    image_description VARCHAR(255),
    service_id CHAR(4),
    portfolio_id CHAR(5),
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolio(portfolio_id)
);

CREATE TABLE Photographer_Service
(
    photographerService_id CHAR(9) PRIMARY KEY,
    photographer_id CHAR(5) NOT NULL,
    service_id CHAR(4) NOT NULL,
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id)
);

CREATE TABLE Cart
(
    cart_id CHAR(5) PRIMARY KEY,
    createdDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    client_id CHAR(4) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);

CREATE TABLE Cart_Service
(
    cartService_id CHAR(9) PRIMARY KEY,
    service_id CHAR(4) NOT NULL,
    cart_id CHAR(5) NOT NULL,
    type_id CHAR(4) NOT NULL,
    addOn_id CHAR(5) NOT NULL,
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (type_id) REFERENCES Type(type_id),
    FOREIGN KEY (addOn_id) REFERENCES AddOn(addOn_id)
);

CREATE TABLE Orders
(
    order_id CHAR(5) PRIMARY KEY,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    message VARCHAR(100) DEFAULT NULL,
    paymentMethod VARCHAR(50) NOT NULL,
    photographer_id CHAR(5) NOT NULL,
    client_id CHAR(4) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(client_id),
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

CREATE TABLE Order_Service
(
    orderService_id CHAR(9) PRIMARY KEY,
    service_id CHAR(4) NOT NULL,
    order_id CHAR(5) NOT NULL,
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

CREATE TABLE Inquiry
(
    inquiry_id CHAR(5) PRIMARY KEY,
    fullName VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telephone VARCHAR(15) NOT NULL,
    message VARCHAR(255) DEFAULT NULL,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP
);
