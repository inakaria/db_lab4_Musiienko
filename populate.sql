INSERT INTO credit_card (routing_number, card_type)
VALUES
    ('877184214', 'mastercard'),
	('190318673', 'mastercard'),
    ('142640072', 'maestro'),
    ('497022206', 'instapayment'),
	('929967648', 'maestro');
	
INSERT INTO purchaser (purchaser_id, first_name, last_name, country, routing_number)
VALUES
    (190018806, 'Yetty', 'Arghent', 'Indonesia', '877184214'),
    (345957405, 'Crystal', 'Bosworth', 'China', '190318673'),
    (614722593, 'Monro', 'Houdhury', 'Indonesia', '142640072'),
	(867023917, 'Bowie', 'Clair', 'China', '497022206'),
	(304309590, 'Myrvyn', 'McAllister', 'Czech Republic', '929967648');
	
INSERT INTO car (car_id, brand, model, color, year_of_manufacture, price, purchaser_id)
VALUES
    ('2G2WC58C261254386', 'Ford', 'Club Wagon', 'Teal', 1993, 8990, 190018806),
    ('2T1BR12E92C507212', 'Cadillac', 'Escalade ESV', 'Fuscia', 2007, 8000, 345957405),
    ('2C4RC1BG2FR678360', 'Mazda', 'Miata MX-5', 'Orange', 2009, 7810, 614722593),
	('JH4KA96582C050366', 'Audi', 'A4', 'Orange', 2005, 7820, 867023917),
	('1YVHP84D765M07958', 'Nissan', 'Maxima', 'Pink', 1994, 5390, 304309590);