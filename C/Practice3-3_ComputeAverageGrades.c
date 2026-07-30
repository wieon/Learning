#include <stdio.h>

int main() {
    int count, score, sum, n, i;
    double average;

    count = 0; sum = 0;
    scanf("%d", &n);
    if (n == 0)
        average = 0.0;
    else {
        for (i=0; i<n; i++) {
        scanf("%d", &score);
        sum += score;
        if (score >= 60)
            count++;
        }
        average = (double) sum / n;
    }
    printf("average = %.1lf\ncount = %d", average, count);

    return 0;
}