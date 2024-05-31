def ExisteArquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

#f) 
def ler_dados(dic):    
    if ExisteArquivo("loja_produtos.txt"):
        arq = open("loja_produtos.txt","r")
        for linha in arq:
            linha = linha[:len(linha)-1] #remove o \n
            produto = linha.split("\t")
            chave = int(produto[0])
            nome = produto[1]
            preço = float(produto[2])
            quant = int(produto[3])
            dic[chave] = [nome,(preço,quant,)]
        arq.close()

#c)
def produto_minimo(dic,n):
    tem = False
    if len(dic):
        for p in dic:   
            codigo = p
            valor = dic[codigo]

            produto = valor[0]
            lista = list(valor[1])
            preço = lista[0]
            quant = lista[1]

            if quant <= n:
                tem = True
                print("--------------------")
                print(f"Código: {codigo}")
                print(f"Produto: {produto}")
                print(f"Preço: R${preço}")
                print(f"Estoque: {quant} unidades")
        if tem == False:
            print("Nenhum produto encontrado")
    else:
        print("Não há dados para se exibir.\n")

#b)
def venda(dic,cod,qCompra):
    valor = 0
    if cod in dic:        
        for p in dic:
            if p == cod:
                codigo = p
                valor = dic[codigo]

                produto = valor[0]
                lista = list(valor[1])
                preço = lista[0]
                quant = lista[1]

                if qCompra <= quant:
                    quant = quant - qCompra
                    valor = preço * qCompra

                    #atualiza dic
                    dic[cod] = [produto,(preço,quant,)]

                    return f"A compra deu R${valor}."
                    
                else:
                    return "Impossível realizar a venda"
    else:
        return "Código do produto não encontrado"


#d)
def alterar_preço(dic,cod,val):
    if cod in dic:        
        for p in dic:
            if p == cod:
                valor = dic[cod]
                
                produto = valor[0]
                lista = list(valor[1])
                quant = lista[1]

                dic[cod] = [produto,(val,quant,)]
                print("Produto alterado com sucesso!!!")
    else:
        print("Código do produto não encontrado")
                
#a)
def inserir(dic): 
    codigo = int(input("Código do produto: "))
    if codigo not in dic:
        info = []
        nome = input("Produto: ")
        preço = float(input("Preço: "))
        quant = int(input("Quant. Estoque: "))
        tupla = (preço,quant,)
        info.append(nome)
        info.append(tupla)
        dic[codigo] = info
        print("Produto cadastrado com sucesso!!!\n")
    else:
        print("Código informado já atribuído a outro produto.\n")
    

    

def mostrar_todos(dic):
    if len(dic):
        print("====================\n")
        for p in dic:   
            codigo = p
            valor = dic[codigo]

            produto = valor[0]
            lista = list(valor[1])
            preço = lista[0]
            quant = lista[1]

            print(f"Código: {codigo}")
            print(f"Produto: {produto}")
            print(f"Preço: R${preço}")
            print(f"Estoque: {quant} unidades\n")
            print("--------------------\n")
    else:
        print("Não há dados para se exibir.\n")
#e)
def gravar_dados(dic):
    if len(dic):
        arq = open("loja_produtos.txt","w")
        for p in dic:
            
            codigo = p
            valor = dic[codigo]

            produto = valor[0]
            lista = list(valor[1])
            preço = lista[0]
            quant = lista[1]

            linha = str(codigo) + "\t" + produto + "\t" + str(preço) + "\t" + str(quant) + "\n"
            arq.write(linha)
        arq.close()
        print("Arquivos gravados com sucesso!\nAdeus...")
    else:
        print("Dicionário vazio")

def menu():
    print("\n_____ Lojinha _____")
    print("1. Inserir produto")
    print("2. Efetuar venda")
    print("3. Exibir produtos abaixo do estoque mínimo")
    print("4. Alterar preço de produto")
    print("5. Mostrar todos produtos")
    print("6. Fim\n")

    opc = int(input("Opção: "))

    if opc == 1:
        inserir(dicionario)
        
    elif opc == 2:
        print("--- VENDA ---")
        c = int(input("Código do produto que deseja comprar: "))
        q = int(input("Quantidade: "))
        print(venda(dicionario,c,q))
        
    elif opc == 3:
        q = int(input("Quantidade: "))
        produto_minimo(dicionario,q)

    elif opc == 4:
        c = int(input("Código do produto: "))
        v = float(input("Novo preço: "))
        alterar_preço(dicionario,c,v)

    elif opc == 5:
        mostrar_todos(dicionario)

    elif opc == 6:
        gravar_dados(dicionario)
        exit()

    else:
        print("Digite uma opção válida")
    menu()
    

dicionario = {}
ler_dados(dicionario)
menu()
#inserir(dicio)
#gravar_dados(dicio)
