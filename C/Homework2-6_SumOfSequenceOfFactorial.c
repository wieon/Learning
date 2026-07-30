#include <stdio.h>

int fact( int m ) {
    int i, result=1;

    for (i=1; i <= m; i++) {
        result *= i;
    }

    return result;
}

int main() {
    int i, n, sum=0;

    scanf("%d", &n);
    for (i=1; i <= n; i++)
        sum += fact(i);
    printf("%d", sum);

    return 0;
}