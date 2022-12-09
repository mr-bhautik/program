#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	char input[16];
    char password[16]= "secreat";
	printf("enter the string:\n");
	scanf("%s", input);
	printf("n1: %s \n n2:%s\n",input,password);
	printf("adress \n n1: %p \n n2: %p",input,password);
	return 0;
}
