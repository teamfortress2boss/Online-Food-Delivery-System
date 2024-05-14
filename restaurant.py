import tkinter as tk
import sqlite3
from menuitems import MenuItemsPage

class RestaurantPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.beige = "#ecc884"
        self.font = ("Calibre", 20)
        self.text = "Choose your favorite restaurant"
        self.name_lb = tk.Label(self, text=self.text, font=self.font, bg=self.beige)
        self.name_lb.grid(column=2, row=1)

        self.checked_state_SL = tk.IntVar()
        self.secretlarrys = tk.Checkbutton(master=self, text="Secret Larry's", variable=self.checked_state_SL,
                                           font=self.font, bg="#ecc884")
        self.secretlarrys.grid(column=2, row=2, sticky="w")

        self.checked_state_CS = tk.IntVar()
        self.crabshack = tk.Checkbutton(master=self, text="The Crab Shack", variable=self.checked_state_CS,
                                        font=self.font, bg="#ecc884")
        self.crabshack.grid(column=2, row=3, sticky="w")

        self.checked_state_RE = tk.IntVar()
        self.riverside = tk.Checkbutton(master=self, text="Riverside Eatery", variable=self.checked_state_RE,
                                           font=self.font, bg="#ecc884")
        self.riverside.grid(column=2, row=4, sticky="w")

        self.checked_state_FH = tk.IntVar()
        self.thefreehouse = tk.Checkbutton(master=self, text="The Free House", variable= self.checked_state_FH,
                                           font=self.font, bg="#ecc884")
        self.thefreehouse.grid(column=2, row=5, sticky="w")

        self.checked_state_CG = tk.IntVar()
        self.capitalgrill = tk.Checkbutton(master=self, text="The Capital Grill", variable=self.checked_state_CG,
                                           font=self.font, bg="#ecc884")
        self.capitalgrill.grid(column=2, row=6, sticky="w")

        self.next_button = tk.Button(self, width=20, text="Next", font=self.font, command=self.choose_restaurant)
        self.next_button.grid(column=3, row=7)

    def choose_restaurant(self):
        restaurants = ['Secret Larrys', 'The Crab Shack', 'Riverside Eatery', 'The Freehouse', 'The Capital Grille']
        on_off = [self.checked_state_SL.get(), self.checked_state_CS.get(), self.checked_state_RE.get(),
              self.checked_state_FH.get(), self.checked_state_CG.get()]
        chosen = []
        for i in range(0, 5):
            if on_off[i] == 1:
                chosen.append(restaurants[i])

        placeholders = ",".join("?" for _ in chosen)
        connection = sqlite3.connect("MustangsEat.db")
        my_cursor = connection.cursor()
        query = """ SELECT M.itemName, M.price, M.rating
                    FROM menuitems M
                    INNER JOIN restaurant AS R ON R.restID = M.restID
                    WHERE R.name IN  ({});"""

        my_cursor.execute(query.format(placeholders), chosen)
        all_items = my_cursor.fetchall()
        print(all_items)

        self.destroy()
        menuitems_page = MenuItemsPage(self.master, width=600, height=800, bg="#ecc884")
        menuitems_page.place(x=100, y=250)
        menuitems_page.create_widgets(all_items)
