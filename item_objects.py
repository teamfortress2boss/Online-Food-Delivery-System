import tkinter as tk

class ItemObject():
    def __init__(self, thetuple):
        self.name = thetuple[0]
        self.rating = thetuple[2]
        self.price = thetuple[1]
        self.selection_status = None
        self.checkbox = None