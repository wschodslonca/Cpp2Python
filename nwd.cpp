#include<iostream>
using namespace std;

int NWD(int a, int b){
	
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
	cout<<" NWD = "<<NWD(number1,number2);
}
