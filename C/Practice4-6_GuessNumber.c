#include <stdio.h>

int main() {
    int num, target, N, count, flag;

    count = 0; flag = 0;
    scanf("%d %d", &target, &N);
    scanf("%d", &num);  count++;
    while (num >= 0 || count <= N) {
        if (flag == 0) {
            if (num > target) {
            printf("Too big\n");
            } else if (num < target) {
            printf("Too small\n");
            } else {
                if (count == 1)  printf("Bingo!\n");
                else if (count > 1 && count <= 3)  printf("Lucky You!\n");
                else  printf("Good Guess!\n");
                flag = 1;
            }
        }
        scanf("%d", &num);  count++;
    }
    if ((count > N && flag == 0) || (count <= N && num < 0))
        printf("Game Over\n");
}