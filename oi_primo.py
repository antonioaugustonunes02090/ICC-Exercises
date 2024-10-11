num = int(input())

def check_prime(x):
    n = 'Não é primo'
    y = 'É primo'
    if x == 1 or x == 0:
        return n
    elif x == 2:
        return y
    for i in range(2,x):
        if x%i == 0:
            return n
    return y
print(check_prime(num))
