#include<iostream>
using namespace std;

int nwd(int a, int b){
	while(a!=b){
		if(a>b){
			a-=b;
		}
		else{
		    b-=a;
		}
	}
	return a;
}
int main(){
    int number1 = 72;
    int number2 = 84;
    string name = "";
    cout<<"Podaj imie"<<endl;
    cin>>name;
    cout<<"Witaj "<<name<<endl;
	cout<<"wynik NWD liczb "<<number1<<" oraz "<<number2<<" : "<<nwd(number1,number2)<<endl;
}