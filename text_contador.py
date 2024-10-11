from sys import stdin

def func(st):
    soletra = list(''.join((st.lower().split())))
    letras = {}
    for letra in soletra:
        if letra in letras:
            letras[letra]+=1
        else:
            letras[letra] = 1
    resposta = ''
    for letra in letras:
        resposta += f'{letra}: {letras[letra]}\n'
    return resposta

for line in stdin:
    print(func(line),end='')
