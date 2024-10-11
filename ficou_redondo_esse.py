from sys import stdin
def make_it_a_dict(values):
    a_dict = {}
    for i in range(0,len(values),2):
        a_dict[values[i]] = values[i+1]
    return a_dict
def get_dict():
    data = list(map(lambda x: x.rstrip(),stdin.readlines()))
    values = data[1:]
    ans = make_it_a_dict(values)
    return ans

ans = get_dict()
print(ans)
