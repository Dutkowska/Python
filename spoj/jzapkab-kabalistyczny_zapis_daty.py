#task: https://pl.spoj.com/problems/JZAPKAB/
chars = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'k':10, 'l':20, 'm':30, 'n':40, 'o':50, 'p':60, 'q':70, 'r':80, 's':90, 't':100, 'v':200, 'x':30, 'y':400, 'z':500}
text = input()
date = 0
for i in text: date += chars[i]
print(date)