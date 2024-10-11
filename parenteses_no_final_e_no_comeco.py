st = input()

def check_num(string):
    return False if len(string)%2!=0 else True
def check_par(string):
    lista = list(string)
    expected1, expected2 = '()',')('
    observed = ''.join([string[0],string[-1]])
    ans = True if observed == expected1 or observed == expected2 else False
    return ans
def recursive_checker(string):
    if not check_num(string):
        return False
    if len(string)==2 and check_par(string):
        return True
    elif check_par(string):
        new_string = list(string)
        del new_string[0]
        del new_string[-1]
        final_str = ''.join(new_string)
        return check_par(final_str)
print(recursive_checker(st))
        
