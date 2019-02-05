import random

def start():
    name=input("Write your name: ")
    print("Hello ", name, " let's start a game!")
    print("Your word has length: ", len(word))
    for char in word: guess.append('_')
    print(*guess)
def game():
    position=word.index(char)
    if char in good: #what if we have word "loop" and the second "o"
        for j in range(len(word)):
            if word[j]==char and j!=position:
                position=j
                break
    good.append(char)
    guess[position]=char
    print(*guess)
    if(stay==0): 
        print("Good! It was your last chance.")
    else:
        print(message.format(beg="Good.", num=stay))
def end():
    print("Wrong answers: ", wrong, " times. ")
    print("Correct answers: ", repeat-wrong, " times. ")
    print("Your word: ", *guess)
    try_word=input("Try to write word. ")
    if try_word==word: print("Good!")
    else: print("Wrong, right word: ", word)

# ---- variables ----
wrong=0 #num of incorrect answers
good=[] #only good chars
write=[] #all chars
guess=[] #to write sth like: _ _ a _ _ b
turn=0
words=['hangman', 'input', 'name', 'hello', 'loop', 'dog', 'cat']
word=random.choice(words)
message="{beg} Try again, you still have {num} chance(s). Enter 'stop' to stop."


start()
while True:
    try: 
        repeat=int(input("How many attempts do you want? "))
        print("You have ", repeat, " chances. Good luck! Write a character or 'stop' to stop: ")
        break
    except ValueError:
        print("Your number is not a numeric data. Try again.")

while turn<repeat:
    stay=repeat-turn-1
    char=input()
    if char=='stop':
        break
    elif len(char)>1:
        turn-=1
        print(message.format(beg="Write only 1 character.", num=stay+1))
    elif char.isdigit(): 
        turn-=1
        print(message.format(beg="Write a character, not numerical data.", num=stay+1))
    elif char in write and write.count(char)==word.count(char):# loop - second 'o' is ok, third not.
        turn-=1
        print(message.format(beg="You have already written that letter!", num=stay+1))
    else:
        if char not in word:
            wrong+=1
            if(stay==0): 
                print("It was your last chance.")
                break
            print(message.format(beg="Wrong.", num=stay))
        else:
            game()
    write.append(char)
    turn+=1
end()