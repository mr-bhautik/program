#include<stdio.h>

int main(){
	int i, j=1, sum=0;
	printf("enter number: ");
	scanf("%d", &i);
	while(j<=i){
		sum=sum+j*j;
		printf("%d\n",j*j );
		j++;
	}
	printf("sum is %d\n", sum );
}
