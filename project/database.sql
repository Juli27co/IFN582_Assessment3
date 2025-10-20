-- Drop and recreate the database
DROP DATABASE IF EXISTS sql12802431;
CREATE DATABASE sql12802431;
USE sql12802431;

CREATE TABLE Admin
(
	admin_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Client
(
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    preferredPaymentMethod VARCHAR(50) NOT NULL
);

CREATE TABLE Service
(
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    shortDescription VARCHAR(100) NULL,
    longDescription VARCHAR(255) NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    coverImage VARCHAR(255) NULL
);

CREATE TABLE Photographer
(
    photographer_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    bioDescription VARCHAR(255) NULL,
    location VARCHAR(50) NOT NULL,
    availability VARCHAR(50) NULL DEFAULT 'Not set',
    rating DECIMAL(2,1) NULL DEFAULT 0.0,
    profilePicture VARCHAR(255) NULL
);

CREATE TABLE ServiceType
(
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) NOT NULL,
    shortDescription VARCHAR(100) NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00
);

CREATE TABLE AddOn
(
    addOn_id INT AUTO_INCREMENT PRIMARY KEY,
    addOn VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00
);


CREATE TABLE Image
(
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    imageSource VARCHAR(255) NOT NULL,
    image_description VARCHAR(255),
    service_id INT,
    photographer_id INT,
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

CREATE TABLE Photographer_Service
(
    photographerService_id INT AUTO_INCREMENT PRIMARY KEY,
    photographer_id INT,
    service_id INT,
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id)
);

CREATE TABLE Cart
(
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    createdDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);

CREATE TABLE Cart_Service
(
    cartService_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT,
    cart_id INT,
    type_id INT,
    addOn_id INT,
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (type_id) REFERENCES ServiceType(type_id),
    FOREIGN KEY (addOn_id) REFERENCES AddOn(addOn_id)
);

CREATE TABLE Orders
(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    client_id INT,
    address VARCHAR(255) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);


