#Wikipedia: "In mathematics, in the areas of combinatorics and computer science,
#a Lyndon word is a nonempty string that is strictly smaller in lexicographic order than all of its rotations."
#in other words: permutation from the smallest values.
def lyndon(tab):
    tab.sort()
    c=[-1]
    while c:
        c[-1]+=1
        if len(c)==len(tab):
            print(''.join(tab[i] for i in c))
        while len(c)<len(tab):
            c.append(c[-len(c)])
        while c and c[-1] == len(tab)-1:
            c.pop()
tab=['2','1','3','5']
lyndon(tab)