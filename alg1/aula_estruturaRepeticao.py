'''
#Exercicio 01
soma = 0
qEle = 0
for i in range (13,74):
    soma = soma + i
    qEle = qEle + 1
print(soma,qEle, soma/qEle)
'''

'''
#Exercicio 02
somaIdade = 0
quant = 0
percent = 0

for i in range (1,5):
    idade = int(input("Digite uma idade:"))
    peso = float(input("Digite um peso:"))
    altura = int(input("Digite uma altura em cm:"))
    print()
    
    somaIdade = somaIdade + idade

    if peso > 90 and altura < 150:
        quant = quant + 1

    if 10 <= idade <= 30 and altura > 190:
        percent = percent + 1

print(f'\nA média das idades é {somaIdade/4}')
print(f'Há {quant} pessoas com peso > 90 e altura < 150cm')
print(f'{((percent/4)*100)}% das pessoas tem entre 10 e 30 anos e mais de 190cm')
'''

'''
#Exercicio 03
n = float(input("Digite uma nota: "))
quantA = 0
maior = 0
menor = 999999
media = 0
while n > 0:
    quantA += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    media = media + n
    n = float(input("Digite uma nota: "))
media = media/quantA
print(f'Há {quantA} alunos. Onde a maior nota é {maior} e a menor {menor} e a média da sala é {media}.')
'''

'''
#Exercicio 04
melhorTempo = 9999999999999999
nMelhorVolta = 0
tempoMedio = 0
for i in range (1,11):
    tempo = int(input("Digite o tempo da volta em segundos:"))

    if tempo < melhorTempo:
        melhorTempo = tempo
        nMelhorVolta = i

    tempoMedio = tempoMedio + tempo
tempoMedio = tempoMedio / 10
print(f'O melhor tempo foi a volta nº{nMelhorVolta} com duração de {melhorTempo}s!!')
print(f'O tempo médio das voltas foi de {tempoMedio}s.')
'''

'''
#Exercicio 05
num = 1
den = 1
soma = 0
print('S = ', end=' ')
for i in range (1,51):
    if i == 50:
        print(f'{num}/{den}', end=' = ')
    else:
        print(f'{num}/{den}', end=' + ')
    soma = soma + (num/den)
    num += 2
    den += 1
print(soma)
'''
