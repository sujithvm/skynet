__author__ = 'Archana V Menon, Sujith V'

def fibonacci(N):

    if N == 0 : return []
    if N == 1 : return [0]

    fib = [0, 1]
    for i in range(2, N):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib

