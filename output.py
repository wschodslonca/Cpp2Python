# from nwd.cpp to output.py

def nwd(a, b):
    i = -5
    while i < -1:
        if i % 2 == 0:
            print(i, '\n', sep='', end='')
        i += 1
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def main():
    powitanie = "witaj! "
    number1 = 72
    number2 = 84
    number1 = 72
    print(powitanie, '\n', "a oto wynik: ", '\n', nwd(number1,number2), '\n', sep='', end='')
    print(powitanie, '\n', "a oto wynik: ", '\n', nwd(number1,number2), '\n', sep='', end='')


if __name__ == '__main__':
  main()