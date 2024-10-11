nums = list(map(int,input().split()))



def mdc(n,m,start):
    if n % start == 0 and m % start ==0:
        return start
    else:
        return mdc(n,m,start-1)

print(mdc(nums[0],nums[1],min(nums)))
        
