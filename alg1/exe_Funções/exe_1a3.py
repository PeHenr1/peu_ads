#Exercicio 01
def inteiroPositivo(n):
    if n.isdigit():
        return True
    else:
        return False

    
#Exercicio 02
def inteiro(n):
    if n[0] == '-':
        n = n[1:]
    if n.isdigit():
        return True
    else:
        return False

#Exercicio 03
def real(n):
    retorno = True
    abc = 'abcdefghijklmnopqrstuvwxyzçâã'
    simbolos = '+-*/&%$#@!()='
    if n[0] == '-':
        n = n[1:]
    if n.isdigit():
        return True
    else:
        for e in range (len(n)):
            print(n[e])
            if n[e] == '.':
                for ee in n[e+1:]:
                    if ee == '.':
                        return False
            elif n[e] in abc:
                return False
            elif n[e] in simbolos:
                return False
    return retorno
        

string = input("Digite:")
#print(inteiroPositivo(string))
#print(inteiro(string))
print(real(string))

    
