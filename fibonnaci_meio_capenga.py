from sys import stdout
num = int(input())
def fib(n):
    fiblist = [0,1,1]
    if n == 1:
        return None
    a,b = 1,1
    for i in range(2,n-1):
        fiblist.append(a+b)
        a,b = b,a+b
    return fiblist
result = fib(num)
if not result is None:
    for i in fib(num):
        print(i,end=' ')
else:
    print(0)
