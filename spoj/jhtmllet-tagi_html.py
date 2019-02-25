"""
task: https://pl.spoj.com/problems/JHTMLLET/
"""
while True:
    line = list(map(str, input()))
    if line == "": break
    else:
        for i in range(len(line)):
            if line[i] == "<": check = True
            elif line[i] == ">": check = False
            else:
                if check == True: line[i]=line[i].upper()
    text = "".join(line)
    print(text)