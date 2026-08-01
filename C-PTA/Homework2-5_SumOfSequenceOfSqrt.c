#include <stdio.h>
#include <math.h>

int main() {
    int n, i;
    double sum, j;

    scanf("%d", &n);
    for (i=1; i<=n; i++) {
        j = i;
        sum += sqrt(j);
    }
    printf("sum = %.2lf", sum);

    return 0;
}