def ExisteArquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

dicionario = {
    'SC180100':('Aluno 1','aluno1@ifsp.edu.br'),
    'SC180200':('Aluno 2','aluno2@ifsp.edu.br'),
    'SC180300':('Aluno 3','aluno3@ifsp.edu.br')
    }

if len(dicionario):
    arq = open("cad_alunos.txt","w")
    for aluno in dicionario:
        RA = aluno
        nome, email = dicionario[aluno]
        linha = RA + "\t" + nome + "\t" + email + "\n"
        arq.write(linha)
    arq.close()
    print("Arquivo gravado com sucesso")


# recuperando com o FOR (ler)
dic = {}
existe = ExisteArquivo("cad_alunos.txt")
if existe:
    ref_arq = open("cad_alunos.txt","r")
    for linha in ref_arq:
        linha = linha[:len(linha)-1] #remove o \n
        aluno = linha.split("\t")
        chave = aluno[0]
        nome = aluno[1]
        email = aluno[2]
        dic[chave] = [nome,email]
    ref_arq.close()
    print(dic)

# recuperando com o WHILE
dic2 = {}
existe = ExisteArquivo("cad_alunos.txt")
if existe:
    ref_arq = open("cad_alunos.txt","r")
    linha = ref_arq.readline()
    while linha != "":
        linha = linha[:len(linha)-1] #remove o \n
        aluno = linha.split("\t")
        chave = aluno[0]
        nome = aluno[1]
        email = aluno[2]
        dic2[chave] = (nome,email,)
        linha = ref_arq.readline()
    ref_arq.close()
    print(dic2)



    
