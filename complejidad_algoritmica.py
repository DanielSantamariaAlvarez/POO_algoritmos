import time
import sys

def factorial(n):
    respuesta = 1

    while n>1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_recursiva(n):
    if n == 1:
        return 1
    return n*factorial_recursiva(n-1)

if __name__ == '__main__':
    n = 100000
    sys.setrecursionlimit(n+10)
    inicio = time.time()
    factorial(n)
    fin = time.time()
    print(f'el tiempo de ejecución de factorial es {fin-inicio}')

    inicio2 = time.time()
    factorial_recursiva(n)
    fin2 = time.time()
    print(f'el tiempo de ejecución de factorial recursivo es {fin2-inicio2}')
