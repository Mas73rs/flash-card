from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# -------------------- UI SETUP --------------------

# Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Load images
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')

# Widgets

# Create a card widget
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# Add image to canvas
canvas.create_image(400, 263, image=card_front_img)
# Add text to canvas
canvas.create_text(400, 150, text='Language', fill='black', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='word', fill='black', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Add buttons
wrong_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0) # Red button
right_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=1) # Green button



window.mainloop()