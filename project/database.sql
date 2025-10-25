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
    FOREIGN KEY (service_id) REFERENCES Service(service_id) ON DELETE CASCADE,
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id) ON DELETE CASCADE
);

CREATE TABLE Photographer_Service
(
    photographerService_id INT AUTO_INCREMENT PRIMARY KEY,
    photographer_id INT,
    service_id INT,
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Service(service_id) ON DELETE CASCADE
);

CREATE TABLE Cart
(
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    createdDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    lastUpdated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE
);

CREATE TABLE Cart_Service
(
    cartService_id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT,
    cart_id INT,
    type_id INT,
    addOn_id INT,
    FOREIGN KEY (service_id) REFERENCES Service(service_id) ON DELETE CASCADE,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES ServiceType(type_id) ON DELETE SET NULL,
    FOREIGN KEY (addOn_id) REFERENCES AddOn(addOn_id) ON DELETE SET NULL
);

CREATE TABLE Orders
(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    lastUpdated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    client_id INT,
    address VARCHAR(255) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE
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
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES Service(service_id) ON DELETE CASCADE,
	FOREIGN KEY (type_id) REFERENCES ServiceType(type_id) ON DELETE SET NULL,
    FOREIGN KEY (addOn_id) REFERENCES AddOn(addOn_id) ON DELETE SET NULL,
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id) ON DELETE SET NULL
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
('admin1@gmail.com', 'ef51306214d9a6361ee1d5b452e6d2bb70dc7ebb85bf9e02c3d4747fb57d6bec', '0490557292', '', '', '2025-01-01 09:30:00'),
('admin2@gmail.com', 'ef51306214d9a6361ee1d5b452e6d2bb70dc7ebb85bf9e02c3d4747fb57d6bec', '0490557292', '', '', '2025-01-03 11:45:00');


INSERT INTO Client (email, password, phone, firstName, lastName, preferredPaymentMethod) VALUES
('julicortesarb@gmail.com', '8d2d88bb4441fbd89795917d6eb585ef67aa7f13b57f30eda8b994a03904ab38', '0490557292', 'Juliana', 'Cortes', 'Credit Card'),
('mike.hansen88@yahoo.com', '38aab61555a84be5f1eea1d6790a6005419f035b5efcf757832a1aaf816a6f0b', '0451234567', 'Michael', 'Hansen', 'Credit Card'),
('sara_lee12@gmail.com',    '00c20396f065af467701c634bbf43e1b0bb05b6f9de76047368e5b7b3ac1d190', '0478901234', 'Sara', 'Lee', 'Cash'),
('tom.jenkins@outlook.com', '038ff275dbded9e17df4c869fd6ac730d73ef21e1e13eec9a095fee2a243343e', '0498765432', 'Tom', 'Jenkins', 'Credit Card'),
('diana.ross@mail.com',     'd21dafb415326ffd763b873dfbf28ca8a2dda32dfe6cfdb889b3b075717d1d13', '0487654321', 'Diana', 'Ross', 'Cash'),
('lucas_ng@live.com',       'c332d7c13cc97a04d5b7e24a15b8616a501c20f59fb0dfd9404e65a81b38ff0c', '0477123456', 'Lucas', 'Ng', 'Credit Card'),
('emilybrown123@gmail.com', '7036f91acd9f9c4458b3f202c6e140824fed8476277a03d7f8245b6b6bb9c578', '0466123456', 'Emily', 'Brown', 'Credit Card'),
('omar.youssef@gmail.com',  '84f32adc0b64c8c07fe694e434218b79d0cd18ea673c1fd2b47c3c72cc1fb201', '0433556677', 'Omar', 'Youssef', 'Credit Card'),
('natalie_woods@hotmail.com','292c311b5be4843641a62041e5ebc29ea00767d8290283641c34788d8bc598fa', '0499776655', 'Natalie', 'Woods', 'Cash'),
('leo.fernandez@mail.com',  '5b1fb5283ff377dc62077b408f2e6cdca042fcdf94084a5ba506abaad5551980', '0422446688', 'Leo', 'Fernandez', 'Credit Card');


