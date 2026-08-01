#include <stdio.h>

int main() {
    double sum;
    int N, i;

    scanf("%d", &N);
    for (i=1; i<=N; i++)
        sum += 1.0/i;
    printf("sum = %.6lf", sum);

    return 0;
}