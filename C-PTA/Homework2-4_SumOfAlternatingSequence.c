#include <stdio.h>

int main() {
    int i, n;
    double sum;

    scanf("%d", &n);
    for (i=1; i<=n; i++) {
        if (i%2 == 0)
            sum -= i/(2.0*i-1);
        else
            sum += i/(2.0*i-1);
    }
    printf("%.3lf", sum);

    return 0;
}