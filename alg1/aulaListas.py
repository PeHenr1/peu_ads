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


#Exercicio 11
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
    
mais = 0
nMais = 0
maiores = []
for numero in range(len(lista)):
    cont = 0
    #print(f'lista[numero]: {lista[numero:]};')
    for n in lista[numero:]:
        if lista[numero] == n:
            cont += 1
            nMais = n
    if cont >= mais:
        #print('entrei')
        mais = cont
        maiores.append(nMais)
print(maiores,'aparecem',mais,'vezes')


#Exercicio 12
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
print(f'Lista: {lista}')
x = int(input("Qual nº deseja remover a primeira ocorrência?:"))
deletou = False
for i in range(len(lista)-1):  #for i in range(len(lista)-1,-1,-1): inverso
    if lista[i] == x and deletou == False:
        del lista[i]
        deletou = True
print(f'Lista: {lista}')
   

#Exercicio 13
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
print(f'Lista: {lista}')
x = int(input("Qual nº deseja remover a última ocorrência?:"))
deletou = False
for i in range(len(lista)-1,-1,-1): 
    if lista[i] == x and deletou == False:
        del lista[i]
        deletou = True
print(f'Lista: {lista}')


#Exercicio 14
lista = []
N = int(input("Quantidade de elementos:"))
for i in range(N):
    lista.append(int(input("Digite um número:")))
print(f'Lista: {lista}')
x = int(input("Qual nº deseja remover todas ocorrências?:"))
for i in range(len(lista)-1,-1,-1): 
    if lista[i] == x:
        del lista[i]
print(f'Lista: {lista}')


#Exercicio 15 (talvez devesse ler e ignorar os espaços)
lista = []
string = input("Digite algo:")
while string != 'fim':
    lista.append(string)
    string = input("Digite algo ('fim' para encerrar):")
maior = len(lista[0])
menor = len(lista[0])
pMaior, pMenor = '',''
for s in range(len(lista[1:])):
    if len(lista[s]) > maior:
        pMaior = lista[s]
    elif len(lista[s]) < menor:
        pMenor = lista[s]
print(f"Maior string: '{pMaior}'\nMenor string: '{pMenor}'")


#Exercicio 16
lista = []
string = input("Digite algo:")
while string != 'fim':
    lista.append(string)
    string = input("Digite algo:")
x = input('Digite caractere para remover em tds as strings:')
print(f'Lista: {lista}')

for i in range(len(lista)-1,-1,-1):                #percorre a lista
    nova = ''
    deletou = False
    #print(f"len palavra '{lista[i]}' {len(lista[i])}")
    for letra in range(len(lista[i])):          #percorre a string
        if deletou == False:
            if len(lista[i]) == 1 :
                del lista[i]
            elif lista[i][letra] == x:
                nova = lista[i][:letra]+lista[i][letra+1:]
                lista[i] = nova
                deletou = True
                #print('?',nova)
print(f'Lista Nova: {lista}')


#Exercicio 17
agenda = [
    'Joelma',['99669-6969','93363-3663'],
    'Nina',['99999-9999'],
          ]
print("---------- AGENDA ---------- \n1 - Incluir contato e telefone\n2 - Alterar um telefone de um contaton\n3 - Excluir um telefone de um contato\n4 - Consultar os telefones de um contato\n5 - Listar todos os contatos e seus respectivos telefones\n6 – FIM\n----------------------------")
opc = int(input('Digite a opção desejada:'))
    
while opc != 6:
    if opc == 1:
        nome = input("Nome do contato:")
        # verificar se o contato ja está cadastrado
        agenda.append(nome)
        telefones = []
        tel = input("Telefone:")
        while tel != "":
            telefones.append(tel)
            tel = input("Telefone:")
        agenda.append(telefones)
        print('Contato adicionado com sucesso!!')

    if opc == 2:
        print('Contatos existentes:')
        for nomes in range(len(agenda)):
            if nomes % 2 == 0:
                print('-',agenda[nomes])
        nome = input("\nNome do contato:")
        for e in range(len(agenda)):
            if agenda[e] == nome:
                tel = agenda[e+1]
                print("Telefones:", end=' ')
                for t in range(len(tel)):
                    print(f'{t}){tel[t]}',end=', ')
                novoT = int(input("\nDigite o número que deseja alterar:"))
                for t in range(len(tel)):
                    if novoT == t:
                        telNovo = input("Telefone novo:")
                        agenda[e+1][t] = telNovo
                        print('Número alterado com sucesso!!')

    if opc == 3:
        print('Contatos existentes:')
        for nomes in range(len(agenda)):
            if nomes % 2 == 0:
                print('-',agenda[nomes])
        nome = input("\nNome do contato:")
        for e in range(len(agenda)-1,-1,-1):
            if agenda[e] == nome:
                tel = agenda[e+1]
                print("Telefones:", end=' ')
                for t in range(len(tel)):
                    print(f'{t}.{tel[t]}',end=' ')
                num = int(input("\nDigite o número que deseja excluir:"))
                for t in range(len(tel),-1,-1):
                    if num == t:
                        del agenda[e+1][t]
                        print('Número deletado com sucesso!!')
    
    if opc == 4:
        print('Contatos existentes:')
        for nomes in range(len(agenda)):
            if nomes % 2 == 0:
                print(agenda[nomes],end=', ')
        nome = input("\n\nNome do contato:")

        for e in range(len(agenda)-1,-1,-1):
            if agenda[e] == nome:
                tel = agenda[e+1]
                print('Telefones:', end =' ')
                for t in range(len(tel)):
                    print(f'{tel[t]}',end=' ')

    if opc == 5:
        for nomes in range(len(agenda)):
            if nomes % 2 == 0:
                print(f'\n{agenda[nomes]}',end=': ')
                tel = agenda[nomes+1]
                for t in range(len(tel)):
                    print(f'{tel[t]}',end=' ')


    print("\n\n---------- AGENDA ----------")
    print("1 - Incluir contato e telefone")
    print("2 - Alterar um telefone de um contato")
    print("3 - Excluir um telefone de um contato")
    print("4 - Consultar os telefones de um contato")
    print("5 - Listar todos os contatos e seus respectivos telefones")
    print("6 – FIM")
    print("----------------------------")
    opc = int(input('Digite a opção desejada:'))
'''
