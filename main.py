from tkinter import *
import pandas
from random import choice

# ------------------------- CONSTANTS -------------------------#
BACKGROUND_COLOR = "#B1DDC6"
INITIAL_CSV_FILE = "data/french_words.csv"
WORDS_TO_LEARN= "data/words_to_learn.csv"


# ---------------------------- FUNCTIONALITY------------------------------- #
to_learn = {}
chosen_item = {}

try:
    words_file = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    original_words_file = pandas.read_csv(INITIAL_CSV_FILE)
    to_learn = original_words_file.to_dict(orient="records")
else:
    to_learn = words_file.to_dict(orient="records")



def pick_a_word():
    global chosen_item, flip_timer
    chosen_item = choice(to_learn)
    window.after_cancel(flip_timer)
    chosen_word = chosen_item['French']
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{chosen_word}", fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{chosen_item['English']}", fill="white")


def is_known():
    to_learn.remove(chosen_item)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    pick_a_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text=f"", font=("Courier", 32, "italic"))
card_word = canvas.create_text(400, 263, text=f"", font=("Courier", 48, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=pick_a_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

pick_a_word()

window.mainloop()
