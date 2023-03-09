from tkinter import *
import pandas
import random

SECS = 3
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------Translate----------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    print(data_dict)
else:
    data_dict = data.to_dict(orient="records")
    print(data_dict)

current_dict = {}


def card():
    global current_dict, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_img)
    current_dict = random.choice(data_dict)
    canvas.itemconfig(title, text="French", fill="Black")
    canvas.itemconfig(cards, text=current_dict["French"], fill="Black")
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(cards, text=current_dict["English"], fill="white")


def is_know():
    data_dict.remove(current_dict)
    data_remain = pandas.DataFrame(data_dict)
    data_remain.to_csv("./data/words_to_learn.csv", index=False)
    card()


window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(410, 255, image=card_front_img)
cards = canvas.create_text(410, 255, text="Word", fill="Black", font=("Courier", 45, "bold"))
title = canvas.create_text(410, 144, text="Title", fill="Black", font=("Courier", 25, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

my_image = PhotoImage(file="images/right.png")
known_button = Button(image=my_image, highlightthickness=0, command=is_know)
known_button.grid(row=1, column=0, pady=10, padx=10)

my_image_1 = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=my_image_1, highlightthickness=0, command=card)
unknown_button.grid(row=1, column=1)

card()

window.mainloop()
