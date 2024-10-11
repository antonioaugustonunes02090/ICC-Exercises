nums = input().split()
base, n = int(nums[0]), int(nums[1])

def exp(b,n):
    if n==0:
        return 1
    return b*exp(b,n-1)

print(exp(base,n))
