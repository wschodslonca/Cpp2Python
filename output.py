def nwd(a, b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

def main():
    number1 = None
    number2 = None
    number1 = input() 
    number2 = input() 
    print(nwd(number1,number2),'\n',sep='',end='')

if __name__ == '__main__':
  main()