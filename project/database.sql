INSERT INTO Client (client_id, email, password, phone, firstName, lastName, preferredPaymentMethod, address) VALUES
('C001', 'julicortesarb@gmail.com', '1234qwer', '0490557292', 'Juliana', 'Cortes', 'Credit Card', '22 Street Av'),
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
('S004', 'Product Photography', 'High-quality product photography to showcase your items.', 'Our product photography service is designed to highlight the features and details of your products, ideal for e-commerce and marketing materials.', 500.00);

INSERT INTO Type (type_id, type_name, shortDescription, price) VALUES
('T001', 'Mini Session', '30 minutes session with 5 edited photos.', 100.00),
('T002', 'Standard Session', '60 minutes session with 10 edited photos and a photo book.', 300.00),
('T003', 'Deluxe Session', '90 minutes session with all edited photos, a photo book, and a canvas print.', 500.00);

INSERT INTO AddOn (addOn_id, addOn, price) VALUES
('AO001', 'Extra Edited Photos', 0.00),
('AO002', 'Printed Album', 0.00);

INSERT INTO Photographer (photographer_id, email, password, phone, firstName, lastName, bioDescription, location, availability, rating) VALUES
('PH001', 'john.doe@example.com', 'securePassword123', '0412345678', 'John', 'Doe', 'Experienced photographer specializing in portrait and event photography.', 'Sydney', 'Weekdays', 4.8),
('PH002', 'emily.smith@example.com', 'pass1234secure', '0498765432', 'Emily', 'Smith', 'Specializing in landscape photography with a keen eye for natural light and outdoor scenes.', 'Melbourne', 'Weekdays', 4.7),
('PH003', 'michael.jones@example.com', 'mikephoto321', '0401122334', 'Michael', 'Jones', 'Freelance photographer with a focus on corporate headshots and commercial photography.', 'Brisbane', 'Short notice bookings', 4.9),
('PH004', 'sophia.wilson@example.com', 'sophiaW!23', '0455667788', 'Sophia', 'Wilson', 'Creative portrait photographer with over 10 years of experience capturing moments that tell stories.', 'Perth', 'Weekends', 5.0),
('PH005', 'david.brown@example.com', 'davidsPhoto2023', '0422333445', 'David', 'Brown', 'Experienced in wedding and engagement photography, known for capturing genuine emotions and timeless moments.', 'Adelaide', 'Weekends', 4.6),
('PH006', 'olivia.miller@example.com', 'OliviaM123!', '0433556677', 'Olivia', 'Miller', 'Family and newborn photographer dedicated to capturing the purest moments of life with warmth and elegance.', 'Gold Coast', 'Weekdays', 4.9),
('PH007', 'benjamin.taylor@example.com', 'photoBen5678', '0466778899', 'Benjamin', 'Taylor', 'Fashion and editorial photographer with a passion for capturing the latest trends and unique styles.', 'Sydney', 'Weekdays', 4.8),
('PH008', 'ava.anderson@example.com', 'Ava2023secure', '0477889900', 'Ava', 'Anderson', 'Specializes in event photography and commercial shoots, ensuring high-quality results for every project.', 'Melbourne', 'Weekends', 4.7),
('PH009', 'liam.thomas@example.com', 'LiamPhoto987', '0488992233', 'Liam', 'Thomas', 'Travel and adventure photographer who captures breathtaking landscapes and remote destinations.', 'Hobart', 'Weekdays', 4.9),
('PH010', 'chloe.davis@example.com', 'Chloe2023!Pass', '0412349876', 'Chloe', 'Davis', 'Wedding and portrait photographer with a passion for capturing candid moments and emotional stories.', 'Canberra', 'Short notice bookings', 4.8);

INSERT INTO Photographer_Service (photographerService_id, photographer_id, service_id) VALUES
('PH001S001', 'PH001', 'S001'),
('PH002S002', 'PH002', 'S002'),
('PH003S003', 'PH003', 'S003'),
('PH004S004', 'PH004', 'S004'),
('PH005S001', 'PH005', 'S001'),
('PH006S003', 'PH006', 'S003'),
('PH007S004', 'PH007', 'S004'),
('PH008S002', 'PH008', 'S002'),
('PH009S002', 'PH009', 'S002'),
('PH010S001', 'PH010', 'S001');

INSERT INTO Portfolio (portfolio_id, photographer_id) VALUES
('PF001', 'PH001'),
('PF002', 'PH002'),
('PF003', 'PH003'),
('PF004', 'PH004'),
('PF005', 'PH005'),
('PF006', 'PH006'),
('PF007', 'PH007'),
('PF008', 'PH008'),
('PF009', 'PH009'),
('PF010', 'PH010');

