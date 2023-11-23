##### CLASSES #####
class Contato:
    nome = ''
    telefones = []

    def adicionar_telefone(self,nome,numeros):
        self.nome = nome
        self.telefones = numeros

    def alterar_nome(self,nome):
        self.nome = nome

    def alterar_telefone(self,numeros):
        self.telefones = numeros

    def exibir_contato(self):
        print(f'Nome: {self.nome}')
        if self.telefones != []:
            print('Telefones:', end=' ')
            for tel in self.telefones:
                if self.telefones[-1] == tel:
                    print(f'{tel}')
                else:
                    print(f'{tel}', end=', ')
                
            print()
        else:
            print('Nenhum telefone registrado para esse contato.\n')

class Agenda:
    contatos = []

    def incluir_contato(self,contato):
        self.contatos.append(contato)

    def buscar_contato(self,nome):
        for c in self.contatos:
            if nome == c.nome:
                return c
        return -1

    def excluir_contato(self,contato):
        for i in range(len(self.contatos)):
            if self.contatos[i] == contato:
                pos = i
        del self.contatos[pos]

##### FUNÇÕES #####
def adicionarContato():
    novo_contato = Contato()
        
    nome = input('Novo contato:')
    novo_contato.alterar_nome(nome)

    tels = [] 
    n = input('Telefone(s):')
    while n != "":
        if int(n) not in tels:
            tels.append(int(n))
        else:
            print('Número já existente.')
        n = input('Telefone(s):')
    novo_contato.adicionar_telefone(nome,tels)
        
    agenda = Agenda()
    agenda.incluir_contato(novo_contato)

    '''print(novo_contato.nome)
    print(novo_contato.telefones)
    print(novo_contato.exibir_contato())'''

def exibe():
    agenda = Agenda()
     
    if agenda == None: ##como funcionaria
        print('Lista de contatos vazia')
    else:
        nome = input('Nome do contato:')
        nomeE = agenda.buscar_contato(nome)
        if nomeE == -1:
            print('Contato não encontrado.')
        else:
            nomeE.exibir_contato()

def deleta():
    agenda = Agenda()
     
    if agenda == None: ##como funcionaria
        print('Lista de contatos vazia')
    else:
        nome = input('Nome do contato:')
        nomeE = agenda.buscar_contato(nome)
        if nomeE == -1:
            print('Contato não encontrado.')
        else:
            agenda.excluir_contato(nomeE)
            print('Contato deletado com sucesso!!!\n')

def menu():
    print('\n---------- MENU ----------')
    print('1. Adicionar contato')
    print('2. Exibir contato')
    print('3. Excluir contato')
    print('4. Alterar contato')
    print('5. Sair')
    print('--------------------------')
    opc = int(input('\nEscolha uma opção:'))

    if opc == 1:
        adicionarContato()
        print('Contato salvo com sucesso!!!\n')

    if opc == 2:
       exibe()

    if opc == 3:
        deleta()

    if opc == 4:
        r = input('Contato que deseja alterar: ')
        agenda = Agenda()

        if agenda == None: ##como funcionaria
            print('Lista de contatos vazia')
        else:
            nomeE = agenda.buscar_contato(r)
            if nomeE == -1:
                print('Contato não encontrado.')
            else:
                #nomeE.exibir_contato()
                    
                r = input('Alterar <nome> ou <telefones>?')
                if r == 'nome':
                    novo = input('Novo nome para o contato:')
                    nomeE.alterar_nome(novo)
                    print('Nome alterado com sucesso!!!')
                elif r == 'telefones':
                    print('still in progress.....')
                else:
                    print('Comando inválido')

    if opc == 5:
        exit()
    menu()
        
##### PROG PRINC #####
menu()