CREATE TABLE Order_Service
(
    orderService_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    service_id INT,
    type_id INT,
    addOn_id INT, 
    photographer_id INT,
    subtotal DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
	FOREIGN KEY (type_id) REFERENCES ServiceType(type_id),
    FOREIGN KEY (addOn_id) REFERENCES AddOn(addOn_id),
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

CREATE TABLE Payment
(
	payment_id INT AUTO_INCREMENT PRIMARY KEY,
	order_id INT,
    payment_method VARCHAR(50) NOT NULL,
    payment_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    payment_status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);


CREATE TABLE Inquiry
(
    inquiry_id INT AUTO_INCREMENT PRIMARY KEY,
    fullName VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telephone VARCHAR(15) NOT NULL,
    message VARCHAR(255) NULL,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Admin (email, password, phone, firstName, lastName, lastUpdated) VALUES
('admin1@gmail.com', 'ef51306214d9a6361ee1d5b452e6d2bb70dc7ebb85bf9e02c3d4747fb57d6bec', '0490557292', '', '', '2024-10-16 13:25:00'),
('admin2@gmail.com', 'ef51306214d9a6361ee1d5b452e6d2bb70dc7ebb85bf9e02c3d4747fb57d6bec', '0490557292', '', '', '2024-10-19 11:40:00');

INSERT INTO Client (email, password, phone, firstName, lastName, preferredPaymentMethod) VALUES
('julicortesarb@gmail.com', '1234qwer', '0490557292', 'Juliana', 'Cortes', 'Credit Card'),
('mike.hansen88@yahoo.com', 'passM!ke88', '0451234567', 'Michael', 'Hansen', 'PayPal'),
('sara_lee12@gmail.com', 'saraLeePwd', '0478901234', 'Sara', 'Lee', 'Debit Card'),
('tom.jenkins@outlook.com', 'jenkinsT90', '0498765432', 'Tom', 'Jenkins', 'Bank Transfer'),
('diana.ross@mail.com', 'rossDiana21', '0487654321', 'Diana', 'Ross', 'Credit Card'),
('lucas_ng@live.com', 'lucasNg@2023', '0477123456', 'Lucas', 'Ng', 'Cash'),
('emilybrown123@gmail.com', 'emBrown!45', '0466123456', 'Emily', 'Brown', 'Credit Card'),
('omar.youssef@gmail.com', 'Omar2024$', '0433556677', 'Omar', 'Youssef', 'Debit Card'),
('natalie_woods@hotmail.com', 'natWoods99', '0499776655', 'Natalie', 'Woods', 'PayPal'),
('leo.fernandez@mail.com', 'FernLeo#10', '0422446688', 'Leo', 'Fernandez', 'Credit Card');

INSERT INTO Service (name, shortDescription, longDescription, price, coverImage) VALUES
('Wedding Photography', 'Capture your special day with beautiful wedding photography.', 'Our wedding photography service includes a full day of coverage, from the ceremony to the reception, ensuring every precious moment is captured.', 2000.00, 'drew-coffman-llWjwo200fo-unsplash.jpg'),
('Pets Photography', 'Professional portrait sessions for pets.', 'Our pets photography sessions are perfect for capturing timeless images of your furry friends in a relaxed setting.', 300.00, 'jamie-street-s9Tf1eBDFqw-unsplash.jpg'),
('Newborn Photography', 'Capture the precious moments of your newborn with professional photography services.', 'We specialize in newborn photography, offering a gentle and personalized experience to preserve the earliest moments of your baby’s life.', 1500.00, 'janko-ferlic-EpbIXGCrtK0-unsplash.jpg'),
('Product Photography', 'High-quality product photography to showcase your items.', 'Our product photography service is designed to highlight the features and details of your products, ideal for e-commerce and marketing materials.', 500.00, 'pmv-chamara-CeQiQxNNdUM-unsplash.jpg');

INSERT INTO ServiceType (type_name, shortDescription, price) VALUES
('Mini Session', 'Basic session with 5 edited photos.', 0.00),
('Standard Session', 'Extend session with 10 edited photos and a photo book.', 50.00),
('Deluxe Session', 'Deluxe session with all edited photos, a photo book, and a canvas print.', 100.00);

INSERT INTO AddOn (addOn, price) VALUES
('Extra Edited Photos', 50.00),
('Printed Album', 100.00),
('Both : Extra Edited Photos + Printed Album', 150.00);

INSERT INTO Photographer (email, password, phone, firstName, lastName, bioDescription, location, availability, rating, profilePicture) VALUES
('john.doe@example.com', 'securePassword123', '0412345678', 'John', 'Doe', 'Experienced photographer specializing in portrait and event photography.', 'Sydney', 'Weekdays', 4.8, ''),
('emily.smith@example.com', 'pass1234secure', '0498765432', 'Emily', 'Smith', 'Specializing in landscape photography with a keen eye for natural light and outdoor scenes.', 'Melbourne', 'Weekdays', 4.7, 'jakob-owens-DQPP9rVLYGQ-unsplash.jpg'),
('michael.jones@example.com', 'mikephoto321', '0401122334', 'Michael', 'Jones', 'Freelance photographer with a focus on corporate headshots and commercial photography.', 'Brisbane', 'Short notice bookings', 4.9, 'home-page-welcome.jpg'),
('sophia.wilson@example.com', 'sophiaW!23', '0455667788', 'Sophia', 'Wilson', 'Creative portrait photographer with over 10 years of experience capturing moments that tell stories.', 'Perth', 'Weekends', 5.0, 'andre-furtado-JtV6zyOZSrA-unsplash.jpg'),
('david.brown@example.com', 'davidsPhoto2023', '0422333445', 'David', 'Brown', 'Experienced in wedding and engagement photography, known for capturing genuine emotions and timeless moments.', 'Adelaide', 'Weekends', 4.6, 'home-page-welcome.jpg'),
('olivia.miller@example.com', 'OliviaM123!', '0433556677', 'Olivia', 'Miller', 'Family and newborn photographer dedicated to capturing the purest moments of life with warmth and elegance.', 'Gold Coast', 'Weekdays', 4.9, 'janko-ferlic-EpbIXGCrtK0-unsplash.jpg'),
('benjamin.taylor@example.com', 'photoBen5678', '0466778899', 'Benjamin', 'Taylor', 'Fashion and editorial photographer with a passion for capturing the latest trends and unique styles.', 'Sydney', 'Weekdays', 4.8, 'jakob-owens-f3s0i96CRGQ-unsplash.jpg'),
('ava.anderson@example.com', 'Ava2023secure', '0477889900', 'Ava', 'Anderson', 'Specializes in event photography and commercial shoots, ensuring high-quality results for every project.', 'Melbourne', 'Weekends', 4.7, 'daniel-korpai-hbTKIbuMmBI-unsplash.jpg'),
('liam.thomas@example.com', 'LiamPhoto987', '0488992233', 'Liam', 'Thomas', 'Travel and adventure photographer who captures breathtaking landscapes and remote destinations.', 'Hobart', 'Weekdays', 4.9, 'andre-furtado-JtV6zyOZSrA-unsplash.jpg'),
('chloe.davis@example.com', 'Chloe2023!Pass', '0412349876', 'Chloe', 'Davis', 'Wedding and portrait photographer with a passion for capturing candid moments and emotional stories.', 'Canberra', 'Short notice bookings', 4.8, 'garrett-jackson-oOnJWBMlb5A-unsplash.jpg');

INSERT INTO Photographer_Service (photographer_id, service_id) VALUES
(1,1),
(1,2),
(1,3),
(1,4),
(5,1),
(6,3),
(7,4),
(8,2),
(9,2),
(10,1);


INSERT INTO Cart (createdDate, lastUpdated, client_id) VALUES
('2025-01-01 09:30:00','2025-01-01 09:30:00',1),
('2025-01-03 11:45:00','2025-01-03 11:45:00',2),
('2025-01-04 14:10:00','2025-01-04 14:10:00',3),
('2025-01-06 10:25:00','2025-01-06 10:25:00',4),
('2025-01-08 16:40:00','2025-01-08 16:40:00',5),
('2025-01-10 09:50:00','2025-01-10 09:50:00',6),
('2025-01-12 13:05:00','2025-01-12 13:05:00',7),
('2025-01-14 08:20:00','2025-01-14 08:20:00',8), 
('2025-01-16 18:35:00','2025-01-16 18:35:00',9), 
('2025-01-18 11:10:00','2025-01-18 11:10:00',10);


INSERT INTO Image (imageSource, image_description, service_id, photographer_id) VALUES
('chris-CxoEeNkJwUA-unsplash.jpg','Bride and groom during ceremony',1, 1),
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 1),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 1),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 1),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 1),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 1),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 1),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 1),
('imani-bahati-LxVxPA1LOVM-unsplash.jpg','Stylish shoes for sale',4, 1);


