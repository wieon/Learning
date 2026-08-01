#include <stdio.h>

/* 计算阶乘 */
int fact( int n ) {
    int i, result;

    result = 1;
    for (i=1; i<=n; i++) {
        result *= i;
    }
    return result;
}

int main() {
    int n, i;
    double sum;

    sum = 1;
    scanf("%d", &n);
    for (i=1; i<=n; i++) {
        sum += 1.0 / fact(i);
    }
    printf("%.8lf", sum);

    return 0;
}