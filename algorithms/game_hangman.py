import random
words=['hangman', 'input', 'name', 'hello']
word=random.choice(words)
print("Your word has length: ", len(word), ". Try to guess its, write a letter: ")
wrong=0
good=[]
for i in range(4):
    char=input()
    if len(char)>1:
        print("Write only 1 character! You missed that one, try another.")
    else: 
        if char not in word:
            wrong+=1
            print("Wrong! You have still have ", i, " chance(s).")
        else:
            good.append(char)
            print("Good!")
print("You were wrong ", wrong, " times. ")
good.sort()
print("Your letter from ", len(word), "- length word:")
for x in good: print(x)
try_word=input("Try to write word!")
if try_word==word: print("Good!")
else: print("Wrong, right word: ", word)