#include <stdio.h>

void CharPyramid( int n, char ch );

int main()
{    
    int n;
    char ch;

    scanf("%d %c", &n, &ch);
    CharPyramid(n, ch);
    
    return 0;
}

/* 请在这里填写答案 */
void CharPyramid( int n, char ch ) {
    int i, j;

    for (i=1; i<=n; i++){  // 每行
        for (j=1; j <= n-i; j++)  // 输出每行前面的空格
            printf(" ");
        for (j=1; j <= i; j++)
            printf("%c ", ch);
        putchar('\n');
    }
}