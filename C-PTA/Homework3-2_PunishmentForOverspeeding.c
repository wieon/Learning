#include <stdio.h>
#include <math.h>

int main() {
    int speed, restriction, exceed;
    double percentage;

    scanf("%d %d", &speed, &restriction);
    percentage = (double) speed / restriction;
    if (percentage < 1.1) 
        printf("OK");
    else if (percentage >= 1.1 && percentage < 1.5) {
        exceed = round(percentage * 100 - 100);  // 四舍五入
        printf("Exceed %d%%. Ticket 200", exceed);
    } else {
        exceed = round(percentage * 100 - 100);  // 四舍五入
        printf("Exceed %d%%. License Revoked", exceed);
    }
        
    return 0;
}