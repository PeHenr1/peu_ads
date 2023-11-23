def ExisteArquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

def ler_dados(dic):
    if len(dic):
        if ExisteArquivo("loja_produtos.txt"):
            arq = open("loja_produtos.txt","r")
            for linha in arq:
                linha = linha[:len(linha)-1] #remove o \n
                produto = linha.split("\t")
                chave = produto[0]
                nome = produto[1]
                preço = produto[2]
                quant = produto[3]
                dic[chave] = [nome,(preço,quant,)]
            arq.close()
    else:
        print("Não há dados.")
                

def inserir(dic):
    codigo = int(input("Código do produto: "))
    info = []
    nome = input("Produto: ")
    preço = float(input("Preço: "))
    quant = int(input("Quant. Estoque: "))
    tupla = (preço,quant,)
    info.append(nome)
    info.append(tupla)
    dic[codigo] = info
    
    print("Produto cadastrado com sucesso!!!")
    

def gravar_dados(dic):
    if len(dic):
        arq = open("loja_produtos.txt","w")
        for aluno in dicionario:
            RA = aluno
            nome, email = dicionario[aluno]
            linha = RA + "\t" + nome + "\t" + email + "\n"
            arq.write(linha)
        arq.close()
        print("Arquivo gravado com sucesso")
    else:
        print("Dicionário vazio")

dicionario = {
    1 : [ "Camiseta" , (19.99, 50)],
    2 : [ "Tênis" , (49.99, 30)],
    3 : [ "Boné" , (9.99, 100)]
}

dicio = {}
ler_dados(dicionario)
#menu()
inserir(dicio)
gravar_dados(dicio)
