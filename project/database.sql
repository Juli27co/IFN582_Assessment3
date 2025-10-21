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
    client_id INT,
    address VARCHAR(255) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
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
('admin1@gmail.com', 'b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb0f1d1a4f6e6d6f0b1f6d9f3d0', '0490557292', '', '', '2025-01-01 09:30:00'),
('admin2@gmail.com', 'b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb0f1d1a4f6e6d6f0b1f6d9f3d0', '0490557292', '', '', '2025-01-03 11:45:00');


INSERT INTO Client (email, password, phone, firstName, lastName, preferredPaymentMethod) VALUES
('julicortesarb@gmail.com', 'b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb0f1d1a4f6e6d6f0b1f6d9f3d0', '0490557292', 'Juliana', 'Cortes', 'Credit Card'),
('mike.hansen88@yahoo.com', '5348d991c98f6633ed258afcd3b75b8d650a10df645c9ab6f75e264926427d5b', '0451234567', 'Michael', 'Hansen', 'Credit Card'),
('sara_lee12@gmail.com', '30de04940d6e88d8f82fa57ca7c2b9c50de1bd1e2e7c318e44b4e5c1036e3d3c', '0478901234', 'Sara', 'Lee', 'Cash'),
('tom.jenkins@outlook.com', 'e04ff4d1cd6e1bf7e47a5f2d29d5a8d6381f240d34df0aa9a7f8f3cd91e5a05d', '0498765432', 'Tom', 'Jenkins', 'Credit Card'),
('diana.ross@mail.com', 'b2eddd64f89b1cb5c93e0709a18f7574898ca8b4f5d6c1d942b8bdb5e0cbd0a3', '0487654321', 'Diana', 'Ross', 'Cash'),
('lucas_ng@live.com', '5f5cfabfbbe9b5e6b9bbf7b0c5c88d34fae0787e6460a9cbbbc798be54c2c7af', '0477123456', 'Lucas', 'Ng', 'Credit Card'),
('emilybrown123@gmail.com', '7f6ad475c2e62fa3a3d6e830b954320b638d8ff4ea4652a934ed6a7f5e3e0c38', '0466123456', 'Emily', 'Brown', 'Credit Card'),
('omar.youssef@gmail.com', 'd2ea159a47c047cc05a5b6ecc5d0402d6d8fde5253d8bd96a4b83acb7a4f1d6d', '0433556677', 'Omar', 'Youssef', 'Credit Card'),
('natalie_woods@hotmail.com', '62fc5162c7056eeff1e5d4b19a142043dd44f4bea7f2a7bc01db57ee97dc0bff', '0499776655', 'Natalie', 'Woods', 'Cash'),
('leo.fernandez@mail.com', '75304fb1d2111093c8e9905e0d207ba318915d6f1f03c2b9c52f4a1517972ed2', '0422446688', 'Leo', 'Fernandez', 'Credit Card');


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
('john.doe@example.com', '4dbd5e49147b5102ee2731ac03dd0db7decc3b8715c3df3c1f3ddc62dcbcf86d', '0412345678', 'John', 'Doe', 'Experienced photographer specializing in portrait and event photography.', 'Sydney', 'Weekdays', 4.8, 'clem-onojeghuo-jUAcCtbMb0k-unsplash.jpg'),
('emily.smith@example.com', '5e9debce1deef8c0096b74dec27f4704a9eece077978c88a2530ed30db07f450', '0498765432', 'Emily', 'Smith', 'Specializing in landscape photography with a keen eye for natural light and outdoor scenes.', 'Melbourne', 'Weekdays', 4.7, 'jakob-owens-f3s0i96CRGQ-unsplash.jpg'),
('michael.jones@example.com', 'b63df8656b78eb0db74d65d15ab6c36b8ba0a3f7bef4ebfcc41c4ad75dd5724b', '0401122334', 'Michael', 'Jones', 'Freelance photographer with a focus on corporate headshots and commercial photography.', 'Brisbane', 'Short notice bookings', 4.9, 'home-page-welcome.jpg'),
('sophia.wilson@example.com', '7bb2dbd81bf00f3564e035db97e7d224b1d887645370a2f4ed5dcc5cfaa9eb29', '0455667788', 'Sophia', 'Wilson', 'Creative portrait photographer with over 10 years of experience capturing moments that tell stories.', 'Perth', 'Weekends', 5.0, 'andre-furtado-JtV6zyOZSrA-unsplash.jpg'),
('david.brown@example.com', '88d21bcd079235290778ebf22486b7e71c6fe2a5230f1cc5c764ae4b17bc8344', '0422333445', 'David', 'Brown', 'Experienced in wedding and engagement photography, known for capturing genuine emotions and timeless moments.', 'Adelaide', 'Weekends', 4.6, 'alif-ngoylung-jg-6ARMiaPM-unsplash.jpg'),
('olivia.miller@example.com', 'dbe816a84781322fad7cba8cabb6c3477ff13978ba5f530f2ed2e84fcf4a048f', '0433556677', 'Olivia', 'Miller', 'Family and newborn photographer dedicated to capturing the purest moments of life with warmth and elegance.', 'Gold Coast', 'Weekdays', 4.9, 'jakob-owens-DQPP9rVLYGQ-unsplash.jpg'),
('benjamin.taylor@example.com', 'be09643fd6a65f76801be40de19d55fd799238e85e4805b7ecbd0443897c8523', '0466778899', 'Benjamin', 'Taylor', 'Fashion and editorial photographer with a passion for capturing the latest trends and unique styles.', 'Sydney', 'Weekdays', 4.8, 'luigi-estuye-lucreative-HVK4t3leM1I-unsplash.jpg'),
('ava.anderson@example.com', 'eb7f1a6e2264a882c78fa074be472482fb9be174376721b594c8570a9bd8c09d', '0477889900', 'Ava', 'Anderson', 'Specializes in event photography and commercial shoots, ensuring high-quality results for every project.', 'Melbourne', 'Weekends', 4.7, 'marco-xu-ToUPBCO62Lw-unsplash.jpg'),
('liam.thomas@example.com', 'aefd9a7f7cf078ea869e3d62138d0f99865947d6d9135ad0f8c0c3c70264d63f', '0488992233', 'Liam', 'Thomas', 'Travel and adventure photographer who captures breathtaking landscapes and remote destinations.', 'Hobart', 'Weekdays', 4.9, 'patrick-pahlke-G7wgKn7j_Rs-unsplash.jpg'),
('chloe.davis@example.com', 'da56f72946d3fe164d2ba180baf97c16cfe92b086dd8a7da4c9cc5188b1479a9', '0412349876', 'Chloe', 'Davis', 'Wedding and portrait photographer with a passion for capturing candid moments and emotional stories.', 'Canberra', 'Short notice bookings', 4.8, 'stacey-koenitz-bduka9UJzrk-unsplash.jpg'),
('alex.hughes@example.com', 'e3a1da282372e7b47476e5d070abb13e5047e985bad416f9332a63b1d607a8e5', '0411999888', 'Alex', 'Hughes', 'Portrait and corporate photographer delivering clean, modern looks for websites and LinkedIn.', 'Newcastle', 'Weekdays', 4.7, 'home-page-welcome.jpg'),
('zoe.martin@example.com', '65b2c6b17d3b0af160e650fc311eb68cb5d170a9a226ccbaa0dc185cce27910b', '0499001122', 'Zoe', 'Martin', 'Family and maternity photographer known for warm tones and natural outdoor light.', 'Sunshine Coast', 'Weekends', 4.9, 'zoe-martin-portrait.jpg'),
('ethan.walker@example.com', 'da8c3441e824c0caa630acf018d5d908734738b536206e6d1d10d58a818b1223', '0400776655', 'Ethan', 'Walker', 'Documentary-style event photographer capturing candid moments and brand stories.', 'Darwin', 'Short notice bookings', 4.8, 'jakob-owens-f3s0i96CRGQ-unsplash.jpg'),
('mia.white@example.com', 'f1a3e04947893999b0890973025cd24e65106892c6ce1beb9a00c815589b8cce', '0422555011', 'Mia', 'White', 'Wedding and engagement specialist with timeless, airy edits and detail-focused coverage.', 'Geelong', 'Weekdays', 4.6, 'andre-furtado-JtV6zyOZSrA-unsplash.jpg'),
('noah.king@example.com', '3e067006faa5a8436f96a4a2b390c164fbccac89c1f4cab8963f8ae7617d3905', '0477003344', 'Noah', 'King', 'Studio and product photographer obsessed with crisp lighting and color accuracy.', 'Townsville', 'Weekends', 5.0, 'jakob-owens-DQPP9rVLYGQ-unsplash.jpg');

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
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 2),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 1),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 2),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 2),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 1),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 2),
('imani-bahati-LxVxPA1LOVM-unsplash.jpg','Stylish shoes for sale',4, 1),
('alvaro-cvg-mW8IZdX7n8E-unsplash.jpg','Outdoor wedding ceremony with balloons',1,2),
('luwadlin-bosman-P_HRPYpFTNA-unsplash.jpg','Bride and groom dancing at reception',1,3),
('marc-a-sporys-NO8Sj4dKE8k-unsplash.jpg','Close-up of bride and groom shoes',1,4),
('furkids-com-tw-V9c7Y_oi1ys-unsplash.jpg','Dog looking out a cafe window',2,5),
('celine-druguet-Y5W-1NlqBQw-unsplash.jpg','Studio portrait of a black-and-white dog',2,6),
('gabriel-jones-mcvpMaUQ1Eo-unsplash.jpg','Dog standing in a retro living room',2,7),
('brian-erickson-pbmRKbQ5VHY-unsplash.jpg','Newborn baby in a hospital bassinet',3,8),
('matthew-osborn-tAQJE4mySN4-unsplash.jpg','Newborn asleep in a wicker basket',3,9),
('javier-gonzalez-fotografo-B34_uqPppi0-unsplash.jpg','Baby boy wearing a knit hat on a pillow',3,10),
('toa-heftiba-z6wMRo7jx-s-unsplash.jpg','Newborn sleeping on a bed in neutral tones',3,11),
('kadyn-pierce-8_f5p6xROew-unsplash.jpg','Baby lying on a blanket with milestone cards',3,12),
('edward-go-Lhx2dU49Lp8-unsplash.jpg','Swaddled newborn with a bunny toy',3,13),
('gold-chain-collective-wLJOUebBwJ4-unsplash.jpg','Green glass bottle with oranges on colorful background',4,14),
('rohit-sharma-7qt_K3esmck-unsplash.jpg','Smartphone on a wooden background',4,15),
('jack-atkinson-RsohkuU8mrxU-unsplash.jpg','Skincare bottle with stones and towel',4,2),
('praniket-desai-ZZVP99CMSJE-unsplash.jpg','Wine bottle and glasses with grapes',4,3),
('ela-de-pure-Youa6n5fssM-unsplash.jpg','Cosmetic jars arranged on a podium',4,4);


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

