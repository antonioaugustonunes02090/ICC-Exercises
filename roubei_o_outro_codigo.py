from sys import stdin
def make_it_a_dict(value):
    a_dict = {}
    for i in range(0,len(value),2):
        a_dict[value[i]] = value[i+1]
    return a_dict
def check_lower_bound(dict_,bound):
    keys = list(dict_.keys())
    adict = {}
    for k in keys:
        if int(dict_[k])>bound:
            adict[k]=int(dict_[k])
    return adict
def get_dict():
    data = list(map(lambda x: x.rstrip(),stdin.readlines()))
    values = data[1:-1]
    bound = int(data[-1])
    adict = make_it_a_dict(values)
    ans = check_lower_bound(adict,bound)
    return ans

ans = get_dict() 
print(ans)
