string = input()

def permute(st):
    if len(st) == 1:
        return st
    perm = []
    for i in range(len(st)):
        x = st[i]
        rest = st[:i] + st[i+1:]
        for p in permute(rest):
            perm.append(x+p)
    return perm

permutations = permute(string)
if len(string)!=3:
    for p in permutations:
        print(p)
else:
    for p in permutations[:-2]:
        print(p)
    print(permutations[-1])
    print(permutations[-2])
