# SLIDES DE WHILE E FOR

'''
#Exercicio 01
n = int(input("Digite um número:"))
i = 1
while i <= n:
    print(i)
    i += 1
'''

'''
#Exercicio 02
x = int(input("Digite um número X:"))
y = int(input("Digite um número Y:"))
while x <= y:
    print(x)
    x += 1
'''

'''
#Exercicio 03
soma = 0
i = 0
while i <= 100:
    soma = soma + i
    i += 1
print(soma)
'''

'''
#Exercicio 04
soma = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        soma = soma + i
    i += 1
print(soma)
'''

'''
#Exercicio 05
chico = 150
ze = 110
anos = 0

while ze < chico:
    chico += 2
    ze += 3
    anos += 1
print(f'Demorou {anos} anos para Zé ficar maior que Chico')
'''

'''
#Exercicio 06
n = int(input("Digite um número:"))
for i in range (1,10): #o exemplo saida mostrou ate o 9
    print(f'{i} x {n} =',n*i)
'''

'''
#Exercicio 07
n = int(input("Digite um número:"))
h = 0
if n >= 1:
    i = 1
    while i <= n:
        h = h + (1/i)
        i+=1
print(f'O número harmônico de {n} é: {h}')
'''

'''
#Exercicio 08
numero = int(input("Digite um número:"))
fat = numero
n = numero - 1
if numero == 0:
    print(f'Fatorial de {numero} é: 1')
else:
    while n != 0:
        fat = fat * n
        n-=1
    print(f'Fatorial de {numero} é: {fat}')
'''

'''
#Exercicio 09
n = int(input("Digite um número:"))
maior = 0
while n > 0:
    if n > maior:
        maior = n
    n = int(input("Digite um número:"))
print(f'O maior número digitado foi {maior}')
'''

'''
#Exercicio 10
n = int(input("Digite uma nota de um aluno:"))
maior = 0
menor = 999999999
qtdeA = 0
while n > 0:
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    qtdeA += 1
    n = int(input("Digite outra nota de um aluno:"))
print(f'Há {qtdeA} alunos. Onde a maior nota foi {maior} e a menor foi {menor}')
'''

'''
#Exercicio 11
n = int(input("Digite uma nota de um aluno:"))
qA = 0
qB = 0
qC = 0
while n > 0:
    if n >= 6:
        qA += 1
    elif n >= 4 and n < 6:
        qB += 1
    else:
        qC += 1
    n = int(input("Digite outra nota de um aluno:"))
print(f'Dos digitados, {qA} tem nota maior ou igual a 6, {qB} tem notas entre 4 e 6 e {qC} tem nota menor que 4.')
'''

'''
#Exercicio 12
# Fibonacci Fn é dado pela seguinte fórmula: Fi = Fi-1 + Fi-2
n = int(input("Digite um número:"))
Fi = 1
ant = 1     #Fi-1
antant = 0  #Fi-2
while n != 0:
    print(Fi, end=' ')
    Fi = Fi + antant
    antant = ant
    ant = Fi
    n -= 1
'''

'''
#Exercicio 13
x = int(input("Digite uma nota de um aluno:"))
while x != 1:
    if x % 2 ==0:
        x = x/2
    else:
        x = 3 * x + 1
    print(int(x), end=' ')
'''

''' fazer teste de mesa
#Exercicio 14
x = int(input())
y = int(input())
z = int(input())
while x < 10:
    x = x + 3
    y = y + (x % 2)
flag = True
while flag and y < 10:
    y = y + 2
    x = x - 1
    if x <= y:
        flag = False
i = 0
while i < z:
    y = y + i
    i = i + 1
print(x, y, z)'''


