#include <stdio.h>

int main() {
    int N, i;
    double sum;

    scanf("%d", &N);
    for (i=1; i <= 3*N-2; i += 3){
        if (i%2 == 0)
            sum -= 1.0/i;
        else
            sum += 1.0/i;
    }
    printf("sum = %.3lf", sum);

    return 0;
}