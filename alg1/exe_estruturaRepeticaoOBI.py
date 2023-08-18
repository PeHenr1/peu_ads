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



