from string import ascii_lowercase as alphabet
st = list(''.join(input().lower().split()))
vowels = ['a','â','ã','á','à','e','é','ê','i','í','o','õ','ô','ó','u','ú']
consonants = list(alphabet)
consonants.append('ç')
for letter in vowels:
    if letter in consonants:
        consonants.remove(letter)
def count(string):
    global vowels, consonants
    dict_count= {'Vogais':0,'Consoantes':0}
    for letter in string:
        if letter in vowels:
            dict_count['Vogais'] += 1
        elif letter in consonants:
            dict_count['Consoantes']+=1
    message = f'Vogais: {dict_count["Vogais"]}\nConsoantes: {dict_count["Consoantes"]}'
    return message
print(count(st))
            
    
