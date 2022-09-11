from tkinter import *
import pandas as pd
import random
import time

currentCard = {}
toLearn = {}

try:
    wordList = pd.read_csv('data/words_to_learn.csv')
    
except FileNotFoundError:
    originalData = pd.read_csv('data/french_words.csv')
    toLearn = originalData.to_dict(orient="records")

else:
    toLearn = wordList.to_dict(orient="records")
    

def setEnglishCard():

    canvas.itemconfig(cardBackground, image=card_back_img)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=currentCard["English"])
    

def nextWord():

    global currentCard
    canvas.itemconfig(cardBackground, image=card_front_img)
    canvas.itemconfig(title, text="French")
    currentCard = random.choice(toLearn)
    canvas.itemconfig(word, text=currentCard["French"])

    root.after(3000, func=setEnglishCard)

def isKnown():
    
    print(currentCard)

    toLearn.remove(currentCard)
    data = pd.DataFrame(toLearn)
    data.to_csv("data/words_to_learn.csv", index="false")
    nextWord()


root= Tk()

BACKGROUND_COLOR = "#B1DDC6"
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file='images/card_back.png')
cardBackground = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, 'italic'), fill='#000000')
word = canvas.create_text(400, 300, text="word", font=("Ariel", 60, 'bold'), fill='#000000')

check_button_image = PhotoImage(file="images/right.png")
checkButton = Button(image=check_button_image, command=isKnown)
checkButton.grid(column=0, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrongButton = Button(image=wrong_button_image, command=nextWord)
wrongButton.grid(column=1, row=1)

nextWord()



    


root.mainloop()