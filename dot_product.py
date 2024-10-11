from sys import stdin

def dot(m1,m2):
    line1 = [m1[0]*m2[0]+m1[1]*m2[2],m1[0]*m2[1] + m1[1]*m2[3]]
    line2 = [m1[2]*m2[0]+m1[3]*m2[2],m1[2]*m2[1] + m1[3]*m2[3]]
    print(f'{line1[0]} {line1[1]}',f'{line2[0]} {line2[1]}',sep='\n')
m1 = []
m2 = []
x=0
for line in stdin:
    nums = list(map(int,line.split()))
    for num in nums:
        if x<2:
            m1.append(num)
        else:
            m2.append(num)
    x+=1
dot(m1,m2)
