'''
estoque_frutas = {'banana': 50, 'laranja': 12, 'melancia': 25, 'maça': 73}
print(estoque_frutas)
print()

for fruta in estoque_frutas:
    chave = fruta
    valor = estoque_frutas[chave]
    print(f'Temos {valor} items do elemento {chave} no estoque.')

total = 0
for valor in estoque_frutas.values():
    total += valor
print(f'Temos {total} frutas no estoque.')
print()

for akey in estoque_frutas:
    print(f'Quantidade da fruta {akey} é {estoque_frutas[akey]}.')
print()

for k in estoque_frutas.items():
    print("Par Chave-Valor: ", k)
print()


ks = list(estoque_frutas.keys())
ks.append('kiwi')
print("Lista de frutas:",ks)
for k in ks:
    print(k, ": ", estoque_frutas.get(k,0))
print()




frutas_preço = {'banana': 3.90, 'laranja': 2.50, 'melancia': 7.99, 'maça': 1.75}
print(list(frutas_preço.keys()))
print(list(frutas_preço.values()))
print(list(frutas_preço.items()),'\n')

for (k,v) in frutas_preço.items():
    print(f'Fruta {k} é vendida por {v}.')
print()
for k in frutas_preço:
    print(f'Fruta {k} é vendida por {frutas_preço[k]}.')
print()
'''
'''
IGNORE = ' .,;:?!\t\n'
def main():
    frase = input("Digite uma frase: ")
    letra = {}

    for c in frase:
        if c not in IGNORE:
            if c in letra:
                letra[c] += 1
            else:
                 letra[c] = 1
    print(letra)
    keylist = list(letra.keys())
    keylist.sort()
    for i in keylist:
        print(i,":",letra[i])

main()
'''
'''
d1 = {"Joao": 10, "Maria":20}
d2 = d1.copy()
d2["Pedro"] = 30
d1["Joao"] = 40
print(d1)
# saída: {"Joao": 40,"Maria": 20}
print(d2)
# saída: {"Pedro": 30,"Joao": 10,"Maria": 20}
'''
'''

d1 = {"Joao":[1,2], "Maria":[3,4]}
d2 = d1.copy()
d2["Pedro"]=[5,6]
d1["Joao"] += [3]
print(d1)
# saída: {"Joao": [1, 2, 3], "Maria": [3, 4]}
print(d2)
# saída{"Pedro": [5, 6],"Joao": [1, 2,3],"Maria":[3, 4]}  NAO DEVIA TER O 3 NO JOAO
'''


