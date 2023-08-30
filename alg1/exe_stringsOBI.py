'''
# Exercicio 01 - Cifra da Nlogônia
palavra = input("Digite uma palavra sem acentos:")
codif = ''
vogais = 'aeiou'
alfabeto = 'abcdefghijklmnopqrstuvxz'
for letra in palavra:
    if letra in vogais:
        codif += letra
    else:
        #1. consoante original
        codif += letra
        #2. vogal mais proxima da consoante original
        posC = 0
        posV = 0
        for ind in range (len(alfabeto)):
            if letra == alfabeto[ind]:
                #pegar a vogal mais proxima
                posC = ind
                achou = False
                while achou == False:
                    i = ind-1
                    posA = 0
                    posD = 0
                    #percorre da posC ate o começo
                    while i >= 0:
                        if alfabeto[i] in vogais:
                            posA = i
                            i = -1
                        i = i - 1
                    #percorre da posC ate o final
                    i = ind + 1
                    while i < len(alfabeto):
                        if alfabeto[i] in vogais:
                            posD = i
                            i = len(alfabeto)+1
                        i = i + 1
                    #verifica qual letra ta mais perto e mais perto do começo
                    if (posC-posA)<(posD-posC) or (posC-posA)==(posD-posC):
                        posV = posA
                        achou = True
                    elif (posC-posA)>(posD-posC):
                        posV = posD
                        achou = True
                codif = codif + alfabeto[posV]
        #3. pega a proxima consoante
        posC += 1
        while posC < len(alfabeto):
            if alfabeto[posC] not in vogais:
                codif = codif + alfabeto[posC]
                posC = len(alfabeto)+1
            posC +=1

print(f'Palavra codificada: {codif}')
'''

# Exercicio 02 - Telefone

n = input("Digite um número de telefone:")
dois = 'abcABC'
tres = 'defDEF'
quatro = 'ghiGHI'
cinco = 'jklJKL'
seis = 'mnoMNO'
sete = 'pqrsPQRS'
oito = "tuvTUV"
nove = 'wxyzWXYZ'

nDigitos = ''

for d in n:
    if d.isdigit():
        nDigitos += d
    else:
        if d in dois:
            nDigitos += '2'
        elif d in tres:
            nDigitos += '3'
        elif d in quatro:
            nDigitos += '4'
        elif d in cinco:
            nDigitos += '5'
        elif d in seis:
            nDigitos += '6'
        elif d in sete:
            nDigitos += '7'
        elif d in oito:
            nDigitos += '8'
        elif d in nove:
            nDigitos += '9'
        else:
            nDigitos += d
print(nDigitos)
            
            






