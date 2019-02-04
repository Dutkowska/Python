#task: https://pl.spoj.com/problems/SYS/

def ele_sys(eleven):
    result=''
    signs={0:'0',1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A'}
    if eleven==0: return '0'
    while eleven!=0:
        new=eleven%11
        result+=signs[int(new)]
        eleven=int(eleven/11)
    result=result[::-1]
    return result

t=int(input())
for i in range(t):
    x=int(input())
    print(hex(x)[2:].upper(), ele_sys(x))