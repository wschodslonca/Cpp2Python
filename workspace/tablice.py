# from tablice.cpp to tablice.py

def print_array(tab, n, name):
    print(name, ": ", '\n', sep='', end='')
    i = 0
    while i < n:
        print(i, ": ", tab[i], '\n', sep='', end='')
        i += 1


def main():
    tab1 = [0 for _ in range(4)]
    # 10 15 20 40
    tab1[0] = 10
    tab1[1] = tab1[0] + 5
    tab1[2] = 10 * 2
    tab1[3] = 80 / 2
    print_array(tab1,4,"tablica bez inicjalizacji")
    # 180 360 720
    tab2 = [180, 2 * 180, 4 * 180]
    print_array(tab2,3,"tablica z inicjalizacja")


if __name__ == '__main__':
    main()
