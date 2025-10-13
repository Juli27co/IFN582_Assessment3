DROP DATABASE IF EXISTS ifn582_assessment3;
CREATE DATABASE ifn582_assessment3;
USE ifn582_assessment3;


CREATE TABLE Service (
	serviceID CHAR(4) PRIMARY KEY,
    name VARCHAR(20), 
    shortDescription VARCHAR(50),
    longDescription VARCHAR(200)
);

CREATE TABLE Type (
	typeID CHAR(4) PRIMARY KEY,
    type VARCHAR(20),
    shortDescription VARCHAR(50),
    price FLOAT
);

CREATE TABLE AddOn(
	addOnID CHAR(5) PRIMARY KEY,
    addOn VARCHAR(20),
    price FLOAT
);

-- CREATE TABLE Cart(
-- 	cartID,
--     createdDate,
--     lastUpdated,
--     clientID
-- );

-- CREATE TABLE Cart_Service(
-- 	cartServiceID,
--     serviceID,
--     typeID,
--     addOnID,
--     cartID
-- );

CREATE TABLE Photographer(
	photographerID CHAR(5) PRIMARY KEY,
    email VARCHAR(50),
    password VARCHAR(20),
    telephone VARCHAR(20),
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    bioDescription VARCHAR(150),
    location VARCHAR(20),
    availability VARCHAR(50),
    rating FLOAT
);

CREATE TABLE Photographer_Service(
	photographerServiceID CHAR(9) PRIMARY KEY,
    photographerID CHAR(5),
    serviceID CHAR(4),
    FOREIGN KEY(photographerID) REFERENCES Photographer(photographerID),
    FOREIGN KEY(serviceID) REFERENCES Service(serviceID)
);

CREATE TABLE Portfolio(
	portfolioID CHAR(5) PRIMARY KEY,
    photographerID CHAR(5),
    FOREIGN KEY(photographerID) REFERENCES Photographer(photographerID)
);

CREATE TABLE Images(
	imageID CHAR(6) PRIMARY KEY,
    imageSource VARCHAR(100),
    imageDescription VARCHAR(50),
    serviceID CHAR(4),
    portfolioID CHAR(5),
    FOREIGN KEY(serviceID) REFERENCES Service(serviceID),
    FOREIGN KEY(serviceID) REFERENCES Service(serviceID)
);

-- CREATE TABLE Order(
-- 	orderID,
--     createdData,
--     lastUpdated,
--     message,
--     paymentMethod,
--     photographerID,
--     clientID,
--     addressID
-- );

-- CREATE TABLE Address(
-- 	addressID,
--     address1,
--     address2,
--     location,
--     state,
--     zip,
--     clientID
-- );

-- CREATE TABLE Client(
-- 	clientID,
--     email,
--     password,
--     telephone,
--     firstName,
--     lastName,
--     preferedPaymentMethod
-- );

-- CREATE TABLE Order_Service(
-- 	orderServiceID,
--     serviceID,
--     typeID,
--     addOnID,
--     orderID
-- );

CREATE TABLE Inquiry(
	inquiryID INT AUTO_INCREMENT PRIMARY KEY,
    fullName VARCHAR(40),
    email VARCHAR(50),
    telephone VARCHAR(20),
    message VARCHAR(200),
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
);

INSERT INTO Service (serviceID,name,shortDescription,longDescription
) VALUES 
	('S001','Pets','Capture your pet’s personality','A 30-60 minute photoshoot dedicated to your pet, featuring natural and playful poses, with professional editing of the best shots.'),
	('S002','Newborn','Adorable newborn photography','Safe and delicate session for newborns, with gentle poses and professional editing of high-quality photos.'),
	('S003','Product','Showcase your products professionally','Product photography session, ideal for catalogs or e-commerce, with professional lighting and image editing to highlight every detail.');

INSERT INTO Type (typeID,type,shortDescription,price
) VALUES 
    ('T001','Mini Session','30 min (5 edited photos)','80'),
    ('T002','Standard','60 min (10 edited photos)','150'),
    ('T003','Deluxe','90 min (20 edited photos + prints)','200');
    
INSERT INTO AddOn(addOnID,addOn,price
) VALUES 
    ('AO001', 'Extra props pack','50'),
    ('AO002', 'Printed album','100');

INSERT INTO Photographer(photographerID,email,password,telephone,firstName,lastName,bioDescription,location,availability,rating
) VALUES
    ('PH001','emily.smith@email.com','Pass123!','+61 412345678','Emily','Smith','Professional portrait and wedding photographer with 8 years of experience.','Brisbane','Weekdays only',4.8),
    ('PH002','james.lee@email.com','Lee2025#','+61 498765432','James','Lee','Specialized in product and commercial photography, delivering high-quality shots.','Sydney','Short notice bookings',4.6),
    ('PH003','sophia.jones@email.com','Sophia!99','+61 431234567','Sophia','Jones','Pet and family photographer passionate about capturing memories.','Brisbane','Weekends only',4.9);

INSERT INTO Photographer_Service(photographerServiceID,photographerID,serviceID
) VALUES
    ('PH001S001','PH001','S001'),
    ('PH001S002','PH001','S002'),
    ('PH002S002','PH002','S002');

INSERT INTO Portfolio(portfolioID,photographerID
) VALUES
    ('PR001','PH001'),
    ('PR002','PH002'),
    ('PR003','PH003');

INSERT INTO  Images(imageID,imageSource,imageDescription,serviceID,portfolioID
) VALUES
    ('IMG001','eric-ward-ISg37AI2A-s-unsplash.jpg','Golden Retriever playing in the park','S001','PR001'),
    ('IMG002','andrew-s-ouo1hbizWwo-unsplash.jpg','Golden Retriever playing in the park','S001','PR001'),
    ('IMG003','imani-bahati-LxVxPA1LOVM-unsplash.jpg','Golden Retriever playing in the park','S001','PR001'),
    ('IMG004','bonnie-kittle-MUcxe_wDurE-unsplash.jpg','Golden Retriever playing in the park','S001','PR001'),
    ('IMG005','jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden Retriever playing in the park','S001','PR001'),
    ('IMG006','karsten-winegeart-oU6KZTXhuvk-unsplash.jpg','Golden Retriever playing in the park','S001','PR001'),
    ('IMG007','hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Golden Retriever playing in the park','S002','PR001'),
    ('IMG008','pedro-de-sousa-BAVELu_vO-I-unsplash.jpg','Bride and groom at sunset','S001','PR002'),
    ('IMG009','janko-ferlic-EpbIXGCrtK0-unsplash.jpg','Bride and groom at sunset','S002','PR002'),
    ('IMG010','kelly-sikkema-WvVyudMd1Es-unsplash.jpg','Newborn baby sleeping peacefully','S002','PR002');


INSERT INTO Inquiry(fullName, email, telephone, message
) VALUES ("test","test","0000","test");