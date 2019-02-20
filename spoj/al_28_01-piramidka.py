#task: https://pl.spoj.com/problems/AL_28_01/

length = int(input())
text = list(input())
if length == len(text):
    word = list(['.'] * length)
    center = int((length - 1) / 2)
    for i in range(center+1):
        word[center + i] = text[center + i]
        word[center - i] = text[center - i]
        print(*word, sep='')