INSERT INTO Orders (createdDate, lastUpdated, client_id, address, payment_method) VALUES
('2025-01-05 10:15:00', '2025-01-05 10:15:00', 1, '22 Street Av, Parramatta NSW 2150', 'Cash'),
('2025-01-08 14:30:00', '2025-01-08 14:30:00', 2, '12 Maple Drive, Carlton VIC 3053', 'Credit card'),
('2025-01-12 09:45:00', '2025-01-12 10:00:00', 3, '450 Ocean Blvd, Surfers Paradise QLD 4217', 'Credit card'),
('2025-01-15 13:20:00', '2025-01-15 13:20:00', 4, '99 Elm Street, Adelaide SA 5000', 'Credit card'),
('2025-01-17 16:05:00', '2025-01-17 16:30:00', 5, '102 Pine Ave, Fremantle WA 6160', 'Credit card'),
('2025-01-20 11:50:00', '2025-01-20 12:00:00', 6, '78 Sunset Road, Hobart TAS 7000', 'Cash'),
('2025-01-22 08:10:00', '2025-01-22 08:10:00', 7, '66 Birch Lane, Canberra ACT 2601', 'Cash'),
('2025-01-24 15:25:00', '2025-01-24 15:40:00', 1, '120 King Street, Brisbane QLD 4000', 'Credit card'),
('2025-01-26 10:05:00', '2025-01-26 10:10:00', 2, '33 Riverbank Rd, Geelong VIC 3220', 'Cash'),
('2025-01-28 18:45:00', '2025-01-28 19:00:00', 3, '88 Queen Ave, Newcastle NSW 2300', 'Credit card');

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


  