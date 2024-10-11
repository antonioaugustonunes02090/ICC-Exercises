from sys import stdin

def check_palin(string):
    st = ''.join(string.lower().strip())
    palindro = True
    x=0
    while palindro:
        if  st[x] == st[-1-x]:
            x+=1
            if x == len(st):
                break
            pass
        else:
            palindro = False
    resposta = 'Sim' if palindro else 'Não'
    return resposta
for line in stdin:
    print(check_palin(line))
