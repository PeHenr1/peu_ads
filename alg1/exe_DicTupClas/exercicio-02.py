alunos = {
    ('3039048','Pedro H Aissa'):('27/06/2004',['email_1'],['tel_1']),
    ('3038754','Fulano De Tal'):('30/02/2002',['email_4','email_6'],['tel_9','tel_x','tel_p'])
    }

def mostrarNomes():
    for i, a in enumerate(alunos):
        ra, nome = a
        if i == len(alunos)-1:
            print(f'{ra}:{nome}')
        else:
            print(f'{ra}:{nome} || ',end='')

def cadastrar():
    ra = input("RA: ")
    nome = input("Nome: ")
    existe = False
    for a in alunos:
        if ra == a[0] or nome == a[1]:          
            existe = True
            
    if existe == False:
        chave = (ra,nome,)

        datanasc = input("Data de Nascimento (dd/mm/aa): ")
        
        emails = []
        email = input("Email:")
        while email != "":
            if email not in emails:
                emails.append(email)
            email = input("Email:")
            
        telefones = []
        tel = input("Tel:")
        while tel != "":
            if int(tel) not in telefones:
                telefones.append(int(tel))
            tel = input("Tel:")

        valor = (datanasc,emails,telefones,)

        alunos[(chave)] = valor
        print("Aluno(a) cadastrado(a) com sucesso!!!")
        
    else:
        print("RA ou Nome digitados já existentes. Por favor, insira outros valores... \n")
        cadastrar()


def exibir(x):
    for a in alunos:
        if x == a[1] or x == a[0]:          
            ra = a[0]
            nome = a[1]
            dados = alunos[a]
            
            data = dados[0]
            emails = dados[1]
            tels = dados[2]

    print(f"\nRA: {ra}")
    print(f"    Nome: {nome}")
    print(f"    Data de Nascimento: {data}")
    if len(emails) == 1:
        print("    E-mail:", end=' ')
        print(emails[0])
    else:
        print("    E-mails:", end=' ')
        for e in emails:
            if e == emails[-1]: 
                print(e)
            else:
                print(e, end=', ')
    if len(tels) == 1:
        print("    Telefone:", end=' ')
        print(tels[0])
    else:
        print("    Telefones:", end=' ')
        for t in tels:
            if t == tels[-1]: 
                print(t)
            else:
                print(t, end=', ')
    print("__________________________")

def deletar(x):
    for a in alunos:
        if x == a[1] or x == a[0]:
            dele = (a[0],a[1],)
    del alunos[dele]
    print("Aluno(a) deletado(a) com sucesso!!!")
    print("_________________________")

def alterar(x):
    exibir(x)
    for a in alunos:
        if x == a[1] or x == a[0]:
            chave = (a[0],a[1],)
            dados = list(alunos[a])

    r = int(input('\nDeseja alterar:\n  1. Data de Nascimento\n  2. E-mail(s)\n  3. Telefone(s)\n  4. Sair\n:'))
    print()
    if r == 1:
        novadata = input("Informe a nova data de nascimento:")
        dados[0] = novadata

        
    elif r == 2:
        for e in range(len(dados[1])):
            if e == len(dados[1])-1:
                print(f'({e}) {dados[1][e]}')
            else:
                print(f'({e}) {dados[1][e]}',end=' | ')
        re = int(input('\n  1. Adicionar\n  2. Remover\n  3. Sair\n:'))
        if re == 1:
            novoemail = input("Novo email:")
            while novoemail != "":
                if novoemail not in dados[1]:
                    dados[1].append(novoemail)
                else:
                    print("Email existente...")
                novoemail = input("Novo email:")          
        elif re == 2:
            q = int(input("Digite o nº do email que deseja remover:"))
            del dados[1][q]
        elif re == 3:
            alterar(x)

            
    elif r == 3:
        for t in range(len(dados[2])):
            if t == len(dados[2])-1:
                print(f'({t}) {dados[2][t]}')
            else:
                print(f'({t}) {dados[2][t]}',end=' | ')
        rt = int(input('\n  1. Adicionar\n  2. Remover\n  3. Sair\n:'))
        if rt == 1:
            novotel = input("Novo telefone:")
            while novotel != "":
                if novotel not in dados[2]:
                    dados[2].append(novotel)
                else:
                    print("Telefone existente...")
                novotel = input("Novo telefone:")
        elif rt == 2:
            q = int(input("Digite o nº do telefone que deseja remover:"))
            del dados[2][q]
        elif rt == 3:
            alterar(x)
            
    elif r == 4:
        menu()
    
        
    alunos[(chave)] = dados     
    print("Dados alterados com sucesso!!!")
    print("____________________________________")

    

def exibir_todos():
    for a in alunos:
        dados = alunos[a]
        data = dados[0]
        emails = dados[1]
        tels = dados[2]

        print(f"\nRA: {a[0]}")
        print(f"    Nome: {a[1]}")
        print(f"    Data de Nascimento: {data}")
        if len(emails) == 1:
            print("    E-mail:", end=' ')
            print(emails[0])
        else:
            print("    E-mails:", end=' ')
            for e in emails:
                if e == emails[-1]: 
                    print(e)
                else:
                    print(e, end=', ')
        if len(tels) == 1:
            print("    Telefone:", end=' ')
            print(tels[0])
        else:
            print("    Telefones:", end=' ')
            for t in tels:
                if t == tels[-1]: 
                    print(t)
                else:
                    print(t, end=', ')
                    
        print('--------------------------------------')
        
 

def menu():
    print('\n¨¨¨¨¨¨¨¨¨¨ MENU ¨¨¨¨¨¨¨¨¨¨')
    print('1. Cadastrar aluno')
    print('2. Exibir aluno')
    print('3. Deletar aluno')
    print('4. Alterar aluno')
    print('5. Exibir todos os alunos')
    print('6. Sair')
    print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
    opcao()

def opcao():
    opc = int(input('Escolha uma opção:'))
    print()
    
    if opc == 1:
        print("_____ CADASTRAR ALUNO _____")         
        cadastrar()

    if opc == 2:
        mostrarNomes()
        a = input(":")
        print("\n_____ DADOS DO ALUNO _____")
        exibir(a)

    if opc == 3:
        mostrarNomes()
        print("\n_____ DELETAR ALUNO _____")
        a = input(":")
        deletar(a)

    if opc == 4:
        mostrarNomes()
        print("\n_____ ALTERAR DADOS DO ALUNO _____")
        a = input(":")
        alterar(a)

    if opc == 5:
        print("__________ DADOS DOS ALUNOS __________")
        exibir_todos()

    if opc == 6:
        exit()

    menu()



############ PROGRAMA PRINCIPAL ############     
menu()
