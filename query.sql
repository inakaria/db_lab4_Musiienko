-- Загальна сума, на яку покупці зробили замовлення
SELECT CONCAT(LEFT(first_name, 1), '. ', last_name) AS customer, price
FROM purchaser
JOIN car using (purchaser_id)
GROUP BY customer, price;

-- Частка замовлень через кожен вид платежу, окрім mastercard
SELECT card_type, COUNT(*) as count
FROM credit_card
GROUP BY card_type
HAVING card_type <> 'mastercard';

-- Залежність ціни від року виготовлення автомобіля
SELECT year_of_manufacture, price
FROM car
ORDER BY year_of_manufacture;