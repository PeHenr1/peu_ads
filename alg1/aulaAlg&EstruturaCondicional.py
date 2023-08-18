##### SEMANA 2 - PARTE II #####
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

'''
x = int(input("Valor de x:"))
y = int(input("Valor de y:"))
z = (x**2 + y**2)//((x-y)**2)
print(f"Resultado: {z}")
'''

'''Exercicio 7
salario = float(input("Digite o salário:"))
#considerei que o reajuste aumentou
p = (25*salario)/100
r = salario+p
#print(f'Valor do reajuste: {p}')
print(f'Novo salário: {r}')
'''

##### SEMANA 2 - PARTE III #####

'''
nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
media = (nota1 + nota2) / 2
if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Em recuperacao")
else:
    print("Reprovado")
print("Fim do programa!")
'''

'''
n = float(input("Digite um número:"))
if n > 0:
    print('O número é positivo!!')
'''

''' par ou impar
n = float(input("Número:"))
if n % 2 == 0:
    print("O número digitado é par")
else:
    print("O número digitado é ímpar")
'''

''' exercicio 4
q = int(input("Digite a quantidade de livros que deseja: "))

a = (0.25 * q) + 7.5
b = (0.5 * q) + 2.5

print('\nHá duas possibilidades de realizar a comprar:')
print(f'Critério A: R$ 0,25 por livro + R$ 7,50 fixo. Ficando assim R${a}')
print(f'Critério B: R$ 0,50 por livro + R$ 2,50 fixo. Ficando assim R${b}')
'''

''' exercicio 5'''

''' exercicio 10
compra = float(input("Valor da compra:"))
valorT = 0
if compra <= 100:
    print('Desconto de 5%')
    desconto = (5*compra)/100
    valorT = compra - desconto
elif compra > 100 and compra < 200:
    print('Desconto de 10%')
    desconto = (10*compra)/100
    valorT = compra - desconto
else:
    print('Desconto de 20%')
    desconto = (20*compra)/100
    valorT = compra - desconto
print(f'Valor com descontos aplicados é de R${valorT}')
'''
