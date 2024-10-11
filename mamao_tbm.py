num = int(input())

def sum_recursively(n):
    if n == 0:
        return 0
    return n + sum_recursively(n-1)

print(sum_recursively(num))
