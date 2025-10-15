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
    service_id varchar(100) NOT NULL,
    name varchar(100) NOT NULL,
    shortDescription varchar(100) NOT NULL,
    longDescription varchar(255) NOT NULL,
    price decimal(10,2) NOT NULL,
    PRIMARY KEY (service_id)
);

CREATE TABLE Image
(
    image_id varchar(100) NOT NULL,
    imageSource varchar(255) NOT NULL,
    image_description varchar(255),
    service_id varchar(100),
    portfolio_id varchar(100),
    PRIMARY KEY (image_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolio(portfolio_id)
);

CREATE TABLE Photographer
(
    photographer_id varchar(100) NOT NULL,
    email varchar(100) NOT NULL,
    password varchar(200) NOT NULL,
    phone varchar(15) NOT NULL,
    firstName varchar(20) NOT NULL,
    lastName varchar(20) NOT NULL,
    bioDescription varchar(255),
    location varchar (50),
    availability varchar(50),
    rating decimal(2,1),
    PRIMARY KEY (photographer_id)
);

CREATE TABLE Portfolio
(
    portfolio_id varchar(100) NOT NULL,
    photographer_id varchar(100) NOT NULL,
    PRIMARY KEY (portfolio_id),
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

CREATE TABLE Photographer_Service
(
    photographerService_id varchar(100) NOT NULL,
    photographer_id varchar(100) NOT NULL,
    service_id varchar(100) NOT NULL,
    PRIMARY KEY (photographerService_id),
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
);

CREATE TABLE Cart
(
    cart_id varchar(100) NOT NULL,
    createdDate datetime NOT NULL,
    lastUpdated datetime NOT NULL,
    client_id varchar(100) NOT NULL,
    PRIMARY KEY (cart_id),
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);

CREATE TABLE Cart_Service
(
    cartService_id varchar(100) NOT NULL,
    service_id varchar(100) NOT NULL,
    cart_id varchar(100) NOT NULL,
    type_id varchar(100) NOT NULL,
    addOn varchar(255) NOT NULL,
    PRIMARY KEY (cartService_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (type_id) REFERENCES Type(type_id),
    FOREIGN KEY (addOn) REFERENCES AddOn(addOn_id)
);

CREATE TABLE Orders
(
    order_id varchar(100) NOT NULL,
    createdDate datetime NOT NULL,
    lastUpdated datetime NOT NULL,
    message varchar(100) NOT NULL,
    paymentMethod varchar(50) NOT NULL,
    photographer_id varchar(100) NOT NULL,
    client_id varchar(100) NOT NULL,
    address_id varchar(100) NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (client_id) REFERENCES Client(client_id),
    FOREIGN KEY (photographer_id) REFERENCES Photographer(photographer_id)
);

CREATE TABLE Order_Service
(
    orderService_id varchar(100) NOT NULL,
    service_id varchar(100) NOT NULL,
    order_id varchar(100) NOT NULL,
    PRIMARY KEY (orderService_id),
    FOREIGN KEY (service_id) REFERENCES Service(service_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

CREATE TABLE Type
(
    type_id varchar(100) NOT NULL,
    type varchar(100) NOT NULL,
    shortDescription varchar(100),
    price decimal(10,2) NOT NULL,
    PRIMARY KEY (type_id)
);

CREATE TABLE AddOn
(
    addOn_id varchar(100) NOT NULL,
    addOn varchar(100) NOT NULL,
    price decimal(10,2) NOT NULL,
    PRIMARY KEY (addOn_id)
);

CREATE TABLE Inquery(
    inquiry_id INT AUTO_INCREMENT PRIMARY KEY,
    fullName VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    message VARCHAR(255) NOT NULL,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Client (client_id, email, password, phone, firstName, lastName, preferredPaymentMethod, address) VALUES
('C001', 'julicortesarb@gmail.com', '1234qwer', '0490557292', 'Juliana', 'Cortes', 'Credit Card', '22 Street Av')
('C002', 'mike.hansen88@yahoo.com', 'passM!ke88', '0451234567', 'Michael', 'Hansen', 'PayPal', '12 Maple Drive'),
('C003', 'sara_lee12@gmail.com', 'saraLeePwd', '0478901234', 'Sara', 'Lee', 'Debit Card', '450 Ocean Blvd'),
('C004', 'tom.jenkins@outlook.com', 'jenkinsT90', '0498765432', 'Tom', 'Jenkins', 'Bank Transfer', '99 Elm Street'),
('C005', 'diana.ross@mail.com', 'rossDiana21', '0487654321', 'Diana', 'Ross', 'Credit Card', '102 Pine Ave'),
('C006', 'lucas_ng@live.com', 'lucasNg@2023', '0477123456', 'Lucas', 'Ng', 'Cash', '78 Sunset Road'),
('C007', 'emilybrown123@gmail.com', 'emBrown!45', '0466123456', 'Emily', 'Brown', 'Credit Card', '66 Birch Lane'),
('C008', 'omar.youssef@gmail.com', 'Omar2024$', '0433556677', 'Omar', 'Youssef', 'Debit Card', '120 King Street'),
('C009', 'natalie_woods@hotmail.com', 'natWoods99', '0499776655', 'Natalie', 'Woods', 'PayPal', '33 Riverbank Rd'),
('C010', 'leo.fernandez@mail.com', 'FernLeo#10', '0422446688', 'Leo', 'Fernandez', 'Credit Card', '88 Queen Ave');

INSERT INTO Cart (cart_id, createdDate, lastUpdated, client_id) VALUES
('CR001', '2024-10-01 10:00:00', '2024-10-01 10:00:00', 'C001'),
('CR002', '2024-10-02 14:15:00', '2024-10-02 14:15:00', 'C002'),
('CR003', '2024-10-03 09:30:00', '2024-10-03 09:30:00', 'C003'),
('CR004', '2024-10-04 17:45:00', '2024-10-04 17:45:00', 'C004'),
('CR005', '2024-10-05 12:00:00', '2024-10-05 12:00:00', 'C005'),
('CR006', '2024-10-06 08:30:00', '2024-10-06 08:30:00', 'C006'),
('CR007', '2024-10-07 11:00:00', '2024-10-07 11:00:00', 'C007'),
('CR008', '2024-10-08 13:25:00', '2024-10-08 13:25:00', 'C008'),
('CR009', '2024-10-09 15:10:00', '2024-10-09 15:10:00', 'C009'),
('CR010', '2024-10-10 16:50:00', '2024-10-10 16:50:00', 'C010');

INSERT INTO Service (service_id, name, shortDescription, longDescription, price) VALUES
('S001', 'Wedding Photography', 'Capture your special day with beautiful wedding photography.', 'Our wedding photography service includes a full day of coverage, from the ceremony to the reception, ensuring every precious moment is captured.', 2000.00),
('S002', 'Pets Photography', 'Professional portrait sessions for pets.', 'Our pets photography sessions are perfect for capturing timeless images of your furry friends in a relaxed setting.', 300.00),
('S003', 'Newborn Photography', 'Capture the precious moments of your newborn with professional photography services.', 'We specialize in newborn photography, offering a gentle and personalized experience to preserve the earliest moments of your baby’s life.', 1500.00),
('S004', 'Product Photography', 'High-quality product photography to showcase your items.', 'Our product photography service is designed to highlight the features and details of your products, ideal for e-commerce and marketing materials.', 500.00),

INSERT INTO Type (type_id, type, shortDescription, price) VALUES
('T001', 'Mini Session', '30 minutes session with 5 edited photos.', 100.00),
('T002', 'Standard Session', '60 minutes session with 10 edited photos and a photo book.', 300.00),
('T003', 'Deluxe Session', '90 minutes session with all edited photos, a photo book, and a canvas print.', 500.00)

INSERT INTO AddOn (addOn_id, addOn) VALUES
('A001', 'Extra Edited Photos'),
('A002', 'Printed Album')

INSERT INTO Photographer (photographer_id, email, password, phone, firstName, lastName, bioDescription, location, availability, rating) VALUES
('P001', 'john.doe@example.com', 'securePassword123', '0412345678', 'John', 'Doe', 'Experienced photographer specializing in portrait and event photography.', 'Sydney', 'Weekdays', 4.8),
('P002', 'emily.smith@example.com', 'pass1234secure', '0498765432', 'Emily', 'Smith', 'Specializing in landscape photography with a keen eye for natural light and outdoor scenes.', 'Melbourne', 'Weekdays', 4.7),
('P003', 'michael.jones@example.com', 'mikephoto321', '0401122334', 'Michael', 'Jones', 'Freelance photographer with a focus on corporate headshots and commercial photography.', 'Brisbane', 'Short notice bookings', 4.9),
('P004', 'sophia.wilson@example.com', 'sophiaW!23', '0455667788', 'Sophia', 'Wilson', 'Creative portrait photographer with over 10 years of experience capturing moments that tell stories.', 'Perth', 'Weekends', 5.0),
('P005', 'david.brown@example.com', 'davidsPhoto2023', '0422333445', 'David', 'Brown', 'Experienced in wedding and engagement photography, known for capturing genuine emotions and timeless moments.', 'Adelaide', 'Weekends', 4.6),
('P006', 'olivia.miller@example.com', 'OliviaM123!', '0433556677', 'Olivia', 'Miller', 'Family and newborn photographer dedicated to capturing the purest moments of life with warmth and elegance.', 'Gold Coast', 'Weekdays', 4.9),
('P007', 'benjamin.taylor@example.com', 'photoBen5678', '0466778899', 'Benjamin', 'Taylor', 'Fashion and editorial photographer with a passion for capturing the latest trends and unique styles.', 'Sydney', 'Weekdays', 4.8),
('P008', 'ava.anderson@example.com', 'Ava2023secure', '0477889900', 'Ava', 'Anderson', 'Specializes in event photography and commercial shoots, ensuring high-quality results for every project.', 'Melbourne', 'Weekends', 4.7),
('P009', 'liam.thomas@example.com', 'LiamPhoto987', '0488992233', 'Liam', 'Thomas', 'Travel and adventure photographer who captures breathtaking landscapes and remote destinations.', 'Hobart', 'Weekdays', 4.9),
('P010', 'chloe.davis@example.com', 'Chloe2023!Pass', '0412349876', 'Chloe', 'Davis', 'Wedding and portrait photographer with a passion for capturing candid moments and emotional stories.', 'Canberra', 'Short notice bookings', 4.85)

INSERT INTO Photographer_Service (photographerService_id, photographer_id, service_id) VALUES
('P001S001', 'P001', 'S001'),
('P002S002', 'P002', 'S002'),
('P003S003', 'P003', 'S003'),
('P004S004', 'P004', 'S004'),
('P005S001', 'P005', 'S001'),
('P006S003', 'P006', 'S003'),
('P007S004', 'P007', 'S004'),
('P008S002', 'P008', 'S002'),
('P009S002', 'P009', 'S002'),
('P010S001', 'P010', 'S001')

INSERT INTO Portfolio (portfolio_id, photographer_id) VALUES
('PF001', 'P001'),
('PF002', 'P002'),
('PF003', 'P003'),
('PF004', 'P004'),
('PF005', 'P005'),
('PF006', 'P006'),
('PF007', 'P007'),
('PF008', 'P008'),
('PF009', 'P009'),
('PF010', 'P010')

INSERT INTO Image (image_id, imageSource, image_description, service_id) VALUES
('IMG001', 'https://example.com/images/wedding1.jpg', 'Bride and groom during ceremony', 'S001'),
('IMG002', 'https://example.com/images/wedding2.jpg', 'Wedding couple with family', 'S001'),
('IMG003', 'https://example.com/images/pets1.jpg', 'Golden retriever portrait', 'S002'),
('IMG004', 'https://example.com/images/pets2.jpg', 'Cat in a playful pose', 'S002'),
('IMG005', 'https://example.com/images/newborn1.jpg', 'Newborn baby sleeping peacefully', 'S003'),
('IMG006', 'https://example.com/images/newborn2.jpg', 'Parents with their newborn baby', 'S003'),
('IMG007', 'https://example.com/images/product1.jpg', 'High-end watch on display', 'S004'),
('IMG008', 'https://example.com/images/product2.jpg', 'Stylish shoes for sale', 'S004')

