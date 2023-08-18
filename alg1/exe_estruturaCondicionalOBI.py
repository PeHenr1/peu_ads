'''
#Exercicio 01 - Divisão do Tesouro
nMoedas = int(input("Digite o número de moedas:"))
mar = int(input("Digite a quantidade de marinheiros:"))+2
cadaUm = nMoedas/mar
mCap = cadaUm*2
print(mCap)
'''

'''
#Exercício 02 - Duplas de tênis
a = int(input("Nível do jogador A:"))
b = int(input("Nível do jogador B:"))
c = int(input("Nível do jogador C:"))
d = int(input("Nível do jogador D:"))

menorDif = 99999

if ((a+b)-(c+d)) < menorDif:
    if ((a+b)-(c+d)) > 0:
        menorDif = ((a+b)-(c+d))
    else:
        menorDif = ((a+b)-(c+d)) * -1
        
if ((a+c)-(b+d)) < menorDif:
    if ((a+c)-(b+d)) > 0:
        menorDif = ((a+c)-(b+d))
    else:
        menorDif = ((a+c)-(b+d)) * -1
        
if ((a+d)-(b+c)) < menorDif:
    if ((a+d)-(b+c)) > 0:
        menorDif = ((a+d)-(b+c))
    else:
        menorDif = ((a+d)-(b+c)) * -1
#seria interessante pegar os times formados tb
print(menorDif)
'''


#Exercício 03 - Média ou mediana
n1 = int(input("Digite:"))
n2 = int(input("Digite:"))



