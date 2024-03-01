from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"

# Load the CSV data
data = pd.read_csv('./data/french_words.csv')
to_learn = data.to_dict(orient='records')
current_card = {}


# -------------------- NEXT CARD -------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    language = data.columns[0]  # French
    # Pick a random word from the selected language: French
    current_card = rd.choice(to_learn)
    word = current_card[language]
    # Update card widget
    canvas.itemconfig(card_language, text=language, fill='black')
    canvas.itemconfig(card_word, text=word, fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    # Flip card
    flip_timer = window.after(3000, func=flip_card)

# -------------------- FLIP CARD -------------------
def flip_card():
    language = data.columns[1]  # English
    word = current_card[language]

    # Update card widget
    canvas.itemconfig(card_language, text=language, fill='white')
    canvas.itemconfig(card_word, text=word, fill='white')
    # Change color
    canvas.itemconfig(card_background, image=card_back_img)

# -------------------- UI SETUP --------------------

# Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Load images
check_img = PhotoImage(file='./images/right.png')
cross_img = PhotoImage(file='./images/wrong.png')
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')

# Widgets

# Create a card widget
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# Add image to canvas
card_background = canvas.create_image(400, 263, image=card_front_img)
# Add text to canvas
card_language = canvas.create_text(400, 150, text='', fill='black', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', fill='black', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Add buttons
unknown_button = Button(image=cross_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)  # Red button
known_button = Button(image=check_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
known_button.grid(row=1, column=1)  # Green button

# Pick a random card
next_card()


window.mainloop()
