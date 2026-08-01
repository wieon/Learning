#include <stdio.h>

int main(void){
	int a = -1;
	if (a>0 && a++>1){
		printf("OK\n");
	}
	printf("%d\n", a);
}

// && and
// || or
// x > 4 && x < 6
// c >= 'A' && c <= 'Z'
// ! age < 20  单目运算符(Unary operator)优先级高于双目运算符(Binocular operator)，先 ! 后 < 
// priority: ! > && > || 

// short cut 短路 
// &&: false on the left, then stop
// ||: true on the left, then stop

