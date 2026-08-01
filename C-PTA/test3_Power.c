#include <stdio.h>
#include <math.h>

int main() {
    int result;

    result = pow(3.0,3.0);

    /* pow 函数参数和结果都是双精度 */
    printf("%d\n", pow(3,3));  // 0
    printf("%d\n", pow(3.0,3.0));  // 0
    printf("%lf\n", pow(3.0,3.0));  // 27.000000
    printf("%d\n", result);  // 27
    
    return 0;
}