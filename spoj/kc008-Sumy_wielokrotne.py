sum_all = 0
while True:
    tab=[int(x) for x in input().split()]
    print(sum(tab))
    sum_all += sum(tab)
print(sum_all)