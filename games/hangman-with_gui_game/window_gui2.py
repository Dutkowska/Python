from functions import *

def window_view():
    okn = PanedWindow(orient=VERTICAL, bg="brown")
    okn.pack(fill=BOTH, expand=1)
    # okn - window, gi - vertical panel,
    # li/ri - horizontal parts of vertical panels (left/right)

# hello pos ----
    hello = "Good morning.\nYou are in the simple version of:\n Hangman game \n___________________________________________"
    g_hello = Label(okn, text=hello, justify=LEFT, bg="wheat")
    okn.add(g_hello)

# g1 pos ----
    g1 = PanedWindow(orient=HORIZONTAL, bg="wheat")
    okn.add(g1)

# g1 pos ++-- (left)
    l1 = PanedWindow(orient=VERTICAL, bg="wheat")
    g1.add(l1)

    l_sex = Label(l1, text="Your sex: ", justify=RIGHT, bg="wheat")
    l1.add(l_sex)

    l_name = Label(l1, text="Write your name: ", justify=RIGHT, bg="wheat")
    l1.add(l_name)

# g1 pos --++ (right)
    right = PanedWindow(orient=VERTICAL, bg="brown")
    g1.add(right)

    r1 = Menubutton(right, text="Select", relief=RAISED, bg="tan")
    r1.grid()
    r1.menu = Menu(r1)
    r1["menu"] = r1.menu

    fem = IntVar()
    mal = IntVar()

    r1.menu.add_checkbutton(label="female", variable=fem)
    r1.menu.add_checkbutton(label="male", variable=mal)
    r1.pack()
    right.add(r1)

# g1 position --++ (right)
    name = StringVar()
    r_name = Entry(right, bd=5, textvariable=name)
    right.add(r_name)

    word=''
    def start_ok():
        #TODO: make word only before that
        word=change_word()
        if mal.get():
            gm = "Good morning Mr " + str(name.get())
            g_welcome.config(text=gm)
        if fem.get():
            gm = "Good morning Mrs " + str(name.get())
            g_welcome.config(text=gm)
        else:
            gm="Select your sex & write name."
            g_welcome.config(text=gm)

# g_start position ----
    g_start = Button(okn, text="OK", command=start_ok, bg="tan")
    okn.add(g_start)

# g_welcome position ----
    g_welcome = Label(okn, bg="wheat")
    okn.add(g_welcome)

#TODO: rechange this _ _ _ with good letters
    for char in word: guess.append('_ ')
    info="Your word has length: {} \n{}"

# g_guess position ----
    g_guess = Label(okn, text=info.format(len(word), "".join(guess)), justify=LEFT, bg="wheat")
    okn.add(g_guess)

# g_write position ----
    g_write = PanedWindow(orient=HORIZONTAL)
    okn.add(g_write)

# g_write position ++-- (left)
    left2 = PanedWindow(orient=VERTICAL)
    g_write.add(left2)

    l3 = Label(left2, text="Write your letter: ", justify=RIGHT, bg="wheat")
    left2.add(l3)

# g_write position --++ (right)
    right2 = PanedWindow(orient=VERTICAL, bg="wheat")
    g_write.add(right2)

    r3 = Entry(right2, bd=5)
    right2.add(r3)

# g_check position ----
    g_check = Button(okn, text="OK", command=game, bg="tan")
    okn.add(g_check)
