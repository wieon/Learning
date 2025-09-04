skunk = eval(input())
fox = eval(input())
trap = eval(input())
def gcd(a, b):
	if a < b:
		temp = b
		b = a
		a = temp
# 或 a, b = b, a
	reminder = a % b
	if reminder == 0:
		return b
	else:
		return gcd(b, reminder)
if gcd(skunk, trap) > gcd(fox, trap):
	print('黄鼠狼')
elif gcd(skunk, trap) < gcd(fox, trap):
	print('狐狸')
else:
	print('同时')
# 有一个测试失败，为什么？？？

# 法二
import math
a=eval(input())
b=eval(input())
c=eval(input())

#得到最大公约数
def gcd(a,b):
    if a < b:
        temp = b
        b = a
        a = temp
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return gcd(remainder,b)

#求得最大公倍数，越大越晚被抓到
if a*c/gcd(a,c)<b*c/gcd(b,c):
    print("黄鼠狼")
else:
    print("狐狸")

