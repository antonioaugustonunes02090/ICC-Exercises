from sys import stdin

def sorter(string):
    nums = list(map(int,string.split()))
    for i in range(1,len(nums)):
        x=i
        while nums[x]<nums[x-1] and x!=0:
            temp = nums[x]
            nums[x] = nums[x-1]
            nums[x-1] = temp
            x-=1
    resposta = ''
    for i in range(len(nums)):
        resposta+=f'{nums[i]} '
    return resposta.strip()

for line in stdin:
    print(sorter(line))
