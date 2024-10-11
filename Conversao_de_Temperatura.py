from sys import stdin

def integer_converter(num):
    if num.is_integer():
        return int(num)
    else:
        return num
def converter(celsius):
    C = float(celsius.split()[0])
    F = integer_converter(9*C/5 + 32)
    K = integer_converter(C + 273)
    return [F,K]

for line in stdin:
    temp = converter(line)
    print(f'{temp[0]} F')
    print(f'{temp[1]} K')
