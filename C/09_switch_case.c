#include <stdio.h>

int main()
{
	int type;
	scanf("%d", &type);
	
	switch(type){
		case 1:
			printf("hello");
			break;
		case 2:
			printf("bye");
			break;
		case 3:
			printf("aaa");
			break;
		default:
			printf("help");
			break;
	}
}

// case表示从哪里开始做某件事，如果没有break就会顺序执行下去 
