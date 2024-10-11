num = input()

def sum_digits(st):
    nums = list(map(int,list(st)))
    soma = sum(nums)
    return soma

print(sum_digits(num))
