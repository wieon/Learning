#include <stdio.h>
#include <math.h>

int main() {
    double distance;
    int wait, distance_price, wait_price, price;

    scanf("%lf %d", &distance, &wait);

    // 计算路程价格
    if (distance <= 3) {
        distance_price = 10;
    } else if (distance > 3 && distance <= 10) {
        distance_price = round(10 + (distance - 3) * 2);
    } else {
        distance_price = round(10 + 2 * 7 + (distance - 10) * 3);
    }

    // 计算等待价格
    if (wait < 5) {
        wait_price = 0;
    } else {
        wait_price = (wait / 5) * 2;
    }

    price = distance_price + wait_price;
    printf("%d", price);

    return 0;
}