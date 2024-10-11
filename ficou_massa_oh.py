data = eval(input())

def count(data,x=0):
    for e in data:
        if type(e) == type(int()):
            x+=1
        elif type(e) == type(list()):
            x=count(e,x)
        else:
            continue
    return x


print(count(data))
