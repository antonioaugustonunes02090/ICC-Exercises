from sys import stdin

def mean(numbers):
    nums = list(map(int,numbers.split()))
    soma = sum(nums)
    return soma/len(nums)

for line in stdin:
    print(mean(line))
