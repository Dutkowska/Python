#task: https://pl.spoj.com/problems/BFN1/    - palyndromes
def palyndrome(x):
    i=0
    if str(x)==str(x)[::-1]: print(x, i)
    while(str(x)!=str(x)[::-1]):
        x+=int(str(x)[::-1])
        i+=1
    print(x, i)
t=int(input())
for i in range(t):
    x=int(input())
    palyndrome(x)
