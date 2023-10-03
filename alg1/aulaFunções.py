'''
#Exercicio 02
def escreveLinha(n):
    for i in range(n):
        if i == (n-1):
            print('-')
        else:
            print('-', end='')

escreveLinha(3)
print('Instituto Federal')
escreveLinha(3)


#Exercicio 03
def escreveLinha(n, p):
    for i in range(n):
        if i == (n-1):
            print(p)
        else:
            print(p, end='')

escreveLinha(5, '*')
print('Instituto Federal')
escreveLinha(3, '=')


#Exercicio 04
def zeroummenos(n):
    if n > 0:
        e = 1
    elif n < 0:
        e = -1
    else:
        e = 0
    return e

n = int(input('Digite um número:'))
r = zeroummenos(n)
#print(r) duas formas de printar
print(zeroummenos(n))


#Exercicio 05
def letras(p):
    tam = len(p)
    return tam
palavra = input('Digite uma palavra:')
pal = letras(palavra)
print(f'A palavra tem {pal} letras')


#Exercicio 06
def contpalavras(f):
    x = 0
    cont = 0
    while x < len(f):
        #ignora espaço em branco
        while x < len(f) and frase[x] == ' ': 
            x += 1
        if x < len(f):
            cont += 1
            #ignora as letra ate achar oto espaço
            while x < len(f) and frase[x] != ' ' : 
                x += 1 
    return cont

frase = input('Digite uma frase:')
fr = contpalavras(frase)
print(f'A frase tem {fr} palavras')


#Exercicio 07
def palindromo(p):
    inv = p[::-1] # invertido
    e = False
    if p == inv:        
        e = True
    return e

palavra = input('Digite uma palavra:').lower()
print(palindromo(palavra))


#Exercicio 08
def digitos(n):
    n = str(n)
    if n.isdigit():
        tam = len(n)
    else:
        tam = len(n)-1
    return tam
   
n = int(input('Digite um nº:'))
print(f'Possui {digitos(n)} dígitos')


#Exercicio 09
def dataNasc(s):
    meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    dia, mes, ano = s.split('/')
    for m in range(len(meses)):
        if m == int(mes):
            msg = dia + ' de '+ meses[m] + ' de ' + ano
    return msg

data = input('Digite uma data (dd/mm/aaaa):')
print(dataNasc(data))


#Exercicio 10
def nExtenso(n):
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    unid = n % 10
    deze = n // 10

    if 0 <= n <= 9:
        for i in range(len(unidades)):
            if n == i:
                msg = unidades[i]

    elif 10 <= n <= 19:
        if n == 10:
            msg = 'dez'
        elif n == 11:
            msg = 'onze'
        elif n == 12:
            msg = 'doze'
        elif n == 13:
            msg = 'treze'
        elif n == 14:
            msg = 'catorze'
        elif n == 15:
            msg = 'quinze'
        else:
            for d in range(len(dezenas)):
                if deze == d:
                    for u in range(len(unidades)):
                        if unid == u:
                            if u == 6 or u == 7:
                                msg = dezenas[d] + 'es' + unidades[u]
                            elif u == 9:
                                msg = dezenas[d] + 'e' + unidades[u]
                            else:
                                msg = dezenas[d] + unidades[u]
    else:
         for d in range(len(dezenas)):
             if deze == d:
                 for u in range(len(unidades)):
                     if unid == u:
                         msg = dezenas[d] + ' e ' + unidades[u]

    return msg

num = int(input('Digite um nº de 0 a 99:'))
if 0 <= num <= 99:
    extenso = nExtenso(num)
    print(f"{num} por extenso: {extenso}")


#Exercicio 11
def inter(s1,s2):
    nova = ''
    for i in range(len(s1)):
        nova = nova + s1[i] + s2[i]
    return nova

str1 = input("Digite algo:")
str2 = input('Digite algo com a mesma qtde de letras:')
if len(str1) == len(str2):
    print(inter(str1,str2))


#Exercicio 12
def conta(b,e):
    r = int(b)**int(e)
    return r

base = int(input("Digite um nº:"))
exp = input('Digite um expoente:')
print(conta(base,exp))
'''

#Exercicio 13    # lista tem q ser feita pelo usuario
def soma(lista):
    soma = 0
    for e in lista:
        soma += e
    return soma

L = [1,2,3]
'''n = float(input("Digite um nº:"))
while n != '':
    L.append(n)
    n = float(input("Digite um nº:"))'''
print(soma(L))
