#include <stdio.h>
#include <math.h>

int main() {
    int m, n;
    double sum;

    scanf("%d %d", &m, &n);
    for (;m <= n; m++) 
        sum += pow(m, 2) + 1.0/m;
    printf("sum = %.6lf", sum);

    return 0;
}