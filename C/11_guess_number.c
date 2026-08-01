#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	srand(time(0));
	int number = rand()%100+1;
	int count = 0;
	int a = 0;
	printf("number prepared.ready? go!\n");
	do{
		printf("guess a number between 1-100:\n");
		scanf("%d", &a);
		count ++;
		if (a>number){
			printf("u're large\n");
		}else if (a<number){
			printf("u're small\n");
		}
	}while (a != number);
	printf("bingo!!! only %d times!", count);
}
