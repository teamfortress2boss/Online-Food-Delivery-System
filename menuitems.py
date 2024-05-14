import tkinter as tk
import sqlite3
from item_objects import ItemObject
from order_receipt import Order

class MenuItemsPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

    def create_widgets(self, menu_items):
        self.menu_items = menu_items
        self.font = ("Calibre", 15)
        self.beige = "#ecc884"
        self.text = "Choose your favorite dish"
        self.name_lb = tk.Label(self, text=self.text, font=self.font, bg=self.beige)
        self.name_lb.grid(column=2, row=1)

        name = tk.Label(self, text="Item Name", font=("Calibre", 15, 'bold'), bg=self.beige)
        name.grid(column=1, row=2, sticky="w")
        rating = tk.Label(self, text="Rating", font=("Calibre", 15, 'bold'), bg=self.beige)
        rating.grid(column=2, row=2)
        price = tk.Label(self, text="Price", font=("Calibre", 15, 'bold'), bg=self.beige)
        price.grid(column=3, row=2, sticky="w")

        self.all_selections = {}
        for item in range(0, len(self.menu_items)):
            selected_item = ItemObject(self.menu_items[item])
            selected_item.selection_status = tk.IntVar()
            selected_item.checkbox = tk.Checkbutton(master=self, text=self.menu_items[item][0],
                                               variable=selected_item.selection_status, font=self.font, bg="#ecc884")
            selected_item.checkbox.grid(column=1, row=item+3, sticky="w")
            self.all_selections[item] = selected_item.selection_status
            rating = tk.Label(self, text=selected_item.rating*"⭐", font=self.font, bg=self.beige)
            rating.grid(column=2, row=item+3)
            price = tk.Label(self, text="${:.2f}".format(selected_item.price), font=self.font, bg=self.beige)
            price.grid(column=3, row=item+3, sticky="w")

        print(self.all_selections)

        self.next_button = tk.Button(self, width=20, text="Add to Cart", font=self.font, command=self.choose_meal)
        self.next_button.grid(column=3, row=len(self.menu_items) + 3)

    def choose_meal(self):
        self.final_selections = []
        for i in range(0, len(self.menu_items)):
            if self.all_selections[i].get() == 1:
                self.final_selections.append(self.menu_items[i])
        print(self.final_selections)

        connection = sqlite3.connect("MustangsEat.db")
        my_cursor = connection.cursor()
        query = """ SELECT SUM(price)
                    FROM menuitems 
                    WHERE itemName IN ({});"""
        placeholders = ",".join(["?" for _ in self.final_selections])
        my_cursor.execute(query.format(placeholders), [self.final_selections[i][0] for i in range(0, len(self.final_selections))])
        total = my_cursor.fetchall()[0][0]
        print(total)
        self.destroy()
        order = Order(self.master, width=600, height=800, bg="#ecc884")
        order.get_total(total)
        order.create_widgets(self.final_selections)
        order.place(x=100, y=250)