'''Livraria_Itens=['Livros', 'Artigos', 'Revistas']
Livraria=[
[ ['O Sol é para todos',['Harper Lee', 'Beatriz Horta'], 55.9] , ['O Pequeno Príncipe',['Antoine de SaintExupéry'], 45.6] ],
[ ['Artigo Nature', 32.9], ['Artigo Artigado', 99.99 ]],
[ ['Super Interessante', 'Editora Nova', 15.4], ['Mente e Saúde', 'Editora Abril', 19.8] ]
 ]


def livraria(itens,liv):
    for i in range(len(itens)):
        print(f'---------- {itens[i]} ----------')
        if itens[i] == 'Livros':
            livros = liv[i]
            for l in livros:
                print(f'Nome: {l[0]}')
                if len(l[1]) == 1:
                    print(f'Autor(a): {l[1][0]}')
                else:
                    print(f'Autores:',end=' ')
                    for a in range(len(l[1])):
                        
                        if a == len(l[1])-1:
                            print(l[1][a])
                        else:
                            print(l[1][a], end=', ')
                print(f'Preço: R${l[2]}')
                print()
                
        elif itens[i] == 'Artigos':
            artigos = liv[i]
            for l in artigos:
                print(f'Nome: {l[0]}')
                print(f'Preço: R${l[1]}')
                print()

        elif itens[i] == 'Revistas':
            revistas = liv[i]
            for l in revistas:
                print(f'Nome: {l[0]}')
                print(f'Editora: {l[1]}')
                print(f'Preço: R${l[2]}')
                print()
livraria(Livraria_Itens,Livraria)'''



'''def produtos(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        return lista[0]
    return lista[0] * produtos(lista[1:])

L = [1,2,3,4,5]
print(produtos(L))'''



def consecutivo(lista):
    if len(lista) == 0:
        return True
    if len(lista) == 1:
        return True
    if lista[1] == lista[0]+1:
        return consecutivo(lista[1:])
    return False

L = [1,2,3,4,5]
print(consecutivo(L))


