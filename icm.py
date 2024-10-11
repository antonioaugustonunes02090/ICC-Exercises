from sys import stdin
def imc(altura, peso):
        IMC = str(round(peso/(altura**2),2))
        if len(IMC)==4:
            IMC+='0'
        print(IMC, end=' ')
for line in stdin:
    medidas = line.split(',')
    altura, peso = float(medidas[0]) , float(medidas[1])
    imc(altura,peso)
