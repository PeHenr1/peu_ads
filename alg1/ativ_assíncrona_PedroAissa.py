disciplinas = {
    'APR1': ['Algoritmos e Programação', 400],
    'IWEB': ['Introdução a WEB',250],
    'MATC': ['Matemática para Computação',300],
    'ING1': ['Inglês para Computação 1',200],
    'CMOR': ['Comunicação Oral',250],
    'ARCO': ['Arquitetura Computacional',200],
    'FADM': ['Fundamentos de Administração',200],
    'BDD1': ['Banco de Dados 1',400],
    'BDD2': ['Banco de Dados 2',400]
    }

alunos = {
    ('3039048','Pedro H Aissa'):('27/06/2004',['email_1'],[['APR1',9.5],['IWEB',10],['MATC',8.5],['ARCO',9.5],['CMOR',7.9],['FADM',9.1]]),
    ('3038754','Fulano De Tal'):('30/02/2002',['email_4','email_6'],[['APR1',6],['MATC',9]])
}

def mostrarDisciplinas():
    for i, d in enumerate(disciplinas):
        if i == len(disciplinas)-1 or i == 4:
            print(f'| {d} |')
        else:
            print(f'| {d} ',end='')

def mostrarNomes_addNota():
    for i in alunos:
        print(f'► {i[1]}')

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

        notas = []
        valor = (datanasc,emails,notas,)

        alunos[(chave)] = valor
        print("Aluno(a) cadastrado(a) com sucesso!!!")
        
    else:
        print("RA ou Nome digitados já existentes. Por favor, insira outros valores... \n")
        cadastrar()

def alterar(x,y):
    exibir(x,y)
    for a in alunos:
        if y == a[1] and x == a[0]:
            chave = (a[0],a[1],)
            dados = list(alunos[a])

    r = int(input('\nDeseja alterar:\n  1. Data de Nascimento\n  2. E-mail(s)\n  3. Nota(s)\n  4. Sair\n:'))
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
        D = []
        for x in dados[2]:
            D.append(x[0])
        print("Disciplinas e notas:")
        for i in range(len(dados[2])):
            print(f'({i}) {dados[2][i][0]}: {dados[2][i][1]}')
            
        rt = int(input('\n  1. Adicionar\n  2. Remover\n  3. Sair\n:'))
        if rt == 1:
            sigla = input("Sigla da disciplina: ")
            while sigla != "":
                nova = []
                if sigla not in D and sigla in disciplinas:
                    nova.append(sigla)
                    n = float(input("Nota: "))
                    if 0 <= n <= 10:
                        nova.append(n)
                        dados[2].append(nova)
                else:
                    print("O aluno já tem uma nota nessa disciplina")
                sigla = input("Sigla da disciplina: ")
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



def deletar(x,y):
    achou = False
    for a in alunos:
        if y == a[1] and x == a[0]:
            dele = (a[0],a[1],)
            achou = True
    if achou:
        del alunos[dele]
        print("Aluno(a) deletado(a) com sucesso!!!")
    else:
        print("Aluno(a) não encontrado!!!")
   
    print("_________________________")


def exibir(x,y):
    achou = False
    for a in alunos:
        if y == a[1] and x == a[0]:          
            ra = a[0]
            nome = a[1]
            dados = alunos[a]
            
            data = dados[0]
            emails = dados[1]
            dn = dados[2]

            achou = True
    if achou == True:
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
        print("    Disciplinas e notas:")
        for i in dn:
            print(f'      {i[0]}: {i[1]}')
                
    else:
        print("RA ou Nome digitados não existentes.")
        menu()
            

    print("__________________________")

def exibir_todos():
    for a in alunos:
        dados = alunos[a]
        data = dados[0]
        emails = dados[1]
        dn = dados[2]

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
        print("    Disciplinas e notas:")
        for i in dn:
            print(f'       {i[0]}: {i[1]}')
                
                    
        print('--------------------------------------')
        
def add_disciplina_notas():
    mostrarDisciplinas()
    sigla = input("\nInforme a sigla da disciplina: ")
    if sigla in disciplinas:
        mostrarNomes_addNota()

        aluno = input("Aluno: ")
        while aluno != "":
            for a in alunos:
                if aluno == a[1]:
                    chave = (a[0],a[1],)
                    dados = list(alunos[a])
                    notas = dados[2]
                    
                    D = [] #só as disciplinas do aluno
                    for x in dados[2]:
                        D.append(x[0])
                    
                    novas = []
                    if sigla not in D:
                        novas.append(sigla)
                        n = float(input("Nota do aluno: "))
                        novas.append(n)

                        notas.append(novas)
                        dados[2] = notas
                        alunos[chave] = dados

                        print(f"Nota da disciplina {sigla} adicionada à {aluno}!!!")
                        print('_______________________________________')
                        menu()
                    else:
                        print("O aluno já possui uma nota nessa disciplina")

            aluno = input("\nAluno: ")
       
            
    else:
        print("Sigla existente.\n")
        add_disciplina_notas()
    

def menu():
    print('\n¨¨¨¨¨¨¨¨¨¨ MENU ¨¨¨¨¨¨¨¨¨¨')
    print('1. Cadastrar aluno')
    print('2. Alterar aluno')
    print('3. Deletar aluno')
    print('4. Consultar aluno')
    print('5. Exibir todos os alunos')
    print('6. Adicionar disciplina e notas ao aluno')
    print('7. Sair')
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
        print("\n_____ ALTERAR DADOS DO ALUNO _____")
        a = input("RA:")
        b = input("Nome:")
        alterar(a,b)

    if opc == 3:    
        mostrarNomes()
        print("\n_____ DELETAR ALUNO _____")
        a = input("RA:")
        b = input("Nome:")
        deletar(a,b)

    if opc == 4:
        mostrarNomes()
        a = input("RA:")
        b = input("Nome:")
        print("\n_____ CONSULTAR ALUNO _____")
        exibir(a,b)

    if opc == 5:
        print("__________ DADOS DOS ALUNOS __________")
        exibir_todos()

    if opc == 6:
        print("__________ ATRIBUIR AO ALUNO __________\n")
        add_disciplina_notas()

    if opc == 7:
        exit()

    menu()



############ PROGRAMA PRINCIPAL ############     
menu()
