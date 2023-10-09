'''
def termo_fibonacci(n):
    if n <= 1:
        return n
    else:
        return termo_fibonacci(n-1) + termo_fibonacci(n-2)

nro=int(input('Digite o termo da sequência de Fibonacci: '))
if nro < 0:
    print("O número deve ser maior ou igual a zero!")
else:
    print(termo_fibonacci(nro))
'''

def sequencia_fibonacci(a, b, n):
    print(a," ",end="")
    if b < n:
        sequencia_fibonacci(b, a + b, n)
nro=int(input('Digite o valor de parada da sequência de Fibonacci: '))
sequencia_fibonacci(0,1,nro)
