from tkinter import *

# ------------------------- CONSTANTS -------------------------#
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, )

# Canvas
canvas = Canvas(width=800, height=526,)
card_front = PhotoImage(file="images/card_front.png")
# card_back = PhotoImage(file="images/card_back.png.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=1)
# canvas.pack()
window.mainloop()