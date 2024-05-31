def ler_dados(dicionario):
    arq = open("cinema.txt",'r')
    for linha in dicionario:
        linha = linha[:len(linha)-1]
        filme = linha.split("\t")
        
        nomeF = filme[0]
        ano = int(filme[1])
        print('dados:',filme)

def atualizaArq(dicionario):
    if len(dicionario):
        for filme in dicionario:
            nome, ano = filme
            valor = dicionario[filme]
            listaator = valor[0]
            atores = ""
            for a in listaator:
                atores = atores + a + " "

            sessao = ""  
            salaHorario = valor[1]
            for s in salaHorario:
                sessao = sessao + s[0] + " "
                for h in s[1]:
                    sessao = sessao + h + " "
            print(salaHorario,sessao)
            
        
def menu():
    print("---------- CINEMA -----------")
    print("1. Cadastrar novo filme")
    print("2. Cadastrar atores em filme")
    print("3. Cadastrar salas e horários em filme")
    print("4. Cadastrar horários em sala de filme")
    print("5. Alterar os dados de um filme") #solicitar dado a ser alterado
    print("6. Remover filme")
    print("7. Remover atores de um filme")
    print("8. Remover salas de exibição de um filme")
    print("9. Remover horários de sala de exibição")
    print("10. Fechar programa")
    print("----------------------------")

    opc = int(input("\nOpção: "))

    if opc == 1:
        cadastrar(cinema)

    elif opc == 2:
        nomeFilme = input("Filme: ")
        anoLanç = int(input("Ano de lançamento: "))
        cadastrarAtor(cinema, nomeFilme, anoLanç)

    '''elif opc == 3:
        mediaabaixo(cinema)

    elif opc == 4:
        maiormenor(cinema)

    elif opc == 10:
        atualizaArq(cinema)
        exit()

    else:
        print("Opção inválida.")'''

    print()
    menu() 

def cadastrar(dicionario):
    print("\n_______ NOVO FILME _______\n")
    nome = input("Nome: ")
    ano = int(input("Ano de lançamento: "))
    chave = (nome,ano,)

    atores = []
    ator = input("Ator/Atriz: ")
    while ator != "":
        atores.append(ator)
        ator = input("Ator/Atriz: ")

    sessao = []  #sala e horarios
    
    nSala = input("Nº sala: ")
    while nSala != "":
        sala = []
        horarios = []
        h = input("Horário(HH:MM): ")
        while h != "":
            horarios.append(h)
            h = input("Horário(HH:MM): ")
            
        sala.append(nSala)
        sala.append(horarios)
        
        sessao.append(sala)
        nSala = input("\nNº sala: ")

    if chave not in dicionario:
        dicionario[chave] = [atores,sessao]
        atualizaArq(cinema)
        print("Filme cadastrado com sucesso!!")

def cadastrarAtor(dicionario,nome,ano):
    print("\n_______ ADICIONAR ATORES EM FILME _______\n")
    chave = (nome,ano,)
    if len(dicionario):
        for filme in dicionario:
            if filme == chave:
                print(dicionario[chave])
                atores = dicionario[chave][0]

                ator = input("Ator/Atriz: ")
                while ator != "":
                    atores.append(ator)
                    ator = input("Ator/Atriz: ")

                dicionario[chave][0] = atores
                print("Novo(s) ator(es) cadadastrado com sucesso.")        

##################################### TESTE
a = "nome ano#ator1 ator2 ator3$sala 1 19:00 23:00%sala 2 00:00 16:00"
chave = ""
atores = ""
sala1 = ""
sala2 = ""
for letra in range(len(a)-1,-1,-1):
    print(letra)
    print(a[letra])

    if a[letra] == "%":
        sala1 = a[len(a)-1:letra]
        print('porra',sala1)
        a = a[letra+1]
    
    if a[letra] == "#":
        chave = a[:letra]
        a = a[letra+1]
        
    if a[letra] == "$":
        atores = a[:letra]
        a = a[letra+1]
        
    
        

    
        
print(f"chave {chave}")
print(f"atores {atores}")
print(f"sala: {sala1}")
print(f"sala: {sala2}")
##########################################################33

cinema = {}
menu()


