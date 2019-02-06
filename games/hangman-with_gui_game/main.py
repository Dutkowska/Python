from tkinter import *
from menu import make_menu
from window_gui2 import window_view

window_box = Tk()
window_box.title("Hangman")

make_menu(window_box)
window_view()

window_box.mainloop()