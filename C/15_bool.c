#include <stdbool.h>

int main(void){
	bool b = 2>1;
	bool t = true;
	t = 2;  // t is int, can be compiled
	printf("%d\n", t);
	return 0;
}
