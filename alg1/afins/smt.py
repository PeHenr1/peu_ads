import random

temas = ['Cor', 'Animal', 'Profissão']
cor = ['rosa','roxo','amarelo','caramelo']
animal = ['cachorro','zebra']
profissao = ['dentista','prostituta','otorrino']

temaSorteado = random.choice(temas)
tentativas = 5

if temaSorteado == 'Cor':
    palavraSorteada = random.choice(cor)
elif temaSorteado == 'Animal':
    palavraSorteada = random.choice(animal)
elif temaSorteado == 'Profissão':
    palavraSorteada = random.choice(profissao)

ganhou = False
perdeu = False
codificada = ''  #mostra na tela
checar = ''      #checa se é igual a palavra sorteada pra sair do laço
for l in palavraSorteada:
    codificada += '_ '
    checar += '_'

print(f'Tema: {temaSorteado}, palavra: {palavraSorteada}, codificado: {codificada}')
print(f'Você tem {tentativas} chances de errar. Boa sorte')
letra = input('Escolha uma letra:')
while ganhou == False or perdeu == False:
    if letra not in palavraSorteada:
        tentativas = tentativas - 1
        print(f'PÉÉÉÉÉÉ. Errou. Você tem mais {tentativas} tentativas')
        if tentativas == 0:
            perdeu = True
            print('buceta',perdeu)
        else:
            letra  = input('Escolha uma letra:')
    else:
        for e in range(len(palavraSorteada)):
            pos = 0
            if letra == palavraSorteada[e]:
                checar = checar[:e] + letra + checar[e+1:]
                pos = e*2
                codificada = codificada[:pos] + letra + codificada[pos+1:]
        print(codificada, ' ',checar)
        if checar == palavraSorteada:
            ganhou = True
        else:
            letra = input('\nEscolhe outra letra:')

if ganhou:
    print('parabéns fera')
elif perdeu:
    print('se fudeu')
