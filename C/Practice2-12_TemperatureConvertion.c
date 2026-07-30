#include <stdio.h>

int main() {
    int lower, upper, F;
    double C;

    scanf("%d %d", &lower, &upper);
    if (lower > upper || upper > 100)
        printf("Invalid.");
    else {
        printf("fahr celsius\n");
        for (;lower <= upper; lower += 2){
            F = lower;
            C = 5.0 * (F - 32) / 9;
            printf("%d%6.1lf\n", F, C);
        }
    }

    return 0;        
}