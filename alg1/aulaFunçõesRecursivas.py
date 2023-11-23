'''
def termo_fibonacci(n):
    if n <= 1:
        return n
    else:
        return termo_fibonacci(n-1) + termo_fibonacci(n-2)

nro=int(input('Digite o termo da sequência de Fibonacci: '))
if nro < 0:
    print("O número deve ser maior ou igual a zero!")
else:
    print(termo_fibonacci(nro))



def sequencia_fibonacci(a, b, n):
    print(a," ",end="")
    if b < n:
        sequencia_fibonacci(b, a + b, n)
nro=int(input('Digite o valor de parada da sequência de Fibonacci: '))
sequencia_fibonacci(0,1,nro)
'''
#Exercicio 01
'''
def fatorial(n):
    fat = 1
    while n != 0:
        fat = fat * n
        n -= 1
    return fat

def fat_recursiva(n):
    if n == 1 or n == 0:
        return 1
    
    return n * fat_recursiva(n-1)
        
    
num = int(input("Digite um número fatorial recursiva:"))
print(fatorial(num))
print(fat_recursiva(num))
'''

#Exercicio 02
'''
def potencia(bas,pot):
    r = 1
    for i in range(pot):
        r = r * bas
    return r

def pot_recursiva(bas,pot):
    if bas == 1 or pot == 1:
        return bas

    return bas * pot_recursiva(bas,pot-1)

x = int(input("Digite um número base:"))
y = int(input("Digite um número potência:"))
print(potencia(x,y))
print(pot_recursiva(x,y))
'''

#Exercicio 03
'''
def quociente(num,div):
    q = 0
    while num >= div:
        num = num - div
        q += 1
    return q

def quoc_recursiva(num,div):
    if num < div:
        return 0
    
    return 1+quociente(num-div,div)
    
n = int(input("Número:"))
d = int(input("Dividido por:"))
print(quociente(n,d))
print(quoc_recursiva(n,d))
'''

#Exercicio 04
'''def resto(num,div):
    while num >= div:
        num = num - div
    return num

def resto_recursiva(num,div):
    if num < div:
        return num
    
    return resto_recursiva(num-div,div)
    
n = int(input("Número:"))
d = int(input("Dividido por:"))
#print(resto(n,d))
print(resto_recursiva(n,d))
'''

#Exercicio 05
'''
def contar(p):
    i = 0
    for e in p:
        i += 1
    return i

def contar_recursiva(p):
    if len(p) == 0:
        return 0

    return 1+contar_recursiva(p[1:])

palavra = input("Digite uma palavra:")
#print(contar(palavra))
print(contar_recursiva(palavra))
'''

#Exercicio 06
'''
def exibe(p):
    for e in p:
        print(e)

def exibe_recursiva(p):
    if len(p) == 0:
        return 0
    
    print(p[0])
    exibe_recursiva(p[1:])

palavra = input("Digite uma palavra:")
exibe(palavra)
#exibe_recursiva(palavra)
'''

#Exercicio 07
'''
def algarismo(n):
    while n != 0:
        print(n%10)
        n = n // 10
        
def alg_recursiva(n):
    if n == 0:
       return n

    print(n%10)
    return alg_recursiva(n//10)

num = int(input("Digite um número:"))
#algarismo(num)
alg_recursiva(num)'''

#Exercicio 08
'''Crie uma função para exibir os algarismos de um número positivo na
ordem correta. Não é permitida a conversão para string. Exemplo: 326'''
'''def algarismo(n):
    alg = []
    #cria uma lista com os N invertido
    while n != 0:
        r = n % 10
        alg.append(r)
        n = n // 10
    #printa na ordem correta, percorrendo de tras pra frente
    for i in range(len(alg)-1,-1,-1):
        print(alg[i])
    
def alg_recursiva(n):
    if n == 0:
       return  
    alg_recursiva(n//10)
    print(n%10)
        

num = int(input("Digite um número:"))
algarismo(num)
alg_recursiva(num)'''

#Exercicio 09
def maior(lista):
    m = 0
    for i in lista:
        if i > m:
            m = i
    return m

def maior_recursiva(lista,m): #nao entendi
    if len(lista) == 0:
        return m
    if lista[0] > m:
        m = lista[0]
    return maior_recursiva(lista[1:],m)

L = [1,3,8,5,6]
M = L[0]
#print(maior(L))
print(maior_recursiva(L,M))


