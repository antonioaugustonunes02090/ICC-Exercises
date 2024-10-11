from sys import stdin

def word_counter(string):
    words = string.lower().split()
    counter = {}
    for word in words:
        if word in counter:
            counter[word]+=1
        else:
            counter[word] = 1
    resposta = ''
    for word in counter:
        resposta += f'{word}: {counter[word]}\n'
    return resposta.strip()

for line in stdin:
    print(word_counter(line), end='')
    
