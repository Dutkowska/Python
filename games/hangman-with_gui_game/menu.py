from functions import *

def make_menu(window_box):
    menup = Menu(window_box)


    pmenu = Menu(menup, tearoff=0)

    submenu = Menu(pmenu)
    # TODO: change_word
    submenu.add_command(label="Refresh", command=change_word)
    submenu.add_command(label="New one", command=problem)
    pmenu.add_cascade(label="Game", menu=submenu, underline=0)

    pmenu.add_separator()

    pmenu.add_command(label="Exit", command=window_box.destroy)
    menup.add_cascade(label="File", menu=pmenu)

    hmenu = Menu(menup, tearoff=0)
    hmenu.add_command(label="About", command=about)
    hmenu.add_command(label="Creator", command=creator)
    menup.add_cascade(label="Help", menu=hmenu)

    # menu from mouse
    def sMenu(poz):
        myszmenu.post(poz.x_root, poz.y_root)

    myszmenu = Menu(window_box, tearoff=0)
    myszmenu.add_command(label="Exit", command=window_box.destroy)
    window_box.bind("<Button-3>", sMenu)

    window_box.config(menu=menup)
