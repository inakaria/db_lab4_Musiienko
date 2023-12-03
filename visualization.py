import psycopg2
import matplotlib.pyplot as plt

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
    customers = []
    total = []

    for row in cur:
        customers.append(row[0])
        total.append(row[1])

    x_range = range(len(customers))
 
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, total, label='Total')
    bar_ax.bar_label(bar, label_type='center')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(customers)
    bar_ax.set_xlabel('Покупці')
    bar_ax.set_ylabel('Сума, $')
    bar_ax.set_title('Загальна сума, на яку покупці зробили замовлення')

    cur.execute(query_2) # Percentage of using each card type for payment, except mastercard
    card_type = []
    card_count = []

    for row in cur:
        card_type.append(row[0])
        card_count.append(row[1])

    pie_ax.pie(card_count, labels=card_type, autopct='%1.1f%%')
    pie_ax.set_title('Частка замовлень через кожен вид платежу, окрім mastercard')

    cur.execute(query_3) # Dependency between year of manufacture and price of cars
    year = []
    item_price = []

    for row in cur:
        year.append(row[0])
        item_price.append(row[1])

    mark_color = 'blue'
    graph_ax.plot(year, item_price, color=mark_color, marker='o')

    for qnt, price in zip(year, item_price):
        graph_ax.annotate(price, xy=(qnt, price), color=mark_color,
                          xytext=(7, 2), textcoords='offset points')    

    graph_ax.set_xlabel('Рік')
    graph_ax.set_ylabel('Ціна')
    graph_ax.set_title('Графік залежності ціни від року виготовлення автомобіля')


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()
