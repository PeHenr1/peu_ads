'''
palavra = 'IFSP'

i = 0
while i < len(palavra):
    print(palavra[i])
    i = i + 1

for i in range (len(palavra)):
    print(palavra[i])

for c in palavra:
    print(c)
'''

'''
texto = 'Instituto Federal'
print(texto[0:9])
print(texto[10:17])
'''

'''
f1 = 'Boa noite com melodia'
f2 = f1[:14]+"alegria!"
print(f2)

f1 = 'Boa noite com melodia'
f2 = ''
for i in range (14):
    f2 = f2 + f1[i]
f2 += 'alegria!'
print(f2)
'''

'''
vogais = 'aeiou'
texto = 'Instituto Federal'
for letra in texto:
    if letra.lower() in vogais:
        print(f'A letra {letra} é uma vogal!')
'''
'''
texto = input("Digite um texto:")
vogais = 'aeiouAEIOU'
texto_sv = ''
for letra in texto:
    if letra not in vogais:
        texto_sv = texto_sv + letra
print(texto_sv)
'''
'''
texto = 'algoritmos e programação'
novo = texto.upper()
print(novo)

t1 = 'minusculas'
t2 = 'MAIUSCULAS'
print(t1.islower())
print(t1.isupper())
print(t2.islower())
print(t2.isupper())
'''
'''
entrada='54987'
if entrada.isdigit():
    print('A entrada corresponde ao numero', int(entrada))
else:
    print('A entrada é um texto')
'''

################################################################
'''
#Exercicio 01
p = input('Digite uma palavra:')
cont = 0
for l in p:
    cont += 1
    print(l)
print(f'A palavra tem {cont} letras')

cont = cont - 1
while cont >= 0:
    print(p[cont])
    cont = cont - 1
'''

'''
#Exercicio 02
f = input('Digite uma frase:')
cont = 0
for l in f:
    if l != ' ':
        cont += 1
print(f'A palavra tem {cont} letras')
'''

'''
#Exercicio 03
frase = input('Digite uma frase:')
tam = len(frase)
cont = 0
x = 0
while x < tam:
    #ignora espaço em branco
    while x < tam and frase[x] == ' ': 
        x += 1
    if x < tam:
        cont += 1
        #ignora as letra ate achar oto espaço
        while x < tam and frase[x] != ' ' : 
            x += 1 
print(f'A frase tem {cont} palavras')
'''

'''
#Exercicios 04
f = input('Digite uma frase:')
l = input('Digite uma letra:')
pos = 0
for letra in range (len(f)):
    if f[letra] == l:
        pos = letra
print(f'A ultima ocorrencia da letra digitada é {pos}')
'''

'''
#Exercicios 05
f = input('Digite uma frase:')
l = input('Digite uma letra:')
pos = 0
for letra in range (len(f)):
    if f[letra] == l:
        pos = letra
print(f[:pos]+f[pos+1:])
'''

'''
#Exercicios 06
f = input('Digite uma frase:')
l = input('Digite uma letra:')
pos = 0
for letra in range (len(f)):
    if f[letra] == l:
        pos = letra
        break
print(f[:pos]+f[pos+1:])
'''
'''
#Exercicio 07
f = input('Digite uma frase:')
l = input('Digite uma letra:')
novo = ''
for letra in f:
    if letra != l:
        novo = novo + letra
print(novo)
'''
'''
#Exercicio 08
f = input('Digite uma frase:')
l = input('Digite uma letra:')
cont = 0
for letra in f:
    if letra == l:
        cont += 1
print(f'A letra {l} aparece {cont} vezes na frase')
'''
'''
#Exercicio 09
nome = input("Digite um nome:")
tam = len(nome)-1
while tam >= 0:
    print(nome[tam].upper(), end='')
    tam = tam - 1
'''
'''
#Exercicio 10
nome = input("Digite um nome:")
for i in range (len(nome)):
    print(nome[:i+1])
'''
'''
#Exercicio 11
frase = input("Digite uma frase:")
quantEsp = 0
quantA = 0
quantE = 0
quantI = 0
quantO = 0
quantU = 0
vogais = 'aeiouAEIOU'
for l in frase:
    if l in vogais:
        if l == 'A' or l == 'a':
            quantA += 1
        if l == 'E' or l == 'e':
            quantE += 1
        if l == 'I' or l == 'i':
            quantI += 1
        if l == 'O' or l == 'o':
            quantO += 1
        if l == 'U' or l == 'u':
            quantU += 1
    elif l == ' ':
        quantEsp += 1
print(f'Há {quantEsp} espaços e há {quantA+quantE+quantI+quantO+quantU} vogais sendo elas...')
print(f'A: {quantA}')
print(f'E: {quantE}')
print(f'I: {quantI}')
print(f'O: {quantO}')
print(f'U: {quantU}')
'''

#Exercicio 12
n = int(input("Digite um número inteiro positivo ou negativo:"))
