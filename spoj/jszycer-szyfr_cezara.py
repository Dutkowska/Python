#task: https://pl.spoj.com/problems/JSZYCER/
#with using Unicode code
while True:
    code = list(map(str, input()))
    if code == '': break
    else:
        for i in range(len(code)):
            if code[i] in ['\n', ' ']: continue
            elif code[i] in ['X', 'Y', 'Z']:
                code[i] = chr(ord(code[i]) - 23)
            else: code[i] = chr(ord(code[i]) + 3)
        text = ''.join(code)
        print(text)