INSERT INTO Service (name, shortDescription, longDescription, price, coverImage) VALUES
('Wedding', 'Capture your special day with beautiful wedding photography.', 'Our wedding photography service includes a full day of coverage, from the ceremony to the reception, ensuring every precious moment is captured.', 2000.00, 'drew-coffman-llWjwo200fo-unsplash.jpg'),
('Pets', 'Professional portrait sessions for pets.', 'Our pets photography sessions are perfect for capturing timeless images of your furry friends in a relaxed setting.', 300.00, 'jamie-street-s9Tf1eBDFqw-unsplash.jpg'),
('Newborn', 'Capture the precious moments of your newborn with professional photography services.', "We specialize in newborn photography, offering a gentle and personalized experience to preserve the earliest moments of your baby's life.", 1500.00, 'janko-ferlic-EpbIXGCrtK0-unsplash.jpg'),
('Product', 'High-quality product photography to showcase your items.', 'Our product photography service is designed to highlight the features and details of your products, ideal for e-commerce and marketing materials.', 500.00, 'pmv-chamara-CeQiQxNNdUM-unsplash.jpg');

INSERT INTO ServiceType (type_name, shortDescription, price) VALUES
('Mini Session', 'Basic session with 5 edited photos.', 0.00),
('Standard Session', 'Extend session with 10 edited photos and a photo book.', 50.00),
('Deluxe Session', 'Deluxe session with all edited photos, a photo book, and a canvas print.', 100.00);

INSERT INTO AddOn (addOn, price) VALUES
('Extra Edited Photos', 50.00),
('Printed Album', 100.00),
('Both : Extra Edited Photos + Printed Album', 150.00);

