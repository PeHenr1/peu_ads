'''
#Exercicio 01
lista = []
for i in range(10):
    lista.append(int(input("Informe um valor:")))
soma = 0
for n in lista:
    print(n, end = ' ')
    soma += n
print(f'\nSoma: {soma}')
for n in lista:
    if n % 2 == 0:
        print(n, end = ' ')

#Exercicio 02
lista = []
n = int(input("Quantos valores irá informar?:"))
for i in range(n):
    lista.append(float(input("Digite uma altura (em metros):")))
menor = lista[0]
pos = 0
for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        pos = i
    print(lista[i],end=' ')
print(f'\nMenor altura: {menor}, posição: {pos}')

#Exercicio 03
lista = []
media = 0
for i in range(7):
    temp = int(input("Informe uma temperatura:"))
    lista.append(temp)
    media += temp
media = media/7
cont = 0
for n in lista:
   if n > media:
       cont += 1
print(cont)


#Exercicio 04
A = []
B = []
lista = []
for i in range(10):
    if i < 5:
        A.append(int(input("Informe um valor para a lista A:")))
    else:
        B.append(int(input("Informe um valor para a lista B:")))
for i in range(10):
    n = int(input("Informa um valor para a lista C:"))
    lista.append(n)
    if i < 5:
        A.append(n)
    else:
        B.append(n)
C = []
for i in range(10):
    x = A[i]+B[i]
    C.append(x)
print(f'Lista A: {A}\nLista B: {B}\nLista C: {C}')


#Exercicio 05
lista = []
impar = 0
par = 0
for i in range(15):
    lista.append(int(input("Digite número:")))
for n in lista:
    if n % 2 == 0:
        par += n
    else:
        impar += n
print(f'Soma Ímpares: {impar}\nSoma Pares: {par}')


#Exercicio 06
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
x = int(input("Qual nº deseja verificar?:"))
ta = False
for i in range(len(lista)):
    if lista[i] == x:
        ta = True
        i = len(lista)-1
if ta:
    print("Está na lista!!")
else:
    print("Não está na lista!!")


#Exercicio 07
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
x = int(input("Qual nº deseja verificar?:"))
ta = False
pos = -1
for i in range(len(lista)):
    if lista[i] == x:
        ta = True
        pos = i
        i = len(lista)-1
        
if ta:
    print(f"Está na lista na posição {pos}!!!")
else:
    print(f"Não está na lista!! {pos}")


#Exercicio 08
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
maior = lista[0]
pos = 0
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        pos = i
print(f"Lista: {lista}\nO maior valor é '{maior}' e está na posição '{pos}'")


#Exercicio 09
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
for i in range(len(lista),0,-1):
    print(i, end=' ')
  

#Exercicio 10
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
x = int(input("Qual nº deseja verificar?:"))
cont = 0
for n in lista:
    if n == x:
        cont += 1
print(f"O nº'{x}' aparece '{cont}' vezes")


#Exercicio 11 - NAO ACABADO
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
mais = 0
maiores = []
for numero in range(len(lista)):
    cont = 0
    for n in lista[numero:]:
        if lista[numero] == n:
            cont += 1
    mais = cont
    '''

#Exercicio 12 - NAO ACABADO
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
print(f'Lista: {lista}')
x = int(input("Qual nº deseja remover?:"))
deletou = False
for i in range(len(lista)):
    if lista[i] == x and deletou == False:
        del lista[i]
        deletou = True
print(f'Lista: {lista}')


        
