#include <stdio.h>

/* 计算n! */
double fact( int n ) {
    int i, result=1;  //要赋初始值！
    for (i=1; i <= n; i++)
        result *= i;
    return result;
}

int main() {
    int m, n, Cnm;

    scanf("%d %d", &m, &n);
    Cnm = fact(n) / fact(n-m) / fact(m);
    printf("result = %d", Cnm);

    return 0;
}