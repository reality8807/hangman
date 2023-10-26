from tkinter import *
import requests

# Random Word from an API
url = 'https://random-word-api.herokuapp.com/word'
data = requests.get(url).json()[0]
word = data.upper()

# Creating Blanks
guess = []
for _ in word:
    guess.append("_")

# Creating the window
root = Tk()
root.title("Hangman")
root.geometry("1000x400")
root.resizable(width=False, height=False)

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lives = 0

# Widgets
letter_frame = Frame(root)
letter_frame.grid(row=1, column=1, padx=25, pady=25)

display_word = Label(root, text=guess, font=("Times", 30, "bold"))
display_word.grid(row=0, column=1, padx=25, pady=25)

display_img = PhotoImage(file="images/hang.png")
display_image = Label(root, image=display_img)
display_image.grid(row=0, column=0, rowspan=2, padx=25, pady=25)

# Loading Images
images = []
for i in range(1, 8):
    img = PhotoImage(file=f"images/hang{i}.png")
    images.append(img)


def create_letters(text, but_click, row, col):
    button = Button(letter_frame, width=4, height=2, text=text, font=("System", 16, "bold"))
    button.config(command=lambda b=button: but_click(b))
    button.grid(row=row, column=col)


def letter_click(b):
    global lives

    b.config(state="disabled")

    letter = b["text"]
    if letter not in word:
        wrong_guess(b)
    else:
        correct_guess(b, letter)

    game_over()


# Creating Letter Buttons
r = 0
c = 0
for i, _ in enumerate(LETTERS, 0):
    create_letters(LETTERS[i], letter_click, r, c)
    c += 1
    if i == 12:
        r = 1
        c = 0


def correct_guess(b, letter):
    b.config(bg="#00e300")

    start_pos = 0
    for let in word:
        if letter == let:
            pos = word.find(letter, start_pos)
            guess[pos] = letter
            start_pos = pos + 1

    display_word.config(text=guess)


def wrong_guess(b):
    global lives

    Label(root, image=images[lives]).grid(row=0, column=0, rowspan=2, padx=25, pady=25)
    lives += 1
    b.config(bg="#c40000")


def game_over():
    global lives

    # Lose
    if lives == 7:
        Label(root, text="You Lose!", font=("Courier New", 20, "bold")).grid(row=2, column=0, columnspan=2, pady=25)
        disable_buttons()

    # Win
    elif display_word["text"].replace(" ", "") == word:
        Label(root, text="You Win!", font=("Courier New", 20, "bold")).grid(row=2, column=0, columnspan=2, pady=25)
        disable_buttons()


def disable_buttons():
    display_word.config(text=word)

    for button in letter_frame.winfo_children():
        if isinstance(button, Button):
            button.config(state="disabled")


root.mainloop()
