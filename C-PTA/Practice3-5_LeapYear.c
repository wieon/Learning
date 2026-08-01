#include <stdio.h>

int main() {
    int n, flag, i;

    flag = 0;
    scanf("%d", &n);
    if (n <= 2000 || n >2100)
        printf("Invalid year!");
    else {
        for (i=2001; i<=n; i++) {
            if (i%4 == 0 && i%100 != 0){
                printf("%d\n", i);
                flag = 1;
            }
        }
        if (flag == 0)
            printf("None");
    }

    return 0;
}