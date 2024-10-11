from sys import stdin

def check_palin(string):
    st = ''.join(string.lower().split())
    palindro = True
    x=0
    erro = 'Erro: entrada inválida, por favor insira uma palavra ou frase'
    while palindro:
        try:
            if  st[x] == st[-1-x]:
                x+=1
                if x == len(st):
                    break
                pass
            else:
                palindro = False
        except:
            return erro
    resposta = 'É palíndromo' if palindro else 'Não é palíndromo'
    return resposta

for line in stdin:
    print(check_palin(line))
