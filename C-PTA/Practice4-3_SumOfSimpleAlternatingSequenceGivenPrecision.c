#include <stdio.h>
#include <math.h>

int main() {
    double eps, sum, item;
    int i, flag;

    i = 1; sum = 0; flag = 1;
    scanf("%lf", &eps);
    item = 1.0/i;
    while (fabs(item) > eps) {
        sum += flag * item;
        i += 3;
        item = 1.0/i;
        flag = -flag;
    }
    sum += flag * item;
    printf("sum = %.6lf", sum);

    return 0;
}