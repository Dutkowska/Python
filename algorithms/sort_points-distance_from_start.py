#write out points, starting from the closest to (0,0)
#This is my (diferent) version of: PP0506A - Sort 1
#https://pl.spoj.com/problems/PP0506A/
#for writing like in task: add a,b to distans=[[...range(4)]]
    #and print x[1:4]

t=int(input())
for i in range(t):
    pts=int(input()) #numb of points
        # add points tab=[[point], [point],...]
        #point = input: name num num (f.e. A 0 1)
        # f.e. A 0 1 // B 2 3 // ... -> [[A, 0, 1], [B, 2, 3], ....]
    tab=[[x for x in input().split()] for points in range(pts)]
    distans=[[0 for x in range(2)] for points in range(pts)]
    for j in range(pts):
        name, a, b = tab[j][0], int(tab[j][1]), int(tab[j][2])
        distans[j][0]=abs(complex(a,b))
        distans[j][1]=name
    distans.sort()
    print(*[x[1] for x in distans])