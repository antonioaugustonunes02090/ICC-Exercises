def get_data():
    n1 = int(input())
    d1 = {input().strip():int(input()) for i in range(n1)}
    n2 = int(input())
    d2 = {input().strip():int(input()) for i in range(n2)}
    return (d1,d2)

def join_dicts():
    d1,d2 = get_data()
    new_dict = {}
    for key in d1.keys():
        new_dict[key] = d1[key]
    for key in d2.keys():
        if key in new_dict:
            new_dict[key]+=d2[key]
        else:
            new_dict[key] = d2[key]
    return new_dict

d = join_dicts()

print(d)
