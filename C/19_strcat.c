#include<string.h>
#include<stdio.h>

/*
int main(){
	char password[16]="";
	char input[]="51";
	
	// printf("%s\n", input[1]);
	strcat(password, input);
	printf("%s\n", password);
	return 0;
}
*/



int main(){
	
	int KeyNum;
	char Password[4]="56";
	
	scanf_s("%d", &KeyNum);
	if(KeyNum){
		if(KeyNum){
			sprintf(Password, "%d", KeyNum%10);  // ¸²¸Ç 
			printf("%s\n", Password);
		}
	}	
}


