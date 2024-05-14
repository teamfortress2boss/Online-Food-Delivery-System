import tkinter as tk
from customer_frame import CustomerPage
from order_receipt import Order

BEIGE = "#ecc884"
DARKBROWN = "#482909"

main_window = tk.Tk()
main_window.title("Mustangs Eat")
main_window.geometry("1000x800")
main_window.config(pady=50, bg=BEIGE)
canvas = tk.Canvas(main_window, height=200, width=1000, bg=DARKBROWN, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(500, 100, image=logo)
canvas.place(x=0, y=20)


customer_page = CustomerPage(main_window, width=600, height=800, bg=BEIGE)
customer_page.place(x=100, y=250)














main_window.mainloop()