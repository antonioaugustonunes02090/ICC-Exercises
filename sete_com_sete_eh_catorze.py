nums = list(map(int,input().split(',')))
def five_seven(start,finish):
    form=''
    for n in range(start,finish+1):
        if n%35==0:
            form+=f'{n},'
    return form.strip(',')

print(five_seven(nums[0],nums[1]))
