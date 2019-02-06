from tkinter import *
from tkinter import messagebox
import random

def creator():
    messagebox.showinfo("Twórca", "Program jest dziełem PD.")

def about():
    window_box2 = Tk()
    window_box2.title("About")
    text = Text(window_box2)
    text.insert(INSERT, "App info")
    text.pack()
    window_box2.mainloop()


def problem():
    messagebox.showerror("Error", "I cannot do this!")

# for hangman:
# ---- variables ----
wrong=0 #num of incorrect answers
good=[] #only good chars
write=[] #all chars
guess=[] #to write sth like: _ _ a _ _ b
turn=0
words=['hangman', 'input', 'name', 'hello', 'loop', 'dog', 'cat']
#word=random.choice(words)
message="{beg} Try again, you still have {num} chance(s). Enter 'stop' to stop."

def change_word():
    #TODO: do this function - with start_word and before entering right chars
    return random.choice(words)

def game():
    pass

def end():
    pass