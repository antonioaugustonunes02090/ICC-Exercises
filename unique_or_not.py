data = input().split()


def unique_value(list_,value):
    index = list_.index(value)
    list_.reverse()
    rindex = list_.index(value)
    return True if rindex ==  len(list_) - index - 1 else False

def unique_values(list_):
    for e in list_:
        if not unique_value(list_,e):
            return False
    return True

print(unique_values(data))
