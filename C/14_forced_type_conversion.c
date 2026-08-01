#include <stdio.h>

int main(void){
	printf("%d\n", (short)32768);
	return 0;
}

// char -> short -> int -> long -> long (small -> large)
// int -> float -> double (small -> large)
// printf: forced type conversion (usually smaller type)
// scanf: short-hd, long long-ld
