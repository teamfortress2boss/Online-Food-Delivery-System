import tkinter as tk
import sqlite3
from datetime import datetime

class RestaurantRating():
    def __init__(self, restname, restrating):
        self.rest_name = restname
        self.rest_rating = restrating


class Rating(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

    def create_widgets(self, restaurants):

        self.font = ("Calibre", 15)
        self.beige = "#ecc884"
        self.text = "Please rate the restaurant."
        self.rate_lb = tk.Label(self, text=self.text, font=self.font, bg=self.beige)
        self.rate_lb.grid(column=2, row=1)



        print("BEFORE LOOP", restaurants)
        self.rating_list = []
        i_for_row = 0
        for i in range(0, len(restaurants)):

            restaurant_lb = tk.Label(self, text=restaurants[i], font=self.font, bg=self.beige)
            restaurant_lb.grid(column=1, row=3 + i, padx=20, pady=20, sticky="w")
            self.rating_options = ['1', '2', '3', '4', '5']
            selected_rating = tk.StringVar(self)
            selected_rating.set(self.rating_options[0])
            rating_option_menu = tk.OptionMenu(self, selected_rating, *self.rating_options)
            rest_object = RestaurantRating(restaurants[i], selected_rating)
            rating_option_menu.grid(column=2, row=3 + i, padx=20, pady=20)
            self.rating_list.append(rest_object)
            i_for_row += 1



        self.finish_button = tk.Button(self, width=20, text="Finish Rating", font=self.font, command=self.update_rating)
        self.finish_button.grid(column=3, row=4 + i_for_row, padx=20, pady=20)

    def update_rating(self):


        connection = sqlite3.connect("MustangsEat.db")
        my_cursor = connection.cursor()
        rest_ids_query = """SELECT restID
                      FROM restaurant
                      WHERE name IN ({});"""
        placeholders = ",".join(["?" for _ in self.rating_list])

        my_cursor.execute(rest_ids_query.format(placeholders), [obj.rest_name for obj in self.rating_list])
        rest_ids = my_cursor.fetchall()
        restid_rating = []
        for j in range(0, len(rest_ids)):
            restid_rating.append((rest_ids[j][0], self.rating_list[j].rest_rating.get()))
        print("Restaurant Id's", restid_rating)

        query = """SELECT MAX(custid)
                   FROM customer;"""
        my_cursor.execute(query)
        cust_info = my_cursor.fetchall()[0][0]
        print("CUSTOMER ID IS ", cust_info)
        print("WHAT IS BEING INSERTED", cust_info, restid_rating[j][0], restid_rating[j][1])
        for i in range(0, len(restid_rating)):
            insert_query = """INSERT INTO rating
                              VALUES(?,?,?,?)
                              ;"""
            my_cursor.execute(insert_query, (cust_info, restid_rating[i][0], datetime.utcnow(),restid_rating[i][1]))
            connection.commit()
        self.master.destroy()