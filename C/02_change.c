#include <stdio.h>

int main(){
	//const int AMUONT = 100;  此时AMOUNT不可改 
	int price = 0;
	//int amount = 100;
	int AMOUNT = 100;
	
	printf("请输入金额（元）：");
	scanf_s ("%d", &price);
	
	//printf("请输入票面（元）：");
	//scanf_s("%d", &amount);
	
	int change = AMOUNT - price;
	
	printf("找您%d元", change);
}
// 为什么总是输出 6487572
// A:在change前加&，则输出总是6487572 
