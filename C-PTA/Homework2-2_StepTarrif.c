#include <stdio.h>

int main() {
    int n;
    double cost;

    scanf("%d", &n);
    if (n <= 0) 
        printf("Invalid Value!");
    else if (n >= 0 && n <= 50) {
        cost = 0.53 * n;
        printf("cost = %.2lf", cost);
    } else {
        cost = 0.53 * 50 + 0.58 * (n - 50);
        printf("cost = %.2lf", cost);
    }

    return 0;
}