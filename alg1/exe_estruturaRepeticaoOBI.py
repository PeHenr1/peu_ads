'''
#Exercicio 01 - Robô
n, c, s = input("Número de estações, de comandos e da estação mais próxima à area devastada:").split(' ')
n = int(n)
c = int(c)
s = int(s)
pos = 1
qtde = 0
if 2 <= n <= 100:
    if pos == s:
        qtde += 1
    for i in range (1,c+1):
        comando = int(input("Movimentação:"))
        if comando == 1:
            #print(f'pra frente, pos {pos}')
            pos = pos + 1 
        elif comando == -1:
            pos = pos - 1
            #print(f'pra tras, pos {pos}') 
        if pos == s:
            qtde += 1
print(qtde)
'''    

'''
#Exercicio 02 - Cálculo Rápido
quantidade = 0
s = int(input("Digite um número :"))
if 1 <= s <= 36:
    a = int(input("Digite outro número [início do intervlo]:"))
    b = int(input("Digite outro número [fim do intervalo]:"))
    if a <= b and 1 <= a <= 10000 and 1 <= b <= 10000:
        for n in range (a,b+1):
            soma = 0
            while n > 0:
                resto = n % 10      #pega o ultimo numero
                n = (n - resto)/10  #pega os primeiro
                soma = soma + resto
                #print(f'soma = {soma}')
            if soma == s:
                quantidade = quantidade + 1
print(quantidade)
'''

'''
#Exercicio 3 - Potência
quant = int(input("Digite a quantidade de termos: "))
if 1 <= quant <= 10:
    soma = 0
    for i in range (1,quant+1):
        n = int(input("Digite um número:"))
        if 10 <= n <= 9999:
            potencia = n % 10
            n = (n - potencia)/10
            soma = soma + (n**potencia)
print(int(soma))
'''

'''
#Exercicio 04 - Progressões Aritméticas
quant = int(input("Quantos elementos serão?: "))
ant = 0
partes = 1
r = 0
rAnt = 0

for i in range (1,quant+1):
    n = int(input("Digite um número:"))
    if ant == 0:
        ant = n
    else:
        r = n - ant
        #print(f'r {r}')
        if rAnt == 0:
            rAnt = r
        else:
            #print(f'rAnt {rAnt}')
            if r != rAnt:
                partes += 1
                r = 0
                rAnt = 0
        ant = n
print(f'Há {partes} PA(s)')
#depois seria interessante separar as PAs
'''

'''
#Exercicio 05 - Maratona
n, m = input("Número de postos de água e distância máx. do atleta: ").split(' ')
n = int(n)
m = int(m)
postoAnt = 0
terminou = True
if 2 <= n <= 1000 and 1 <= m <= 42195:
    for i in range (n-1):
        p = int(input("Informe a posição do posto de água:"))
        if p <= 42195:  
            if (p - postoAnt) > m:
               terminou = False
            else:
                postoAnt = p
if terminou:
    print('S')
else:
    print('N')
'''

