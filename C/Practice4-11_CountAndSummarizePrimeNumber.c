#include <stdio.h>
#include <math.h>

/* 判断是否为质数 */
int IsPrimeNumber( int num ) {
    int i, flag;
    flag = 1;
    if (num%2 == 0)  flag = 0;
    else {
        for (i=3; i<=sqrt(num); i += 2) {
            if (num%i == 0) {
                flag = 0;
                break;
            }
        }
    }
    if (flag == 0)  return 0;  // 不是质数
    else return 1;  // 是质数
}

int main() {
    int m, n, i, count, sum;

    count = 0; sum = 0;
    scanf("%d %d", &m, &n);
    for (i=m; i<=n; i++) {
        if (IsPrimeNumber(i) == 1) {
            count++;
            sum += i;
        }
    }
    printf("%d %d", count, sum);

    return 0;
}