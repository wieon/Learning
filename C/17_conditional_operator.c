#include <stdio.h>

int count = 10;

int main(void){
	count = (count>20) ? count - 10 : count + 10;
	return 0;
}

//if (count>20){
//	count = count - 10;
//}else{
//	count = count + 10;
//}

// 条件运算符的优先级高于赋值运算符，但低于其他所有运算符
// 条件运算符是自右向左结合的 
