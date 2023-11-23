def ExisteArquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

#Exercicio 01
def tamanho(arquivo):
    tam = 0
    if ExisteArquivo(arquivo):
        arq = open(arquivo,"r")
        for linha in arq:
            tam += 1
        arq.close()
    return tam

#Exercicio 02
def caracteres(arquivo):
    carac = 0
    if ExisteArquivo(arquivo):
        arq = open(arquivo,"r")
        for linha in arq:
            for c in linha:
                carac += 1
        arq.close()
    return carac

print('O arquivo possui',tamanho('exeUmDois.txt'), "linhas")
print('O arquivo possui',caracteres('exeUmDois.txt'), "caracteres")

####################################################################
