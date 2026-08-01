#include <stdio.h>
#include <math.h>

int main() {
    int n, i, result;

    scanf("%d", &n);
    for (i=0; i <= n; i++){
        result = pow(3.0,i);  // 自动类型转换（非赋值运算、赋值运算）
        printf("pow(3,%d) = %d\n", i, result);
    }
    
    return 0;
}