INSERT INTO Photographer 
(email, password, phone, firstName, lastName, bioDescription, location, availability, rating, profilePicture) VALUES
('john.doe@example.com', 'bfbfe08edb20e274563cd69250f4e1be3c17bbb919a68082b7fb82802e10ffe0', '0412345678', 'John', 'Doe', 'Experienced photographer specializing in portrait and event photography.', 'Sydney', 'Weekdays', 4.8, 'clem-onojeghuo-jUAcCtbMb0k-unsplash.jpg'),
('emily.smith@example.com', '631fdd64916871af1c2689bf24d6e166ce34726c01bd936dcf60bd680ae29e84', '0498765432', 'Emily', 'Smith', 'Specializing in landscape photography with a keen eye for natural light and outdoor scenes.', 'Melbourne', 'Weekdays', 4.7, 'jakob-owens-f3s0i96CRGQ-unsplash.jpg'),
('michael.jones@example.com', 'd379613d37191f8f64d18ed31314890154647a4e2ba135cb2ab83d7cd5eb4d84', '0401122334', 'Michael', 'Jones', 'Freelance photographer with a focus on corporate headshots and commercial photography.', 'Brisbane', 'Short notice bookings', 4.9, 'home-page-welcome.jpg'),
('sophia.wilson@example.com', 'ccf80f566d86ebe6d1de6741c701e144f7d84e9884ab72e2fba3283ab0d0a36d', '0455667788', 'Sophia', 'Wilson', 'Creative portrait photographer with over 10 years of experience capturing moments that tell stories.', 'Perth', 'Weekends', 5.0, 'andre-furtado-JtV6zyOZSrA-unsplash.jpg'),
('david.brown@example.com', '6f186e817dbe400af280ef52acfdeb843e98df2c4f470c170f01585097c8558e', '0422333445', 'David', 'Brown', 'Experienced in wedding and engagement photography, known for capturing genuine emotions and timeless moments.', 'Adelaide', 'Weekends', 4.6, 'alif-ngoylung-jg-6ARMiaPM-unsplash.jpg'),
('olivia.miller@example.com', '1948f517f8d097b864159837bc56a4c32a39e4d6b9c68bcc441e5d5e31b0a54d', '0433556677', 'Olivia', 'Miller', 'Family and newborn photographer dedicated to capturing the purest moments of life with warmth and elegance.', 'Gold Coast', 'Weekdays', 4.9, 'jakob-owens-f3s0i96CRGQ-unsplash.jpg'),
('benjamin.taylor@example.com', '1ec31f066d9c637d6d858decac04df243af61c80c12d33db8924a7c7b9a14ae2', '0466778899', 'Benjamin', 'Taylor', 'Fashion and editorial photographer with a passion for capturing the latest trends and unique styles.', 'Sydney', 'Weekdays', 4.8, 'luigi-estuye-lucreative-HVK4t3leM1I-unsplash.jpg'),
('ava.anderson@example.com', 'fb34ad71f3c4362954fc3bd671c21ebd9ae0f7032d2df1eed2af218e971e70aa', '0477889900', 'Ava', 'Anderson', 'Specializes in event photography and commercial shoots, ensuring high-quality results for every project.', 'Melbourne', 'Weekends', 4.7, 'marco-xu-ToUPBCO62Lw-unsplash.jpg'),
('liam.thomas@example.com', '5f229cace76bf919146d896308a8f08bc93f89e4548ba6271096809682e1231b', '0488992233', 'Liam', 'Thomas', 'Travel and adventure photographer who captures breathtaking landscapes and remote destinations.', 'Hobart', 'Weekdays', 4.9, 'patrick-pahlke-G7wgKn7j_Rs-unsplash.jpg'),
('chloe.davis@example.com', 'e9787e0f795522c22b1274f1c189ddc8a5fc9e92ea4ceeaa6b79634f066b132c', '0412349876', 'Chloe', 'Davis', 'Wedding and portrait photographer with a passion for capturing candid moments and emotional stories.', 'Canberra', 'Short notice bookings', 4.8, 'stacey-koenitz-bduka9UJzrk-unsplash.jpg'),
('alex.hughes@example.com', '09757beb485e1cf5ff89a57b0294ab8507c4472698adc5401c038493d6109535', '0411999888', 'Alex', 'Hughes', 'Portrait and corporate photographer delivering clean, modern looks for websites and LinkedIn.', 'Newcastle', 'Weekdays', 4.7, 'home-page-welcome.jpg'),
('zoe.martin@example.com', '68f1c48ba69dbd3c8c9529a93003009f4fcf98c2d8d4a1bd303f2471694c5c2f', '0499001122', 'Zoe', 'Martin', 'Family and maternity photographer known for warm tones and natural outdoor light.', 'Sunshine Coast', 'Weekends', 4.9, 'stacey-koenitz-bduka9UJzrk-unsplash.jpg'),
('ethan.walker@example.com', 'ec3a2d011eb79312b7137c3924b8395102cecbd0aa712f9b75f101c9d834224d', '0400776655', 'Ethan', 'Walker', 'Documentary-style event photographer capturing candid moments and brand stories.', 'Darwin', 'Short notice bookings', 4.8, 'jakob-owens-f3s0i96CRGQ-unsplash.jpg'),
('mia.white@example.com', '0f5358f0e3b2ccba51fe0d532fcdaa3006d0d70f5a2bbc10d39a57aa4589a5b3', '0422555011', 'Mia', 'White', 'Wedding and engagement specialist with timeless, airy edits and detail-focused coverage.', 'Geelong', 'Weekdays', 4.6, 'andre-furtado-JtV6zyOZSrA-unsplash.jpg'),
('noah.king@example.com', '0afe867eef6010ee8326b9fe1d2cee2667413309943129bc6830c26e9f9d0516', '0477003344', 'Noah', 'King', 'Studio and product photographer obsessed with crisp lighting and color accuracy.', 'Townsville', 'Weekends', 5.0, 'jakob-owens-DQPP9rVLYGQ-unsplash.jpg');

