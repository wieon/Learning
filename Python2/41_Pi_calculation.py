# 求解圆周率可以采用蒙特卡罗方法，在一个正方形中撒点，
# 根据在 1/4 圆内点的数量占总撒点数的比例计算圆周率值。
# 请以 123 作为随机数种子，获得用户输入的撒点数量，编
# 写程序输出圆周率的值，保留小数点后 6 位。

import random

random.seed(123)
n = eval(input())

def monte_carlo_pi(N):
    inside_circle = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / N
    return pi_estimate
	
print(f'{monte_carlo_pi(n):.6f}')