INSERT INTO Cart_Service (service_id, cart_id, type_id, addOn_id) VALUES
(1,1,2,1),
(4,1,1,2),
(2,2,1,1),
(3,3,3,2),
(1,4,2,1),
(2,4,1,2),
(4,5,2,1),
(3,6,1,1),
(1,7,3,2),
(2,8,2,1),
(4,9,1,2),
(3,10,2,1);

INSERT INTO Orders (createdDate, lastUpdated, client_id, address) VALUES
('2025-01-05 10:15:00', '2025-01-05 10:15:00', 1, '22 Street Av, Parramatta NSW 2150'),
('2025-01-08 14:30:00', '2025-01-08 14:30:00', 2, '12 Maple Drive, Carlton VIC 3053'),
('2025-01-12 09:45:00', '2025-01-12 10:00:00', 3, '450 Ocean Blvd, Surfers Paradise QLD 4217'),
('2025-01-15 13:20:00', '2025-01-15 13:20:00', 4, '99 Elm Street, Adelaide SA 5000'),
('2025-01-17 16:05:00', '2025-01-17 16:30:00', 5, '102 Pine Ave, Fremantle WA 6160'),
('2025-01-20 11:50:00', '2025-01-20 12:00:00', 6, '78 Sunset Road, Hobart TAS 7000'),
('2025-01-22 08:10:00', '2025-01-22 08:10:00', 7, '66 Birch Lane, Canberra ACT 2601'),
('2025-01-24 15:25:00', '2025-01-24 15:40:00', 1, '120 King Street, Brisbane QLD 4000'),
('2025-01-26 10:05:00', '2025-01-26 10:10:00', 2, '33 Riverbank Rd, Geelong VIC 3220'),
('2025-01-28 18:45:00', '2025-01-28 19:00:00', 3, '88 Queen Ave, Newcastle NSW 2300');

INSERT INTO Order_Service (order_id, service_id, type_id, addOn_id, photographer_id, subtotal) VALUES
(1, 1, 2, 2, 1, 2150.00),
(2, 2, 1, 1, 2, 350.00),
(3, 3, 3, 3, 3, 1750.00),
(4, 4, 2, NULL, 4, 550.00),
(5, 1, 3, 3, 2, 2250.00),
(6, 2, 2, 2, 1, 450.00),
(7, 4, 1, 1, 5, 550.00),
(8, 3, 2, NULL, 3, 1550.00),
(9, 1, 1, NULL, 4, 2000.00),
(10, 2, 3, 3, 5, 550.00);

INSERT INTO Payment (order_id, payment_method, payment_date, total_price, payment_status) VALUES
(1, 'Credit Card', '2025-01-06 12:30:00', 2150.00, 'Confirmed'),
(2, 'Cash', '2025-01-09 15:00:00', 350.00, 'Confirmed'),
(3, 'Credit Card', '2025-01-13 11:20:00', 1750.00, 'Pending'),
(4, 'Credit Card', '2025-01-16 09:45:00', 550.00, 'Confirmed'),
(5, 'Cash', '2025-01-18 14:10:00', 2250.00, 'Cancelled'),
(6, 'Credit Card', '2025-01-19 16:30:00', 450.00, 'Confirmed'),
(7, 'Cash', '2025-01-20 10:15:00', 550.00, 'Pending'),
(8, 'Credit Card', '2025-01-21 12:40:00', 1550.00, 'Confirmed'),
(9, 'Cash', '2025-01-23 17:00:00', 2000.00, 'Confirmed'),
(10, 'Credit Card', '2025-01-25 18:25:00', 550.00, 'Pending');



    
 
