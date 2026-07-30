#include <stdio.h>
#include <math.h>

/* 计算边长 */
double Length_of_side( int x1, int y1, int x2, int y2 ) {
    double l;
    l = sqrt(pow((x1-x2), 2) + pow((y1-y2), 2));
    return l;
}

/* 判断三条边是否能构成三角形 */
int Trangle_or_not( double l1, double l2, double l3 ) {
    if (l1 + l2 > l3 && l1 + l3 > l2 && l2 + l3 > l1)
        return 1;
    else 
        return 0;
}

/* 已知三边求三角形面积 */
double Area( double a, double b, double c ) {
    double area, s;
    s = (a + b + c) / 2;
    area = sqrt(s * (s-a) * (s-b) * (s-c));
    return area;
}


int main() {
    int x1, y1, x2, y2, x3, y3;
    double l1, l2, l3, L, A;

    scanf("%d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3);
    l1 = Length_of_side(x1, y1, x2, y2);
    l2 = Length_of_side(x1, y1, x3, y3);
    l3 = Length_of_side(x3, y3, x2, y2);

    if (Trangle_or_not(l1, l2, l3) == 0) 
        printf("Impossible");
    else {
        L = l1 + l2 + l3;
        A = Area(l1, l2, l3);
        printf("L = %.2lf, A = %.2lf", L, A);
    }
    
    return 0;
}