jogoDaVelha = [
    ["   |   |   "], #0    1 5 9 
    ["---+---+---"],
    ["   |   |   "], #2
    ["---+---+---"],
    ["   |   |   "]  #4
    ]

jogada = 0

def mostrar(jogada):  
    for linha in jogoDaVelha:
        for x in linha:
            print(x)
    turno(jogada)

def turno(jogada):
    if jogada == 0:
        s = 'x'
        n = 1
    elif jogada == 1:
        s = 'o'
        n = 2
    player = int(input(f'\nJOGADOR {n}: '))
    jogador(player,jogada,s)

def verifica(s):
    veredito = ''
    
    # verifica na horizontal
    for linha in range(0,len(jogoDaVelha),2): 
        li = str(jogoDaVelha[linha])
        li = li[2:13]
        print(f'li1:{li[1]}, li5{li[5]}, li9:{li[9]}')
        if li[1] == s and li[5] == s and li[9] == s:
            veredito = s
            
    # verifica na vertical
    i = 1
    liDescart = str(jogoDaVelha[linha])
    liDescart = liDescart[2:13]
    while i < len(liDescart):
        if liDescart[i] == s and liDescart[i] == s and liDescart[i] == s:
            veredito = s
        i += 1

    # verifica diagonal
    linhaUm = str(jogoDaVelha[0])
    linhaUm = linhaUm[2:13]
    linhaDois = str(jogoDaVelha[2])
    linhaDois = linhaDois[2:13]
    linhaTres = str(jogoDaVelha[4])
    linhaTres = linhaTres[2:13]
    if (linhaUm[1] == s and linhaDois[5] == s and linhaTres[9] == s) or (linhaTres[1] == s and linhaDois[5] == s and linhaUm[9] == s):
        veredito = s
    
    if veredito != '':
        print(f'{s} ganhou')
    
def jogador(player,jogada,s):
    if player == 1:
        linha = str(jogoDaVelha[0])
        linha = linha[2:13]
        linha = linha[:1] + s + linha[2:]

        lista = []
        lista.append(linha)
        jogoDaVelha[0] = lista

    elif player == 2:
        linha = str(jogoDaVelha[0])
        linha = linha[2:13]
        linha = linha[:5] + s + linha[6:]

        lista = []
        lista.append(linha)
        jogoDaVelha[0] = lista

    elif player == 3:
        linha = str(jogoDaVelha[0])
        linha = linha[2:13]
        linha = linha[:9] + s + linha[10:]

        lista = []
        lista.append(linha)
        jogoDaVelha[0] = lista

    elif player == 4:
        linha = str(jogoDaVelha[2])
        linha = linha[2:13]
        linha = linha[:1] + s + linha[2:]

        lista = []
        lista.append(linha)
        jogoDaVelha[2] = lista

    elif player == 5:
        linha = str(jogoDaVelha[2])
        linha = linha[2:13]
        linha = linha[:5] + s + linha[6:]

        lista = []
        lista.append(linha)
        jogoDaVelha[2] = lista

    elif player == 6:
        linha = str(jogoDaVelha[2])
        linha = linha[2:13]
        linha = linha[:9] + s + linha[10:]

        lista = []
        lista.append(linha)
        jogoDaVelha[2] = lista

    elif player == 7:
        linha = str(jogoDaVelha[4])
        linha = linha[2:13]
        linha = linha[:1] + s + linha[2:]

        lista = []
        lista.append(linha)
        jogoDaVelha[4] = lista

    elif player == 8:
        linha = str(jogoDaVelha[4])
        linha = linha[2:13]
        linha = linha[:5] + s + linha[6:]

        lista = []
        lista.append(linha)
        jogoDaVelha[4] = lista

    elif player == 9:
        linha = str(jogoDaVelha[4])
        linha = linha[2:13]
        linha = linha[:9] + s + linha[10:]

        lista = []
        lista.append(linha)
        jogoDaVelha[4] = lista

    if jogada == 0:
        jogada = 1
    else:
        jogada = 0

    verifica(s)
    mostrar(jogada)
    

mostrar(jogada)

'''
- verificar se o espaço está vazio (nao pode botar onde ja tem)
- fazer parada quando um player ganhar
- fazer parada quando der velha
- perguntar se quer jogar de novo, se sim, resetar e mandar bala
'''
