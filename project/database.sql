-- Drop and recreate the database
DROP DATABASE IF EXISTS sql12802431;
CREATE DATABASE sql12802431;
USE sql12802431;

CREATE TABLE ADMIN
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
    preferredPaymentMethod VARCHAR(50) NOT NULL,
    address VARCHAR(255) NOT NULL
);

CREATE TABLE Service
(
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
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
    message VARCHAR(100) NULL,
    paymentMethod VARCHAR(50) NOT NULL,
    photographer_id INT,
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES Client(client_id),
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

CREATE TABLE Order_Service
(
    orderService_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT,
    order_id INT,
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
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
('admin1@gmail.com', '1234qwer', '0490557292', '', '', '2024-10-16 13:25:00'),
('admin2@gmail.com', '1234qwer', '0490557292', '', '', '2024-10-19 11:40:00');

INSERT INTO Client (email, password, phone, firstName, lastName, preferredPaymentMethod, address) VALUES
('julicortesarb@gmail.com', '1234qwer', '0490557292', 'Juliana', 'Cortes', 'Credit Card', '22 Street Av'),
('mike.hansen88@yahoo.com', 'passM!ke88', '0451234567', 'Michael', 'Hansen', 'PayPal', '12 Maple Drive'),
('sara_lee12@gmail.com', 'saraLeePwd', '0478901234', 'Sara', 'Lee', 'Debit Card', '450 Ocean Blvd'),
('tom.jenkins@outlook.com', 'jenkinsT90', '0498765432', 'Tom', 'Jenkins', 'Bank Transfer', '99 Elm Street'),
('diana.ross@mail.com', 'rossDiana21', '0487654321', 'Diana', 'Ross', 'Credit Card', '102 Pine Ave'),
('lucas_ng@live.com', 'lucasNg@2023', '0477123456', 'Lucas', 'Ng', 'Cash', '78 Sunset Road'),
('emilybrown123@gmail.com', 'emBrown!45', '0466123456', 'Emily', 'Brown', 'Credit Card', '66 Birch Lane'),
('omar.youssef@gmail.com', 'Omar2024$', '0433556677', 'Omar', 'Youssef', 'Debit Card', '120 King Street'),
('natalie_woods@hotmail.com', 'natWoods99', '0499776655', 'Natalie', 'Woods', 'PayPal', '33 Riverbank Rd'),
('leo.fernandez@mail.com', 'FernLeo#10', '0422446688', 'Leo', 'Fernandez', 'Credit Card', '88 Queen Ave');

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
('michael.jones@example.com', 'mikephoto321', '0401122334', 'Michael', 'Jones', 'Freelance photographer with a focus on corporate headshots and commercial photography.', 'Brisbane', 'Short notice bookings', 4.9, 'home-page-welcome'),
('sophia.wilson@example.com', 'sophiaW!23', '0455667788', 'Sophia', 'Wilson', 'Creative portrait photographer with over 10 years of experience capturing moments that tell stories.', 'Perth', 'Weekends', 5.0, 'andre-furtado-JtV6zyOZSrA-unsplash'),
('david.brown@example.com', 'davidsPhoto2023', '0422333445', 'David', 'Brown', 'Experienced in wedding and engagement photography, known for capturing genuine emotions and timeless moments.', 'Adelaide', 'Weekends', 4.6, 'home-page-welcome'),
('olivia.miller@example.com', 'OliviaM123!', '0433556677', 'Olivia', 'Miller', 'Family and newborn photographer dedicated to capturing the purest moments of life with warmth and elegance.', 'Gold Coast', 'Weekdays', 4.9, ''),
('benjamin.taylor@example.com', 'photoBen5678', '0466778899', 'Benjamin', 'Taylor', 'Fashion and editorial photographer with a passion for capturing the latest trends and unique styles.', 'Sydney', 'Weekdays', 4.8, ''),
('ava.anderson@example.com', 'Ava2023secure', '0477889900', 'Ava', 'Anderson', 'Specializes in event photography and commercial shoots, ensuring high-quality results for every project.', 'Melbourne', 'Weekends', 4.7, ''),
('liam.thomas@example.com', 'LiamPhoto987', '0488992233', 'Liam', 'Thomas', 'Travel and adventure photographer who captures breathtaking landscapes and remote destinations.', 'Hobart', 'Weekdays', 4.9, ''),
('chloe.davis@example.com', 'Chloe2023!Pass', '0412349876', 'Chloe', 'Davis', 'Wedding and portrait photographer with a passion for capturing candid moments and emotional stories.', 'Canberra', 'Short notice bookings', 4.8, '');

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
('2024-10-01 10:00:00','2024-10-01 10:00:00',1),
('2024-10-02 14:15:00','2024-10-02 14:15:00',2),
('2024-10-03 09:30:00','2024-10-03 09:30:00',3),
('2024-10-04 17:45:00','2024-10-04 17:45:00',4),
('2024-10-05 12:00:00','2024-10-05 12:00:00',5),
('2024-10-06 08:30:00','2024-10-06 08:30:00',6),
('2024-10-07 11:00:00','2024-10-07 11:00:00',7),
('2024-10-08 13:25:00','2024-10-08 13:25:00',8),
('2024-10-09 15:10:00','2024-10-09 15:10:00',9),
('2024-10-10 16:50:00','2024-10-10 16:50:00',10);


INSERT INTO Image (imageSource, image_description, service_id, photographer_id) VALUES
('chris-CxoEeNkJwUA-unsplash.jpg','Bride and groom during ceremony',1, 1),
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 1),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 1),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 1),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 1),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 1),
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

  

    
 