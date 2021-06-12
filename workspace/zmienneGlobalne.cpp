#include<iostream>
using namespace std;

int a = 5;

int add(int a, int b){
    return a+b;
}

int b = 10;

int main() {
    cout<<"Wynik: "<<add(a,b);
}
