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

	int number1;
	int number2;
	cin>>number1;
	cin>>number2;
	cout<<nwd(number1,number2)<<endl;
}