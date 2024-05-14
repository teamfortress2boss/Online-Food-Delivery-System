import tkinter as tk
import sqlite3
from rating import Rating

class Order(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

    def create_widgets(self, final_selection):
        self.font = ("Calibre", 20)
        self.lg_beige = "#ffebbd"
        self.text = "This is what you've ordered"
        self.name_lb = tk.Label(self, text=self.text, font=self.font, bg=self.lg_beige)
        self.name_lb.grid(column=2, row=1)
        self.total

        canvas = tk.Canvas(self, height=600, width=800, bg=self.lg_beige, highlightthickness=0)
        canvas.place(x=0, y=0)
        connection = sqlite3.connect("MustangsEat.db")
        my_cursor = connection.cursor()

        self.name_lb = tk.Label(self, text=self.text, font=self.font, bg=self.lg_beige)
        self.name_lb.grid(column=2, row=1)
        query = """ SELECT firstname, lastname, address, apartmentnum
                    FROM customer
                    WHERE custID = (SELECT MAX(custID) FROM customer);"""

        my_cursor.execute(query)
        cust_info = my_cursor.fetchall()
        print(self.total)
        recepient_req = f"First Name:\nLast Name:\nAddress: \nApt No:"
        recepient_reqlb = tk.Label(self, text=recepient_req, font=("Calibre", 15), bg=self.lg_beige)
        recepient_reqlb.grid(column=1, row=2, sticky="")
        recepient_info = f"{cust_info[0][0]}\n{cust_info[0][1]}\n{cust_info[0][2]}\n{cust_info[0][3]}"
        recepient = tk.Label(self, text=recepient_info, font=("Calibre", 15), bg=self.lg_beige)
        recepient.grid(column=2, row=2, sticky="e")
        for i in range(0, len(final_selection)):
            item = tk.Label(self, text=final_selection[i][0], font=("Calibre", 15), bg=self.lg_beige)
            item.grid(column=1, row=i + 3, sticky="w")

            item_price = tk.Label(self, text="{:.2f}".format(final_selection[i][1]), font=("Calibre", 15, 'bold'), bg=self.lg_beige)
            item_price.grid(column=2, row=i + 3, sticky="w")
        self.items_selected = final_selection

        print(self.total)
        sub_total = "${:.2f}".format(self.total)
        delivery_fee = "${:.2f}".format(5)
        tax = "${:.2f}".format(0.15 * self.total)
        total = "${:.2f}".format(1.15 * self.total)
        fees_text = f"    Subtotal:\nDelivery fee:\n         Tax: \n       Total:"
        fee_Label = tk.Label(self, text=fees_text, font=("Calibre", 15,"bold"), bg=self.lg_beige)
        fee_Label.grid(column=1, row=len(final_selection)+4, sticky="e")

        fees_cont = f"{sub_total}\n{delivery_fee}\n{tax}\n{total}"
        fee_Label = tk.Label(self, text=fees_cont, font=("Calibre", 15), bg=self.lg_beige)
        fee_Label.grid(column=2, row=len(final_selection)+4, sticky="w")





        self.next_button = tk.Button(self, width=12, text="Place Order", font=self.font, command=self.finish)
        self.next_button.grid(column=3, row=7)

    def get_total(self, total):
        self.total = total


    def finish(self):

        self.destroy()
        ordered_items = []
        for i in range(0, len(self.items_selected)):
            if self.items_selected[i][0] in ordered_items:
                continue
            else:
                ordered_items.append(self.items_selected[i][0])

        connection = sqlite3.connect("MustangsEat.db")
        my_cursor = connection.cursor()
        query = """ SELECT R.name
                    FROM restaurant R
                    INNER JOIN menuitems AS M On M.restID=R.restID
                    WHERE M.itemName IN ({})
                    GROUP BY R.name;"""
        placeholders = ",".join(["?" for _ in ordered_items])

        my_cursor.execute(query.format(placeholders), ordered_items)
        rest_to_rate = my_cursor.fetchall()
        restaurants_to_rate = []
        for rest in range(0, len(rest_to_rate)):
            restaurants_to_rate.append(rest_to_rate[rest][0])
        print(restaurants_to_rate)



        rating = Rating(self.master, width=600, height=800, bg="#ecc884")
        rating.place(x=100, y=250)
        rating.create_widgets(restaurants_to_rate)


