#include <stdio.h>

int main() {
    int i, n, num, min;

    min = 0;
    scanf("%d", &n);
    if (n == 1) {
        scanf("%d", &min);
    } else {
        for (i=0; i<n; i++) {
            scanf("%d", &num);
            if (num < min)  min = num;
        }
    }
    printf("min = %d", min);

    return 0;
}