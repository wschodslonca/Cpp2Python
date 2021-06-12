#include<iostream>
using namespace std;
int IterateFactorial(int n)
{
	int suma =1;
	for(int i=1;i<=n;i++)
	{
		suma *=i;
	}
	return suma;
}
int RecursiveFactorial(int n)
{
	if (n==0 || n==1)
	{
		return 1;
	}
	else
	{
		return n*RecursiveFactorial(n - 1);
	}
}
int main()
{
	int n=6;
	cout<<"Iteracyjnie "<<IterateFactorial(n)<<endl;
	cout<<"Rekurencyjnie "<<RecursiveFactorial(n);
	return 0;
}