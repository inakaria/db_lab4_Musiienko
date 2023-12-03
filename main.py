import psycopg2

username = 'postgres'
password = 'undrugcat10'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT CONCAT(LEFT(first_name, 1), '. ', last_name) AS customer, price
FROM purchaser
JOIN car using (purchaser_id)
GROUP BY customer, price;
'''
query_2 = '''
SELECT card_type, COUNT(*) as count
FROM credit_card
GROUP BY card_type
HAVING card_type <> 'mastercard';
'''
query_3 = '''
SELECT year_of_manufacture, price
FROM car
ORDER BY year_of_manufacture;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()

    cur.execute(query_1) # How much each customer paid

    for row in cur:
        print(f'Замовник {row[0]}: ${row[1]}')

    cur.execute(query_2) # Percentage of using each card type for payment, except mastercard

    for row in cur:
        print(f'Тип картки {row[0]}: {row[1]}')

    cur.execute(query_3) # Dependency between year of manufacture and price of cars

    for row in cur:
        print(f'Рік {row[0]}: ${row[1]}')
