import random

shapes = ['r', 'p', 's']


def beginner():
    name = input("Write your name: ")
    print("Hello", name)
    while True:
        try:
            repeat = int(input("Let's start a game! Enter number of repetitions: "))
            break
        except ValueError:
            print("Your number is not a numeric data. Try again.")
    return repeat, name


def ender(name, loss, wins):
    print("---- End of the game ----")
    print("Statistics of ", name)
    print("Wins: ", wins)
    print("Lost: ", loss)
    print("Thank you for the game.")


def game(repeat):
    loss, wins = 0, 0
    i = 0
    while (i < repeat):
        shape = random.choice(shapes)
        chosen = input("Your shape - rock/paper/scissors [r/p/s]? Enter 'stop' to stop. ")
        if shape == chosen:
            print("Good! You won!")
            wins += 1
        elif chosen == "stop":
            break
        elif chosen not in shapes:
            print("Enter only ", *shapes, sep="/")
            i -= 1
        else:
            print("You lost, proper value: ", shape)
            loss += 1
        i += 1
        print("Number of chances: ", repeat - i)
    return loss, wins


repeat, name = beginner()
loss, wins = game(repeat)
ender(name, loss, wins)