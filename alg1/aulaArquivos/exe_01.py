def ler_dados(dicionario):
    arq = open("turma_alg.txt","r")
    for linha in arq:
        linha = linha[:len(linha)-1]
        li = linha.split("\t")

        nome = li[0]
        prontuario = li[1]
        notas = []
        notas.append(float(li[2]))
        notas.append(float(li[3]))
        notas.append(float(li[4]))
        notas.append(float(li[5]))
        dicionario[prontuario]=[nome,notas]
    arq.close()    

def atualizaArq(dicionario):
    if len(dicionario):
        arq = open("turma_alg.txt","w")
        for aluno in dicionario:
            prontuario = aluno
            valor = dicionario[prontuario]

            nome = valor[0]
            n1,n2,n3,n4 = valor[1]

            linha = nome + "\t" + prontuario + "\t" + str(n1) +  "\t" + str(n2) +  "\t" + str(n3) +  "\t" + str(n4) + "\n"
            arq.write(linha)
        arq.close()
        
def menu():
    print("\n___________ TURMA ___________\n")
    print("1. Cadastrar aluno")
    print("2. Média dos alunos")
    print("3. Aluno média abaixo")
    print("4. Maior e menor média")
    print("5. Fechar programa")
    print("______________________________")

    opc = int(input("\nOpção: "))

    if opc == 1:
        print(cadastrar(turma))

    elif opc == 2:
        mediaalunos(turma)

    elif opc == 3:
        mediaabaixo(turma)

    elif opc == 4:
        maiormenor(turma)

    elif opc == 5:
        atualizaArq(turma)
        exit()

    else:
        print("Opção inválida.")

    menu()

def cadastrar(dicionario):
    print("\n_______ CADASTRAR ALUNO _______")
    nome = input("Nome: ")
    pront = input("Prontuario: ")
    n = []
    while len(n) != 4:
        num = float(input(f"Nota {len(n)+1}:"))
        n.append(num)
        
    if pront not in dicionario:
        dicionario[pront] = [nome,n]
        atualizaArq(turma) 
        return "Aluno cadastrado com sucesso."
         
    else:
        return "Aluno não cadastrado. Prontuario existente."
    

def mediaalunos(dicionario):
    if len(dicionario):
        print("\n_______ MÉDIA ALUNOS _______")
        for a in dicionario.values():
            nome = a[0]
            notas = a[1]
            media = 0
            for n in notas:
                media += n
            media = media/4
            print(f" - {nome}, Média: {media}")

def mediaabaixo(dicionario):
    naoTem = True
    if len(dicionario):
        print("\n_______ MÉDIA ALUNOS ABAIXO DE 6 _______")
        for a in dicionario.values():
            nome = a[0]
            notas = a[1]
            media = 0
            for n in notas:
                media += n
            media = media/4

            if media < 6:
                naoTem = False
                print(f" - {nome}, Média: {media}")
    if naoTem:
        print("Nenhum aluno ficou com média abaixo de 6.")

def maiormenor(dicionario):
    medias = []
    maiorM = []
    menorM = []
    if len(dicionario):
        print("\n_______ MAIOR E MENOR MÉDIA _______")
        for a in dicionario.values():
            nome = a[0]
            notas = a[1]
            media = 0
            for n in notas:
                media += n
            media = media/4
            medias.append([nome,media])

    maior, menor = medias[0][1], medias[0][1]

    for li in medias:
        if li[1] >= maior:
            maior = li[1]
            maiorM.append(li)
            
        elif li[1] <= menor:
            menor = li[1]
            menorM.append(li)

    print("\nMaior(es) média(s):")
    for n in maiorM:
        print(f" - {n[0]}, Média: {n[1]}")

    print("\nMenor(es) média(s):")
    for n in menorM:
        print(f" - {n[0]}, Média: {n[1]}")
    
            
            

turma = {}
ler_dados(turma)
menu()
