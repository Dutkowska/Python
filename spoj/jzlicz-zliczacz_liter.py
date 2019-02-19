import string
lowerc = string.ascii_lowercase #ab...
upperc = string.ascii_uppercase #AB...
alphabet = lowerc + upperc
text = ''
t = int(input())
for i in range(t):
    words = list(map(str, input()))
    words = ''.join(words)
    text += words
for j in alphabet:
    num = 0
    for k in text:
        if j == k: num += 1
    if num != 0: print(j, num)