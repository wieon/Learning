#include <stdio.h>

int main() {
    double N, sum, i;

    scanf("%lf", &N);
    for (i=1; i <= 2*N; i += 2)
        sum += 1/i;
    printf("sum = %.6lf", sum);

    return 0;
}