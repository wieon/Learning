# include <stdio.h>

// method 1
//int main(){
//	int x;
//	int n=0;
//	scanf("%d", &x);
//	while(x>0){
//		x /= 10;
//		n++;
//	}
//	printf("%d\n", n);
//	return 0;
//}
//È±µã£ºÎÞ·¨ÅÐ¶Ï0 


// method 2
int main(){
	int x;
	int n=0;
	scanf("%d", &x);
	do{
		x /= 10;
		n++;
}while(x>0);
	printf("%d\n", n);
	return 0;
}

