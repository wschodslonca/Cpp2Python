# from nwd.cpp to nwd.py

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
    name = ""
    print("Podaj imie", '\n', sep='', end='')
    name = input()
    print("Witaj ", name, '\n', sep='', end='')
    print("wynik NWD liczb ", number1, " oraz ", number2, " : ", nwd(number1,number2), '\n', sep='', end='')


if __name__ == '__main__':
    main()
