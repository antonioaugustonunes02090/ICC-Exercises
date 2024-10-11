st = input()

def operate(op):
    operators = ['+','-','*','/','^']
    if operators[0] in op:
        nums = list(map(int,op.split(operators[0])))
        result = f'{nums[0]+nums[1]}'
        return result
    if operators[3] in op:
        nums = list(map(int,op.split(operators[3])))
        if nums[1] == 0:
            erro = 'Erro: divisão por zero'
            return erro
        result = f'{round(nums[0]/nums[1],3)}'
        return result
    if operators[2] in op:
        nums = list(map(int,op.split(operators[2])))
        result = f'{nums[0]*nums[1]}'
        return result
    if operators[4] in op:
        nums = list(map(int,op.split(operators[4])))
        if nums[0]==nums[1] and nums[0]==0:
            erro = "Erro: base e expoente nulos"
            return erro
        result = f'{nums[0]**nums[1]}'
        return result
    if operators[1] in op:
        nums = list(map(int,op.split(operators[1])))
        result = f'{nums[0]-nums[1]}'
        return result

print(operate(st))
