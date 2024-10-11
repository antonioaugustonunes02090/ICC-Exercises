st = input()

def letter_counter(string):
    counter = {}
    for letter in string:
        if not letter in counter:
            counter[letter] = 1
        else:
            counter[letter]+=1
    return counter

print(letter_counter(st))
