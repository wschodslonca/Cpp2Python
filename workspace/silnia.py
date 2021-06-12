# from silnia.cpp to silnia.py

def IterateFactorial(n):
    suma = 1
    i = 1
    while i <= n:
        suma *= i
        i += 1
    return suma


def RecursiveFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * RecursiveFactorial(n-1)


def main():
    n = 6
    print("Iteracyjnie ", IterateFactorial(n), '\n', sep='', end='')
    print("Rekurencyjnie ", RecursiveFactorial(n), sep='', end='')
    return 0


if __name__ == '__main__':
    main()
