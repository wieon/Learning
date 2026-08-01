#include <stdio.h>

int main() {
    int num, count;

    count = 0;
    printf("[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit\n");
    scanf("%d", &num);  // printf("%d ", num);
    count++;
    while (num != 0 && count <= 5) {
        if (num > 4 || num < 0) {
            printf("price = 0.00\n"); 
            count++; 
        } else {
            switch (num) {
            case 1:  printf("price = 3.00\n"); count++; break;
            case 2:  printf("price = 2.50\n"); count++; break;
            case 3:  printf("price = 4.10\n"); count++; break;
            case 4:  printf("price = 10.20\n"); count++; break;
            }
        }
        scanf("%d", &num);  // printf("%d ", num);
    }

    return 0;
}