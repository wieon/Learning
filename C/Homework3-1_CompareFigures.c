#include <stdio.h>

int main() {
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);
    // 目标：a <= b <= c
    if (a > b) {
        a ^= b ^= a ^= b;  // a、b值互换
    }
    if (c < b) {
        c ^= b ^= c ^= b;  // c、b值互换
    }
    if (a > b) {
        a ^= b ^= a ^= b;  // a、b值互换
    }
    printf("%d->%d->%d", a, b, c);

    return 0;
}