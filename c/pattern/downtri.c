#include<stdio.h>

int main(){
	int i,j;
	for (int i = 1; i <= 5; ++i)
	{
		for(j=1;j<=i;j++){
			printf(" ");
		}
		for(int k=5;k>i;k--){
			printf("*");
		}
		for(int m=5;m>i;m--){
			printf("*");
		}
		printf("\n");
	}
}