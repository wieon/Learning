### 01. Try to run 试运行
```C
#include <stdio.h>

int main(){
	printf("hello world!\n");
	printf("%d", 12+34) ;
	return 0;
} 
```

### 02. change.c 零钱
> **后面省略`#include<stido.h>  int main(){...}`**
```C
//const int AMUONT = 100;  此时AMOUNT不可改; 这是C99的写法
//const是一个修饰符，放在int前，给变量加上一个const(不变的)属性。若试图修改，编译器会报错。
const int AMOUNT = 100;  //放在最前面，方便以后有需要时找到并修改
int price = 0;
//int amount = 100;

printf("请输入金额（元）：");
scanf_s ("%d", &price);

//printf("请输入票面（元）：");
//scanf_s("%d", &amount);

int change = AMOUNT - price;

printf("找您%d元", change);
// A:在change前加&，则输出总是6487572 
```

### 03. scanf
```C
int a;
int b;

printf("请输入两个整数：");
scanf("%d %d", &a, &b);
printf("%d + %d = %d\n", a, b, a+b);
```
若写成 `scanf("%d,%d", &a, &b)`，则输入时需输入**1,2**才能运行，输入**1 2**程序没有得到**,**则不会运行。

### 04. inch_and_foot.c
```C
int foot;
int inch;
// 或者double和 %lf (printf仍用 %f) 

printf("请输入身高的英尺和英寸，如输入\"5 7\"表示5英尺7英寸：");
scanf("%d %d", &foot, &inch);
printf("身高是%f米",(foot+inch/12.0)*0.3048);
```

### 05. Expression表达式
operator 运算符
operand 算子：参与运算的值（常数、变量）、返回值
%：取余
```C
#include<stdio.h>  //可恶(〃＞皿＜)，一开始头文件输错了

int main(){
	int hour1, minute1;  //分号分号分号分号！
	int hour2, minute2;
	
	scanf("%d %d", &hour1, &minute1);  //o(╥﹏╥)o叕忘了&
	scanf("%d %d", &hour2, &minute2);
	
	int t1 = hour1 * 60 + minute1;
	int t2 = hour2 * 60 + minute2;
	
	int t = t2 - t1;
	
	printf("时间差是%d小时%d分", t/60, t%60);
}
```

### 06. average平均值

| 优先级 | 运算符 | 运算     | 结合关系 | 举例 |
| ------ | ------ | -------- | -------- | ---- |
| 1      | +      | 单目不变 | 自右向左 | a*+b |
| 1      | -      | 单目取负 | 自右向左 | a*-b |
| 2      | *      | 乘       | 自左向右 | a*b  |
| 2      | /      | 除       | 自左向右 | a/b  |
| 2      | %      | 取余     | 自左向右 | a%b  |
| 3      | +      | 加       | 自左向右 | a+b  |
| 3      | -      | 减       | 自左向右 | a-b  |
| 4      | =      | 赋值     | 自右向左 | a=b  |

### 07. switch value 
**断点调试**
```C
int a = 5;
int b = 6;
int t;
t = a;
a = b;
b = t;
printf("a=%d, b=%d\n", a, b);
return 0;
```
> 使用dev C++时遇到问题，“没能够设置关联文件”，解决方法：以管理员运行程序（好麻烦，为什么啊）

### 08. 加加减减
#### 复合赋值
`total += 5`
`total *= sum + 12` 等价于  `total = total * (sum+12)`
#### 递增递减运算符
单目运算符，算子必须是变量，如a, b,i之类，而不能是5,8这种。
`count ++`
`i++` 后缀形式，先用再加（先记录i的值，再加一）
`++i` 前缀形式，先加再用（先加一，再记录i的值）
```C
int a;
a = 10;

printf("a++=%d\n", a++);
printf("a=%d\n", a);

printf("++a=%d\n", ++a);
printf("a=%d\n", a);

return 0;

//a++=10
//a=11
//++a=12
//a=12
```

### 09. if
```C
int hour1, minute1; 
int hour2, minute2;

scanf("%d %d", &hour1, &minute1); 
scanf("%d %d", &hour2, &minute2);

int ih = hour2 - hour1;
int im = minute2 - minute1;
if (im<0){
    im = 60 + im;
    ih--;
}

printf("时间差是%d小时%d分", ih, im);
```

### 10. 比较运算符
```C
printf("%d\n", 5==3)
printf("%d\n", 5>3)
printf("%d\n", 5<=3)
printf("%d\n", 7>=3+4)

//0
//1
//0
```
所有关系运算符的优先级比算数运算符低，但比赋值运算符高。
`6>5>4  //0` 

### 11. 其他

C语言不允许函数嵌套定义。可以在一个函数里放另一个函数的声明，但不能放另一个函数的body。

