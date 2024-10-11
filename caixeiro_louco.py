from itertools import permutations as permute
inp = input().split('[')
n = int(inp[0])
data = list(map(int,inp[1].strip(']').split()))
def check_input(data,n):
    for num in data:
        if num<0:
            message = 'Erro: entrada inválida, por favor insira uma matriz de distâncias com valores não negativos'
            return (False,message)
    if len(data) != n**2:
        message = 'Erro: entrada inválida, por favor insira uma matriz de distâncias quadrada'
        return (False,message)
    elif n==1:
        message = 'Erro: entrada inválida, por favor insira uma matriz de distâncias maior que 1x1'
        return (False,message)
    else:
        return (True,)
def make_matrix(data,n):
    real_matrix = []
    for i in range(n):
        real_matrix.append(data[i*n:(i+1)*n])
    return real_matrix
def make_it_nice(lista):
    lista.reverse()
    lista.append(0)
    lista.reverse()
    lista.append(0)
    return lista
def caixeiro(data,n):
    checking = check_input(data,n)
    if not checking[0]:    
        return checking[1]
    matrix = make_matrix(data,n)
    perm = list(permute([i for i in range(1,n)]))
    dist = []
    for way in perm:
        distsum = 0
        for city in range(n-1):
            if city == 0: 
                distsum+=matrix[0][way[city]]
                continue
            if city == n-2:
                distsum+=matrix[0][way[city]]
            distsum+=matrix[way[city-1]][way[city]]
        dist.append(distsum)
    min_route = min(dist)
    win_perm = make_it_nice(list(perm[dist.index(min(dist))]))
    fastest_perm = str(win_perm)
    message = f'Menor distância: {min_route}\nRota: {fastest_perm}'
    return message
print(caixeiro(data,n))
