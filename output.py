# from nwd.cpp to output.py

def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def main():
    number1 = 72
    number2 = 84
    print("wynik: ", nwd(number1,number2), '\n', sep='', end='')


if __name__ == '__main__':
  main()