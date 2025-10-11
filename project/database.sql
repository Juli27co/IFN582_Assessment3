-- Drop and recreate the database
DROP DATABASE IF EXISTS fotobookingdb;
CREATE DATABASE fotobookingdb;
USE fotobookingdb;

CREATE TABLE Services (
  serviceID       VARCHAR(10) PRIMARY KEY,
  serviceName     VARCHAR(100) NOT NULL,
  shortDescription VARCHAR(150),
  longDescription  TEXT NOT NULL
);

CREATE TABLE Photographers (
  photographerID   VARCHAR(10) PRIMARY KEY,
  email            VARCHAR(100) NOT NULL,
  password         VARCHAR(255) NOT NULL,
  telephone        VARCHAR(20),
  firstName        VARCHAR(100) NOT NULL,
  lastName         VARCHAR(100) NOT NULL,
  bioDescription   TEXT,
  location         VARCHAR(100) NOT NULL,
  availabilityStatus ENUM('Weekdays only','Weekends only','Short notice booking') NOT NULL DEFAULT 'Weekdays only',
  rating           DECIMAL(10,2)
);

CREATE TABLE Portfolios (
  portfolioID     VARCHAR(10) PRIMARY KEY,
  photographerID  VARCHAR(10) NOT NULL,
  FOREIGN KEY (photographerID) REFERENCES Photographers(photographerID) ON DELETE CASCADE
);

CREATE TABLE Images (
  imageID          VARCHAR(10) PRIMARY KEY,
  imageSource      VARCHAR(255) NOT NULL,
  imageDescription VARCHAR(150) NOT NULL,
  serviceID        VARCHAR(10),
  portfolioID      VARCHAR(10),
  FOREIGN KEY (serviceID)   REFERENCES Services(serviceID)     ON DELETE CASCADE,
  FOREIGN KEY (portfolioID) REFERENCES Portfolios(portfolioID) ON DELETE CASCADE
);

CREATE TABLE PhotographerServices (
  photographerServiceID VARCHAR(10) PRIMARY KEY,
  photographerID        VARCHAR(10) NOT NULL,
  serviceID             VARCHAR(10) NOT NULL,
  FOREIGN KEY (photographerID) REFERENCES Photographers(photographerID) ON DELETE CASCADE,
  FOREIGN KEY (serviceID)      REFERENCES Services(serviceID)            ON DELETE CASCADE
);

-- Services
INSERT INTO Services (ServiceID, ServiceName, shortDescription, longDescription) VALUES
('S001', 'Pets', 'Capture your pet''s personality', 'A 30-60 minute photoshoot dedicated to your pet, featuring natural and playful poses, with professional editing of the best shots.'),
('S002', 'Wedding', 'Complete coverage of your wedding', 'Full day wedding photography, including preparations, ceremony, and celebration, with edited digital photos and optional printed album.'),
('S003', 'Newborn', 'Adorable newborn photography', 'Safe and delicate session for newborns, with gentle poses and professional editing of high-quality photos.'),
('S004', 'Product', 'Showcase your products professionally', 'Product photography session, ideal for catalogues or e-commerce, with professional lighting and image editing to highlight every detail.');

-- Photographers
INSERT INTO Photographers
(photographerID, email, password, telephone, firstName, lastName, bioDescription, location, availabilityStatus, rating) VALUES
('PH001', 'emily.smith@email.com', 'Pass123!', '+61 412345678', 'Emily', 'Smith',
 'Professional portrait and wedding photographer with 8 years of experience.', 'Brisbane', 'Weekdays only', 4.8),
('PH002', 'james.lee@email.com', 'Lee2025#', '+61 498765432', 'James', 'Lee',
 'Specialized in product and commercial photography, delivering high-quality shots.', 'Sydney', 'Short notice booking', 4.6),
('PH003', 'sophia.jones@email.com', 'Sophia!99', '+61 431234567', 'Sophia', 'Jones',
 'Pet and family photographer passionate about capturing memories.', 'Brisbane', 'Weekends only', 4.9),
('PH004', 'liam.tan@email.com', 'LiamTan$21', '+61 499876543', 'Liam', 'Tan',
 'Wedding and event photographer with a creative approach to storytelling.', 'Sydney', 'Short notice booking', 4.7),
('PH005', 'olivia.brown@email.com', 'OliveB#45', '+61 412398765', 'Olivia', 'Brown',
 'Newborn and maternity photographer focusing on safe and artistic sessions.', 'Sydney', 'Short notice booking', 4.7);

-- Portfolios
INSERT INTO Portfolios (portfolioID, photographerID) VALUES
('PR001', 'PH001'),
('PR002', 'PH002'),
('PR003', 'PH003'),
('PR004', 'PH004'),
('PR005', 'PH005');

-- PhotographerServices  
INSERT INTO PhotographerServices (photographerServiceID, photographerID, serviceID) VALUES
('PH001S001', 'PH001', 'S001'), 
('PH002S002', 'PH002', 'S002'),  
('PH003S003', 'PH003', 'S003'),  
('PH004S004', 'PH004', 'S004'),  
('PH005S003', 'PH005', 'S003');  

-- Images
INSERT INTO Images (imageID, imageSource, imageDescription, serviceID, portfolioID) VALUES
('IMG001', 'eric-ward-Is9s37A2A-s-unsplash.jpg', 'A man cuddling a dog', 'S001', 'PR001'),
('IMG002', 'chris-cxoEfkNwUaA-unsplash.jpg', 'A photographer capturing a bride and groom at their wedding', 'S002', 'PR001'),
('IMG003', 'garrett-jackson-o0nJWBMlb5A-unsplash.jpg','A newborn baby peacefully sleeping', 'S003', 'PR001'),
('IMG004', 'imani-bahati-LxVxPAlLOWM-unsplash.jpg', 'A sneaker styled for a product photoshoot', 'S004', 'PR001'),
('IMG005', 'kelly-sikkema-VI06bb1aB9Y-unsplash.jpg','A man gently holding his newborn baby', 'S003', 'PR001');
