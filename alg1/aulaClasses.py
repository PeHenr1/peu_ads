'''
class MeuExemplo:
    def __init__(self,valor):
        self.valor = valor

obj1 = MeuExemplo(33)
obj2 = MeuExemplo(49.5)
obj3 = MeuExemplo('Teste de Classe')
obj4 = MeuExemplo([2,6,7,'Lista em classes'])

print(obj1.valor)
print(obj2.valor)
print(obj3.valor)
print(obj4.valor)
'''

class Pessoa:
    def __init__(self,nome,idade): #(self,x,y)
        self.nome = nome           #self.nome = x
        self.idade = idade         #self.idade = y

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    def mostrarPessoa(self):
        print(f'\nNome: {aluno.nome}')
        print(f'Idade: {aluno.idade}')

class OutraPessoa:
    def __init__(self,nome,idade): #(self,x,y)
        self.nome = nome           #self.nome = x
        self.idade = idade         #self.idade = y

    @classmethod  #construtor personalidade da classe
    def criar_pessoa(cls,nome,idade):
        pessoa = cls(nome,idade)
        return pessoa
    

    def saudacao(self,tempo):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos. O dia está {tempo}."

#######################################################################    
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
            print('Telefones:')
            for tel in self.telefones:
                print(f'{tel},', end='')
        else:
            print('Nenhum telefone registrado para esse contato')

def Agenda:
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

# ---------- PROGRAMA PRINCIPAL ----------
########## Exemplo 01 ##########
'''
nome = input('Nome:')
idade = int(input('Idade:'))
#pessoa1 = Pessoa('Pedro',19)

pessoa1 = Pessoa(nome,idade)
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.saudacao())

pessoa2 = OutraPessoa("Pedro",19)
print(pessoa2.nome)
print(pessoa2.idade)
print(pessoa2.saudacao('chuvoso'))
'''

########## Exemplo 02 ##########
alunos = []
nome = input("Nome do aluno:")
while nome != "":
    idade = int(input('Idade do aluno:'))
    aluno = Pessoa(nome,idade)
    alunos.append(aluno)
    nome = input("Nome do aluno:")
#print(alunos) #printa lista com os OBJETOS

#jeito 01
'''for aluno in alunos:
    print(f'\nNome: {aluno.nome}')
    print(f'Idade: {aluno.idade}')'''
#jeito 2:
#cria um método na classe e chama ele no for
for aluno in alunos:
    aluno.mostrarPessoa()


########## Exemplo 03 ##########
