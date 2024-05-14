import sqlite3
final_selections = ['Pan Seared Yellowfin Tuna Loin', 'Alpine Kreuter Butter Steak']
connection = sqlite3.connect("MustangsEat.db")
my_cursor = connection.cursor()
query = """ SELECT firstname, lastname, address, apartmentnum
            FROM customer
            WHERE custID = (SELECT MAX(custID) FROM customer);"""
placeholders = ",".join(["?" for _ in final_selections])
print(placeholders)
my_cursor.execute(query.format(placeholders), final_selections)
cust_info = my_cursor.fetchall()
print(cust_info)

