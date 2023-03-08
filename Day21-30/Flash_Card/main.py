# Day 31 - Flash Card App

from tkinter import PhotoImage, Tk, Canvas, Button
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

# Grab data from csv
try:
    word_df = pd.read_csv('Data/words_to_learn.csv')
except FileNotFoundError:
    word_df = pd.read_csv('Data/spanish_words.csv')
finally:
    to_learn = word_df.to_dict(orient='records')


# ------------------------ Generate next card ------------------------------- #

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(side, image=card_front)
    flash_card.itemconfig(card_title, text="Spanish", fill='black')
    flash_card.itemconfig(
        card_word,
        text=current_card["Spanish"],
        fill='black'
    )
    timer = window.after(3000, flip_card)


# -------------------------- Flip Card  ------------------------------------- #

def flip_card():
    flash_card.itemconfig(side, image=card_back)
    flash_card.itemconfig(card_title, text="English", fill='white')
    flash_card.itemconfig(
        card_word,
        text=current_card["English"],
        fill='white'
    )


# -------------------------- Remove Known Words ----------------------------- #

def remove_word():
    to_learn.remove(current_card)
    new_word_df = pd.DataFrame(to_learn)
    new_word_df.to_csv('Data/words_to_learn.csv', index=False)
    next_card()


# -------------------------- User Interface --------------------------------- #

window = Tk()
window.title('Flashy')
window.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOR
)

timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file='Images/card_back.png')
card_front = PhotoImage(file='Images/card_front.png')
right_img = PhotoImage(file='Images/right.png')
wrong_img = PhotoImage(file='Images/wrong.png')

flash_card = Canvas(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)
side = flash_card.create_image(400, 263, image=card_front)
card_title = flash_card.create_text(400, 150, text='', font=LANG_FONT)
card_word = flash_card.create_text(400, 263, text='', font=WORD_FONT)
flash_card.grid(row=0, column=0, columnspan=2)

x_button = Button(
    image=wrong_img,
    borderwidth=0,
    highlightthickness=0,
    command=next_card
)
x_button.grid(row=1, column=0)

check_button = Button(
    image=right_img,
    borderwidth=0,
    highlightthickness=0,
    command=remove_word
)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()
