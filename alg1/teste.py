'''
nome = input()
#print("Salve", nome,"! Belezura?")
print(f"Salve {nome}! Belezura?")

print("\n.\n")


x = int(input('Informe um valor: '))
y = int(input('Informe outro valor: '))

print("Tipo de dado de x:", type(x))
print("Tipo de dado de y:", type(y))

soma = x + y
multiplicacao = x * y
subtracao = x - y
divisao = x / y
divisao_inteira = x // y
resto_divisao = x % y

print("Soma: ",soma)
print("Multiplicação: ",multiplicacao)
print("Subtração: ",subtracao)
print("Divisão: ",divisao)
print("Divisão inteira: ",divisao_inteira)
print("Resto: ",resto_divisao)
'''
#EXERCICIOS
'''
nome = input()
n1 = float(input("Digite a nota 1:"))
n2 = float(input("Digite a nota 2:"))
media = (n1+n2)/2
print(f"A média de {nome} é: {media}")
'''

'''
n1 = float(input("Digite a nota 1:"))
n2 = float(input("Digite a nota 2:"))
n3 = float(input("Digite a nota 3:"))
peso1, peso2, peso3 = 1,2,3
mediaP = ((n1*peso1)+(n2*peso2)+(n3*peso3))/(peso1+peso2+peso3)
print(mediaP)
'''

x = int(input("Valor de x:"))
y = int(input("Valor de y:"))
z = (x**2 + y**2)//((x-y)**2)
print(f"Resultado: {z}")
