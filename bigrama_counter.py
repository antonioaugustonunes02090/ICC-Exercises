from sys import stdin

def bigrama(string):
    lista = string.lower().split()
    counter = {}
    for n in range(1,len(lista)):
        bigram = f'{lista[n-1]} {lista[n]}'
        if not bigram in counter:
            counter[bigram] = 1
        else:
            counter[bigram]+= 1
    for key in counter:
        print(f'{key}: {counter[key]}')

for line in stdin:
    bigrama(line)
