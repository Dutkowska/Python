from random import random, choice, sample
import linecache
a="What's next? Press 'l' to remind list of codes. "
def info():
    info=open('info.txt', 'r')
    for line in info: print(line)
    info.close()
    print('\n')
    
def read():
    print('\nYour words from test-file:\n')
    test=open('test.txt', 'r')
    for line in test: print(line)
    test.close()
    print(a)
    
def correct():
    word=input("Which world do you want to correct? ")
    wordnew=input("Write the new one: ")
    test=open('test.txt', 'r')
    testdata=test.read()
    test.close()
    
    newtest=testdata.replace(word, wordnew)
    test=open('test.txt', 'w')
    test.write(newtest)
    test.close()
    print("Thank you, your word is changed.")
    print(a)
    
def add():
    test=open('test.txt', 'a')
    test.write("\n")
    word1=input("Write polish word: ")
    test.write(word1)
    word2=input("And translation: ")
    test.write(' - ')
    test.write(word2)
    test.close()
    print("Thank you, your words are in the file. ")
    print(a)
    
def start():
    print("Try to memorize this words!")
    test=open('test.txt', 'r')
    l=len(test.readlines())
    tests=sample(list(open('test.txt')), l)
    print(tests[0])
    for i in range(1,l):
        press=input("Press 'n' to see next random pair of words,\nPress 'e' to stop the game: ")
        if(press=='n'): print(tests[i])
        elif(press=='e'): break
        else: print('Wrong code.')
    test.close()
    print(a)
    
info()
while True:
    code=input("Your code:")
    if code=='r': 
        read()
    elif code=='l':
        info()
    elif code=='c':
        correct()
    elif code=='a':
        add()
    elif code=='s':
        start()
    elif code=='e':
        print("Thank you, bye!")
        break
    else:
        rem=input("Wrong code, try again! Do you want to remind list of codes (y/n)? ")
        if rem=='y':
            info()