INSERT INTO Photographer_Service (photographer_id, service_id) VALUES
(1,1),
(1,2),
(2,1),
(2,3),
(2,4),
(3,2),
(4,1),
(4,2),
(4,3),
(4,4),
(5,1),
(5,4),
(6,2),
(6,3),
(7,4),
(8,1),
(8,2),
(8,4),
(9,2),
(9,3),
(10,1),
(11,3),
(11,4),
(12,1),
(12,2),
(12,3),
(13,2),
(14,1),
(14,4),
(15,1),
(15,3);



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
('chris-CxoEeNkJwUA-unsplash.jpg','Bride and groom during ceremony',1, 11),
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 5),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 6),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 13),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 2),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 7),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 1),
('imani-bahati-LxVxPA1LOVM-unsplash.jpg','Stylish shoes for sale',4, 14),
('alvaro-cvg-mW8IZdX7n8E-unsplash.jpg','Outdoor wedding ceremony with balloons',1, 2),
('luwadlin-bosman-P_HRPYpFTNA-unsplash.jpg','Bride and groom dancing at reception',1, 10),
('marc-a-sporys-NO8Sj4dKE8k-unsplash.jpg','Close-up of bride and groom shoes',1, 9),
('furkids-com-tw-V9c7Y_oi1ys-unsplash.jpg','Dog looking out a cafe window',2, 1),
('celine-druguet-Y5W-1NlqBQw-unsplash.jpg','Studio portrait of a black-and-white dog',2, 9),
('gabriel-jones-mcvpMaUQ1Eo-unsplash.jpg','Dog standing in a retro living room',2, 11),
('brian-erickson-pbmRKbQ5VHY-unsplash.jpg','Newborn baby in a hospital bassinet',3, 2),
('matthew-osborn-tAQJE4mySN4-unsplash.jpg','Newborn asleep in a wicker basket',3, 4),
('javier-gonzalez-fotografo-B34_uqPppi0-unsplash.jpg','Baby boy wearing a knit hat on a pillow',3, 6),
('toa-heftiba-z6wMRo7jx-s-unsplash.jpg','Newborn sleeping on a bed in neutral tones',3, 15),
('kadyn-pierce-8_f5p6xROew-unsplash.jpg','Baby lying on a blanket with milestone cards',3, 1),
('edward-go-Lhx2dU49Lp8-unsplash.jpg','Swaddled newborn with a bunny toy',3, 2),
('gold-chain-collective-wLJOUebBwJ4-unsplash.jpg','Green glass bottle with oranges on colorful background',4, 12),
('rohit-sharma-7qt_K3esmck-unsplash.jpg','Smartphone on a wooden background',4, 3),
('jack-atkinson-RsohkU8mrxU-unsplash.jpg','Skincare bottle with stones and towel',4, 8),
('praniket-desai-ZZVP99CMSJE-unsplash.jpg','Wine bottle and glasses with grapes',4, 10),
('ela-de-pure-Youa6n5fssM-unsplash.jpg','Cosmetic jars arranged on a podium',4, 6),

('chris-CxoEeNkJwUA-unsplash.jpg','Bride and groom during ceremony',1, 3),
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 12),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 15),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 2),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 5),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 9),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 4),
('imani-bahati-LxVxPA1LOVM-unsplash.jpg','Stylish shoes for sale',4, 7),
('alvaro-cvg-mW8IZdX7n8E-unsplash.jpg','Outdoor wedding ceremony with balloons',1, 13),
('luwadlin-bosman-P_HRPYpFTNA-unsplash.jpg','Bride and groom dancing at reception',1, 1),
('marc-a-sporys-NO8Sj4dKE8k-unsplash.jpg','Close-up of bride and groom shoes',1, 8),
('furkids-com-tw-V9c7Y_oi1ys-unsplash.jpg','Dog looking out a cafe window',2, 3),
('celine-druguet-Y5W-1NlqBQw-unsplash.jpg','Studio portrait of a black-and-white dog',2, 14),
('gabriel-jones-mcvpMaUQ1Eo-unsplash.jpg','Dog standing in a retro living room',2, 10),
('brian-erickson-pbmRKbQ5VHY-unsplash.jpg','Newborn baby in a hospital bassinet',3, 8),
('matthew-osborn-tAQJE4mySN4-unsplash.jpg','Newborn asleep in a wicker basket',3, 11),
('javier-gonzalez-fotografo-B34_uqPppi0-unsplash.jpg','Baby boy wearing a knit hat on a pillow',3, 7),
('toa-heftiba-z6wMRo7jx-s-unsplash.jpg','Newborn sleeping on a bed in neutral tones',3, 6),
('kadyn-pierce-8_f5p6xROew-unsplash.jpg','Baby lying on a blanket with milestone cards',3, 12),
('edward-go-Lhx2dU49Lp8-unsplash.jpg','Swaddled newborn with a bunny toy',3, 15),
('gold-chain-collective-wLJOUebBwJ4-unsplash.jpg','Green glass bottle with oranges on colorful background',4, 5),
('rohit-sharma-7qt_K3esmck-unsplash.jpg','Smartphone on a wooden background',4, 9),
('jack-atkinson-RsohkU8mrxU-unsplash.jpg','Skincare bottle with stones and towel',4, 11),
('praniket-desai-ZZVP99CMSJE-unsplash.jpg','Wine bottle and glasses with grapes',4, 2),
('ela-de-pure-Youa6n5fssM-unsplash.jpg','Cosmetic jars arranged on a podium',4, 13),

