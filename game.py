import os.path
from tkinter.ttk import *
from tkinter import *
import random
import os, sys

win = Tk()
win.title("Guess The Number")
win.geometry("300x310")

win.configure(background="#261E36")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def close_app():
    win.destroy()


def randomize():
    global a
    e.config(state="normal")
    difficulty = choice.get()
    if difficulty == 1:
        a = random.randint(0, 50)
    elif difficulty == 2:
        a = random.randint(0, 100)
    elif difficulty == 3:
        a = random.randint(0, 500)
    print(a)


def check(event): # sunartisi pou exei bind se koumpi PANTA vazoume event mesa stis parentheseis
    global tries
    guess = e.get() # tou sumperiferetai san KEIMENO
    if int(guess) == a:
        imglbl.config(image=correct)
    elif int(guess) > a:
        imglbl.config(image=down)
    elif int(guess) < a:
        imglbl.config(image=up)
    tries += 1
    trieslbl.config(text="Tries: "+str(tries))
    e.delete(0, END)


tries = 0
up = PhotoImage(file=resource_path("uparrow.png"))
down = PhotoImage(file=resource_path("downarrow.png"))
correct = PhotoImage(file=resource_path("correct.png"))
dice = PhotoImage(file=resource_path("dice.png"))

title = Label(win, text="Guess the number",background="#261E36", foreground = "white")
title.grid(row=0, column=0, columnspan=3)

choice = IntVar() # metavliti poy tha pairnei akeraious arithmous

rb1 = Radiobutton(win, text="Easy (0-50)", background="#261E36", foreground = "white",value=1, variable=choice)
rb2 = Radiobutton(win, text="Normal (0-100)",background="#261E36", foreground = "white", value=2, variable=choice)
rb3 = Radiobutton(win, text="Hard (0-500)",background="#261E36", foreground = "white", value=3, variable=choice)

rb1.grid(row=1,column=0)
rb2.grid(row=1,column=1)
rb3.grid(row=1,column=2)

instructions = Label(win, text="In this Game you will try to find a secret  number"
                                 "\nthat is randomly chosen every round"
                                 "\nTry to guess it with the least possible tries!",background="#261E36", foreground = "white")
instructions.grid(row=2, column=0, columnspan=3)

imglbl = Label(win, image=correct, background="#261E36")
imglbl.grid(row=3, column=0, rowspan=2)

e = Entry(win, state="disabled")
e.grid(row=3,column=1)

trieslbl = Label(win, text="Tries:0",background="#261E36", foreground = "white")
trieslbl.grid(row=4, column=1)

ebtn = Button(win, text="Exit",background="#261E36", foreground = "white", command=close_app)
rbtn = Button(win, text="Randomize",background="#261E36", foreground = "white", command=randomize)
ebtn.grid(row=3, column=2)
rbtn.grid(row=4, column=2)

win.bind('<Return>', check)

win.mainloop()