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
}