('chris-CxoEeNkJwUA-unsplash.jpg','Bride and groom during ceremony',1, 6),
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 14),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 12),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 1),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 4),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 10),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 9),
('imani-bahati-LxVxPA1LOVM-unsplash.jpg','Stylish shoes for sale',4, 15),
('alvaro-cvg-mW8IZdX7n8E-unsplash.jpg','Outdoor wedding ceremony with balloons',1, 7),
('luwadlin-bosman-P_HRPYpFTNA-unsplash.jpg','Bride and groom dancing at reception',1, 5),
('marc-a-sporys-NO8Sj4dKE8k-unsplash.jpg','Close-up of bride and groom shoes',1, 2),
('furkids-com-tw-V9c7Y_oi1ys-unsplash.jpg','Dog looking out a cafe window',2, 13),
('celine-druguet-Y5W-1NlqBQw-unsplash.jpg','Studio portrait of a black-and-white dog',2, 6),
('gabriel-jones-mcvpMaUQ1Eo-unsplash.jpg','Dog standing in a retro living room',2, 8),
('brian-erickson-pbmRKbQ5VHY-unsplash.jpg','Newborn baby in a hospital bassinet',3, 3),
('matthew-osborn-tAQJE4mySN4-unsplash.jpg','Newborn asleep in a wicker basket',3, 14),
('javier-gonzalez-fotografo-B34_uqPppi0-unsplash.jpg','Baby boy wearing a knit hat on a pillow',3, 5),
('toa-heftiba-z6wMRo7jx-s-unsplash.jpg','Newborn sleeping on a bed in neutral tones',3, 9),
('kadyn-pierce-8_f5p6xROew-unsplash.jpg','Baby lying on a blanket with milestone cards',3, 13),
('edward-go-Lhx2dU49Lp8-unsplash.jpg','Swaddled newborn with a bunny toy',3, 6),
('gold-chain-collective-wLJOUebBwJ4-unsplash.jpg','Green glass bottle with oranges on colorful background',4, 4),
('rohit-sharma-7qt_K3esmck-unsplash.jpg','Smartphone on a wooden background',4, 6),
('jack-atkinson-RsohkU8mrxU-unsplash.jpg.jpg','Skincare bottle with stones and towel',4, 7),
('praniket-desai-ZZVP99CMSJE-unsplash.jpg','Wine bottle and glasses with grapes',4, 3),
('ela-de-pure-Youa6n5fssM-unsplash.jpg','Cosmetic jars arranged on a podium',4, 10),

('chris-CxoEeNkJwUA-unsplash.jpg','Bride and groom during ceremony',1, 13),
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 4),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 9),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 6),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 8),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 1),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 2),
('imani-bahati-LxVxPA1LOVM-unsplash.jpg','Stylish shoes for sale',4, 11),
('alvaro-cvg-mW8IZdX7n8E-unsplash.jpg','Outdoor wedding ceremony with balloons',1, 12),
('luwadlin-bosman-P_HRPYpFTNA-unsplash.jpg','Bride and groom dancing at reception',1, 7),
('marc-a-sporys-NO8Sj4dKE8k-unsplash.jpg','Close-up of bride and groom shoes',1, 10),
('furkids-com-tw-V9c7Y_oi1ys-unsplash.jpg','Dog looking out a cafe window',2, 14),
('celine-druguet-Y5W-1NlqBQw-unsplash.jpg','Studio portrait of a black-and-white dog',2, 3),
('gabriel-jones-mcvpMaUQ1Eo-unsplash.jpg','Dog standing in a retro living room',2, 5),
('brian-erickson-pbmRKbQ5VHY-unsplash.jpg','Newborn baby in a hospital bassinet',3, 10),
('matthew-osborn-tAQJE4mySN4-unsplash.jpg','Newborn asleep in a wicker basket',3, 12),
('javier-gonzalez-fotografo-B34_uqPppi0-unsplash.jpg','Baby boy wearing a knit hat on a pillow',3, 9),
('toa-heftiba-z6wMRo7jx-s-unsplash.jpg','Newborn sleeping on a bed in neutral tones',3, 2),
('kadyn-pierce-8_f5p6xROew-unsplash.jpg','Baby lying on a blanket with milestone cards',3, 11),
('edward-go-Lhx2dU49Lp8-unsplash.jpg','Swaddled newborn with a bunny toy',3, 7),
('gold-chain-collective-wLJOUebBwJ4-unsplash.jpg','Green glass bottle with oranges on colorful background',4, 8),
('rohit-sharma-7qt_K3esmck-unsplash.jpg','Smartphone on a wooden background',4, 5),
('jack-atkinson-RsohkU8mrxU-unsplash.jpg','Skincare bottle with stones and towel',4, 9),
('praniket-desai-ZZVP99CMSJE-unsplash.jpg','Wine bottle and glasses with grapes',4, 12),
('ela-de-pure-Youa6n5fssM-unsplash.jpg','Cosmetic jars arranged on a podium',4, 13),

