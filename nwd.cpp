#include<iostream>
using namespace std;
int nwd(int a, int b){
    for(int i = -5;i<-1;i++) {
        if (i%2==0) {
            cout<<i<<endl;
        }
    }
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

    string powitanie = "witaj! ";
	int number1 = 72;
	int number2 = 84;
	number1 = 72;
	cout<<powitanie<<endl<<"a oto wynik: "<<endl<<nwd(number1,number2)<<endl;
	cout<<powitanie<<endl<<"a oto wynik: "<<endl<<nwd(number1,number2)<<endl;

}