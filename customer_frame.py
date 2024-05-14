import tkinter as tk
import sqlite3
from restaurant import RestaurantPage


class CustomerPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.beige = "#ecc884"
        self.font = ("Calibre", 15)

        self.name_lb = tk.Label(self, text=" First Name", font=self.font, bg=self.beige)
        self.name_lb.grid(column=1, row=2, sticky="w")
        self.name_entered = tk.StringVar(self)
        self.name_entry = tk.Entry(self, width=50)
        self.name_entry.grid(column=2, row=2, padx=20, pady=20)

        self.lastname_lb = tk.Label(self, text="Last Name", font=self.font, bg=self.beige)
        self.lastname_lb.grid(column=1, row=3, sticky="w")
        self.lastname_entry = tk.Entry(self, width=50)
        self.lastname_entry.grid(column=2, row=3, padx=20, pady=20)

        self.street_address_lb = tk.Label(self, text="Address", font=self.font, bg=self.beige)
        self.street_address_lb.grid(column=1, row=4, sticky="w")
        self.street_address_entry = tk.Entry(self, width=50)
        self.street_address_entry.grid(column=2, row=4, padx=20, pady=20)

        self.apt_no_lb = tk.Label(self, text="Apt No.", font=self.font, bg=self.beige)
        self.apt_no_lb.grid(column=3, row=4, sticky="w")
        self.apt_no_entry = tk.Entry(self, width=20)
        self.apt_no_entry.grid(column=4, row=4, padx=20, pady=20)

        self.city_lb = tk.Label(self, text="City", font=self.font, bg=self.beige)
        self.city_lb.grid(column=1, row=5, sticky="w")
        self.city_entry = tk.Entry(self, width=50)
        self.city_entry.grid(column=2, row=5, padx=20, pady=20)

        self.zip_lb = tk.Label(self, text="ZIP", font=self.font, bg=self.beige)
        self.zip_lb.grid(column=3, row=5, sticky="w")
        self.zip_entry = tk.Entry(self, width=20)
        self.zip_entry.grid(column=4, row=5, padx=20, pady=20)

        self.state_lb = tk.Label(self, text="State", font=self.font, bg=self.beige)
        self.state_lb.grid(column=3, row=6, padx=20, pady=20, sticky="w")
        self.us_states = [
            'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID',
            'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
            'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
            'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV',
            'WI', 'WY'
        ]
        self.selected_state = tk.StringVar(self)
        self.selected_state.set(self.us_states[0])
        self.state_option_menu = tk.OptionMenu(self, self.selected_state, *self.us_states)
        self.state_option_menu.grid(column=4, row=6, padx=20, pady=20)

        self.phone_lb = tk.Label(self, text="Phone Number", font=self.font, bg=self.beige)
        self.phone_lb.grid(column=1, row=6, sticky="w")
        self.phone_entry = tk.Entry(self, width=50)
        self.phone_entry.grid(column=2, row=6, padx=20, pady=20)

        self.email_lb = tk.Label(self, text="Email", font=self.font, bg=self.beige)
        self.email_lb.grid(column=1, row=7, sticky="w")
        self.email_entry = tk.Entry(self, width=50)
        self.email_entry.grid(column=2, row=7, padx=20, pady=20)

        self.next_button = tk.Button(self, width=20, text="Next",font=self.font, command=self.insert_custumer)
        self.next_button.grid(column=4, row=8)


    def insert_custumer(self):

        connection = sqlite3.connect("MustangsEat.db")
        my_cursor = connection.cursor()
        query = """INSERT INTO customer(firstname, lastname, address, apartmentnum, zipcode, city, state, phone, email)
                                        VALUES(?,?,?,?,?,?,?,?,?);"""
        customer_inputs = (self.name_entry.get(), self.lastname_entry.get(), self.street_address_entry.get(),
                    self.apt_no_entry.get(), self.zip_entry.get(), self.city_entry.get(), self.selected_state.get(),
                    self.phone_entry.get(), self.email_entry.get())
        my_cursor.execute(query, customer_inputs)
        connection.commit()
        print(customer_inputs)
        self.destroy()
        restaurant_page = RestaurantPage(self.master, width=600, height=800, bg="#ecc884")
        restaurant_page.place(x=100, y=250)

    # def get_cust_info(self):
    #     return self.name_entry.get(), self.lastname_entry.get(), self.street_address_entry.get(), self.apt_no_entry.get()






