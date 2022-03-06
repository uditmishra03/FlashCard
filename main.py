from tkinter import *

# ------------------------- CONSTANTS -------------------------#
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR )

# Canvas
canvas = Canvas(width=800, height=526 , bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1,column=1)


window.mainloop()