INSERT INTO Image (image_id, imageSource, image_description, service_id, portfolio_id) VALUES
('IMG001', 'chris-CxoEeNkJwUA-unsplash.jpg', 'Bride and groom during ceremony', 'S001', 'PF001'),
('IMG002', 'asdrubal-luna-Qxi-boLL4bs-unsplash.jpg', 'Wedding couple with family', 'S001', 'PF001'),
('IMG003', 'jay-wennington-CdK2eYhWfQ0-unsplash1.jpg', 'Golden retriever portrait', 'S002', 'PF002'),
('IMG004', 'andrew-s-ouo1hbizWwo-unsplash.jpg', 'Cat in a playful pose', 'S002', 'PF001'),
('IMG005', 'garrett-jackson-oOnJWBMlb5A-unsplash.jpg', 'Newborn baby sleeping peacefully', 'S003', 'PF001'),
('IMG006', 'hollie-santos-aUtvHsu8Uzk-unsplash.jpg', 'Parents with their newborn baby', 'S003', 'PF001'),
('IMG007', 'daniel-korpai-hbTKIbuMmBI-unsplash.jpg', 'High-end watch on display', 'S004', 'PF001'),
('IMG008', 'himani-bahati-LxVxPA1LOVM-unsplash.jpg', 'Stylish shoes for sale', 'S004', 'PF002');


INSERT INTO Cart_Service (cartService_id, service_id, cart_id, type_id, addOn_id) VALUES
('CR001S001', 'S001', 'CR001', 'T002', 'AO001'),
('CR001S004', 'S004', 'CR001', 'T001', 'AO002'),
('CR002S002', 'S002', 'CR002', 'T001', 'AO001'),
('CR003S003', 'S003', 'CR003', 'T003', 'AO002'),
('CR004S001', 'S001', 'CR004', 'T002', 'AO001'),
('CR004S002', 'S002', 'CR004', 'T001', 'AO002'),
('CR005S004', 'S004', 'CR005', 'T002', 'AO001'),
('CR006S003', 'S003', 'CR006', 'T001', 'AO001'),
('CR007S001', 'S001', 'CR007', 'T003', 'AO002'),
('CR008S002', 'S002', 'CR008', 'T002', 'AO001'),
('CR009S004', 'S004', 'CR009', 'T001', 'AO002'),
('CR010S003', 'S003', 'CR010', 'T002', 'AO001');


INSERT INTO Orders (order_id, createdDate, lastUpdated, message, paymentMethod, photographer_id, client_id) VALUES
('OR001', '2024-10-11 10:05:00', '2024-10-11 10:05:00', 'Please focus on candid shots.', 'Credit Card', 'PH001', 'C001'),
('OR002', '2024-10-12 14:20:00', '2024-10-12 14:20:00', NULL, 'PayPal', 'PH004', 'C002'),
('OR003', '2024-10-13 09:40:00', '2024-10-13 09:40:00', 'Pet shoot at the park.', 'Debit Card',  'PH002', 'C003'),
('OR004', '2024-10-14 16:10:00', '2024-10-14 16:10:00', 'Newborn session at home.', 'Bank Transfer','PH006', 'C004'),
('OR005', '2024-10-15 11:55:00', '2024-10-15 11:55:00', NULL, 'Cash', 'PH010', 'C005'),
('OR006', '2024-10-16 18:30:00', '2024-10-16 18:30:00', 'Need product white background.',  'Credit Card', 'PH007', 'C006'),
('OR007', '2024-10-17 13:05:00', '2024-10-17 13:05:00', 'Prefer golden hour.', 'Credit Card', 'PH005', 'C007'),
('OR008', '2024-10-18 08:25:00', '2024-10-18 08:25:00', NULL, 'PayPal', 'PH003', 'C008');

INSERT INTO Order_Service (orderService_id, service_id, order_id) VALUES
('OR001S001', 'S001', 'OR001'),  
('OR001S004', 'S004', 'OR001'),  
('OR002S001', 'S001', 'OR002'),
('OR003S002', 'S002', 'OR003'),
('OR004S003', 'S003', 'OR004'),
('OR005S001', 'S001', 'OR005'),
('OR006S004', 'S004', 'OR006'),
('OR007S001', 'S001', 'OR007'),
('OR007S002', 'S002', 'OR007'), 
('OR008S003', 'S003', 'OR008');
