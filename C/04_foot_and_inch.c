#include <stdio.h>

int main(){
	int foot;
	int inch;
	// 或者double和 %lf (printf仍用 %f) 
	
	printf("请输入身高的英尺和英寸，如输入\"5 7\"表示5英尺7英寸：");
	scanf("%d %d", &foot, &inch);
	printf("身高是%f米",(foot+inch/12.0)*0.3048);
}
