#include <stdio.h>

int sum(int m, int n);

int main()
{    
    int m, n;

    scanf("%d %d", &m, &n);
    printf("sum = %d\n", sum(m, n));
    
    return 0;
}

/* 你的代码将被嵌在这里 */
int sum(int m, int n) {
    int i, sum=0;  // 自动变量（局部变量），需要赋初始值，不然为随机值

    for (i=m; i<=n; i++) {
        sum += i;
    }

    return sum;
}