'''
#matriz 3x4
linhas = 3
colunas = 4

mat = []

for i in range(linhas):
    linha = []
    
    for j in range(colunas):
        n = int(input(f"Digite um número {[i]}{[j]}:"))
        linha.append(n)
    mat.append(linha)
    
print(f"\n{mat}\n")

#mostra bunitinho
for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j],end=' ')
    print()

'''

'''
#Exercicio 01
mat=[]
linhas = 3
colunas = 3

for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input("Digite um número:"))
        linha.append(n)
    mat.append(linha)

soma = 0
for i in range(linhas):
    for j in range(colunas):
        soma += mat[i][j]
        print(mat[i][j],end=' ')
    print()
print(f'Soma total dos elementos: {soma}')

print('Soma de cada linha respectivamente:', end=' ')
for i in range(linhas):
    s = 0
    for j in range(colunas):
        s += mat[i][j]
    print(s,end = ' ')


#Exercicio 02
mat = []
linhas = int(input("Informe o nº de linhas:"))
colunas = int(input("Informe o nº de colunas:"))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input("Digite um número:"))
        linha.append(n)
    mat.append(linha)

for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j],end=' ')
    print()


#Exercicio 03
mat = []
M = int(input("Informe o nº de linhas e colunas:"))
for i in range(M):
    linha = []
    for j in range(M):
        n = int(input("Digite um número:"))
        linha.append(n)
    mat.append(linha)

for i in range(M):
    for j in range(M):
        print(mat[i][j],end=' ')
    print()

print()
soma = 0
for i in range(M):
    print(mat[i][i], end = ' ')
    soma += mat[i][i]
print(f'\nValor do traço: {soma}')


#Exercicio 04 - NAO ACABADO
mat = []
M = int(input("Informe o nº de linhas e colunas:"))
for i in range(M):
    linha = []
    for j in range(M):
        n = int(input("Digite um número:"))
        linha.append(n)
    mat.append(linha)

print("MATRIZ NORMAL:")
for i in range(M):
    for j in range(M):
        print(mat[i][j],end=' ')
    print()
    
for i in range(M):
    for j in range(M):
        if i == j:
            mat[i][j] = 1
        else:
            mat[i][j] = 0

print("MATRIZ IDENTIDADE:")
for i in range(M):
    for j in range(M):
        print(mat[i][j], end=" ")
    print()


#Exercicio 05
matUm = []
matDois = []
linhas = int(input("Informe o nº de linhas:"))
colunas = int(input("Informe o nº de colunas:"))
for i in range(1,3):
    print(f'\nMatriz {i}:')
    if i == 1:
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                n = int(input("Digite um número:"))
                linha.append(n)
            matUm.append(linha)

        for i in range(linhas):
            for j in range(colunas):
                print(matUm[i][j],end=' ')
            print()
    else:
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                n = int(input("Digite um número:"))
                linha.append(n)
            matDois.append(linha)

        for i in range(linhas):
            for j in range(colunas):
                print(matDois[i][j],end=' ')
            print()
mat = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        soma = matUm[i][j]+matDois[i][j]
        linha.append(soma)
    mat.append(linha)

print('\nMatriz somada:')
for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j],end=' ')
    print()


#Exercicio 06
mat = []
linhas = int(input("Informe o nº de linhas:"))
colunas = int(input("Informe o nº de colunas:"))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input("Digite um número:"))
        linha.append(n)
    mat.append(linha)

print('\nMatriz Normal:')
for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j],end=' ')
    print()

print('\nMatriz Transposta:')
for i in range(colunas):
    for j in range(linhas):
        print(mat[j][i],end=' ')
    print()


#Exercicio 07
mat = []
linhas = int(input("Informe o nº de linhas e colunas:"))
colunas = linhas
simetrica = True

for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input("Digite um número:"))
        linha.append(n)
    mat.append(linha)
print('\nMatriz Normal:')
for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j],end=' ')
    print()

matT = []  #cria uma mat transposta
for i in range(colunas):
    linha = []
    for j in range(linhas):
        linha.append(mat[j][i])
    matT.append(linha)
print('\nMatriz Transposta:')
for i in range(colunas):
    for j in range(linhas):
        print(mat[j][i],end=' ')
    print()

#compara pra ver se é simétrica
for i in range(linhas):
    for j in range(colunas):
       if mat[i][j] != matT[i][j]:
           simetrica = False

if simetrica:
    print("\nÉ simétrica!!")
else:
    print("\nNão é simétrica!!")


#Exercicio 08
matUm = []
matDois = []
linhas = int(input("Informe o nº de linhas:"))
colunas = int(input("Informe o nº de colunas:"))
for i in range(1,3):
    print(f'\nMatriz {i}:')
    if i == 1:
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                n = int(input("Digite um número:"))
                linha.append(n)
            matUm.append(linha)

        for i in range(linhas):
            for j in range(colunas):
                print(matUm[i][j],end=' ')
            print()
    else:
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                n = int(input("Digite um número:"))
                linha.append(n)
            matDois.append(linha)

        for i in range(linhas):
            for j in range(colunas):
                print(matDois[i][j],end=' ')
            print()
mat = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        soma = matUm[i][j]-matDois[i][j]
        linha.append(soma)
    mat.append(linha)

print('\nMatriz substraida:')
for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j],end=' ')
    print()
'''

#Exercicio 09 - nao entendi como proceder a parte dos produto
matA = []
matB = []
mat = []
linhA = int(input("Informe o nº de linhas [Matriz A]:"))
colA = int(input("Informe o nº de colunas [Matriz A]:"))
linhB = colA
colB = int(input("Informe o nº de colunas [Matriz B]:"))

for i in range(1,3):
    if i == 1:
        print(f'\nMatriz A:')
        for i in range(linhA):
            linha = []
            for j in range(colA):
                n = int(input("Digite um número:"))
                linha.append(n)
            matA.append(linha)

        for i in range(linhA):
            for j in range(colA):
                print(matA[i][j],end=' ')
            print()
    else:
        print(f'\nMatriz B:')
        for i in range(linhB):
            linha = []
            for j in range(colB):
                n = int(input("Digite um número:"))
                linha.append(n)
            matB.append(linha)

        for i in range(linhB):
            for j in range(colB):
                print(matB[i][j],end=' ')
            print()
mat = []
product = 0
for i in range(linhA):
    linha = []
    for j in range(colB):
        for k in range(linhB):
            product += matA[i][k] * matB[k][j]
            linha.append(product)
        mat.append(linha)
        product = 0
print()
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print()
