#fatorial
def fatorial(n):
    if n <= 1:
        return n
    
    return n * fatorial(n-1)
'''    
num = int(input('Digite um número:'))
print(fatorial(num))
'''

#potencia
def potencia(base,pote):
    if base == 1 or pote == 1:
        return base

    return base * potencia(base,pote-1)
'''
b = int(input('Digite nº base:'))
p = int(input('Digite nº potência:'))
print(potencia(b,p))
'''    

#quociente
def quociente(num,div):
    if num < div:
        return 0
    return 1+quociente(num-div,div)
'''
n = int(input('Nº:'))
d = int(input('Dividido por:'))
print(quociente(n,d))
'''

#resto da divisao
def resto(num,div):
    if num < div:
        return num
    return resto(num-div,div)
'''
n = int(input('Nº:'))
d = int(input('Dividido por:'))
print(resto(n,d))
'''

#qtde caractere
def quant(p):
    if len(p) == 0:
        return 0
    return 1 + quant(p[1:])
'''
pal = input("Digite algo:")
print(quant(pal))
'''

#mostrar string em pé
def mostra(p):
    if len(p) == 0:
        return 0
    print(p[0])
    mostra(p[1:])
'''
pal = input("Digite algo:")
mostra(pal)
'''

#mostra num invertido
def invertido(n):
    if n == 0:
        return n
    print(n%10)
    invertido(n//10)
'''  
num = int(input("Nº:"))
invertido(num)
'''

#mostrar num ordem certa
def certa(n):
    if n == 0:
        return n
    certa(n//10)
    print(n%10)
'''  
num = int(input("Nº:"))
certa(num)
'''

#maior elemento inteiro de uma lista
def maior(lista):
    if len(lista) == 1:
        return lista[0]
    
    # Recursivamente encontre o maior elemento da sublista restante
    sublista = lista[1:]
    maior_da_sublista = maior(sublista)

    # Compare o primeiro elemento com o maior elemento da sublista
    if lista[0] > maior_da_sublista:
        return lista[0]
    else:
        return maior_da_sublista
         
L = [5,9,1,15,4,7]
print(maior(L))
