#include <stdio.h>

int main(){
	int n;
	printf("enter no of row: ");
	scanf("%d", &n);
	for (int i =n; i<=1; ++i)
	{
		for (int i = 1; i<=n; ++i)
		{
			printf("1");
		}
		printf("\n");
	}
}