('chris-CxoEeNkJwUA-unsplash.jpg','Bride and groom during ceremony',1, 7),
('asdrubal-luna-Qxi-boLL4bs-unsplash.jpg','Wedding couple with family',1, 8),
('jay-wennington-CdK2eYhWfQ0-unsplash.jpg','Golden retriever portrait',2, 2),
('andrew-s-ouo1hbizWwo-unsplash.jpg','Cat in a playful pose',2, 4),
('garrett-jackson-oOnJWBMlb5A-unsplash.jpg','Newborn baby sleeping peacefully',3, 12),
('hollie-santos-aUtvHsu8Uzk-unsplash.jpg','Parents with their newborn baby',3, 13),
('daniel-korpai-hbTKIbuMmBI-unsplash.jpg','High-end watch on display',4, 6),
('imani-bahati-LxVxPA1LOVM-unsplash.jpg','Stylish shoes for sale',4, 5),
('alvaro-cvg-mW8IZdX7n8E-unsplash.jpg','Outdoor wedding ceremony with balloons',1, 11),
('luwadlin-bosman-P_HRPYpFTNA-unsplash.jpg','Bride and groom dancing at reception',1, 15),
('marc-a-sporys-NO8Sj4dKE8k-unsplash.jpg','Close-up of bride and groom shoes',1, 3),
('furkids-com-tw-V9c7Y_oi1ys-unsplash.jpg','Dog looking out a cafe window',2, 10),
('celine-druguet-Y5W-1NlqBQw-unsplash.jpg','Studio portrait of a black-and-white dog',2, 13),
('gabriel-jones-mcvpMaUQ1Eo-unsplash.jpg','Dog standing in a retro living room',2, 1),
('brian-erickson-pbmRKbQ5VHY-unsplash.jpg','Newborn baby in a hospital bassinet',3, 1),
('matthew-osborn-tAQJE4mySN4-unsplash.jpg','Newborn asleep in a wicker basket',3, 6),
('javier-gonzalez-fotografo-B34_uqPppi0-unsplash.jpg','Baby boy wearing a knit hat on a pillow',3, 9),
('toa-heftiba-z6wMRo7jx-s-unsplash.jpg','Newborn sleeping on a bed in neutral tones',3, 2),
('kadyn-pierce-8_f5p6xROew-unsplash.jpg','Baby lying on a blanket with milestone cards',3, 8),
('edward-go-Lhx2dU49Lp8-unsplash.jpg','Swaddled newborn with a bunny toy',3, 6),
('gold-chain-collective-wLJOUebBwJ4-unsplash.jpg','Green glass bottle with oranges on colorful background',4, 7),
('rohit-sharma-7qt_K3esmck-unsplash.jpg','Smartphone on a wooden background',4, 9),
('jack-atkinson-RsohkU8mrxU-unsplash.jpg','Skincare bottle with stones and towel',4, 13),
('praniket-desai-ZZVP99CMSJE-unsplash.jpg','Wine bottle and glasses with grapes',4, 2),
('ela-de-pure-Youa6n5fssM-unsplash.jpg','Cosmetic jars arranged on a podium',4, 9);




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