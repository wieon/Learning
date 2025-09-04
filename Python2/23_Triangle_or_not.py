'''
import math
a = float(input())
b = float(input())
c = float(input())
list = [a, b, c]
list.sort(reverse=True)  # 在原列表里排序，新建空列表引用会报TypeError: NoneType‘ object is not subscriptable
a, b, c = list[0], list[1], list[2]  # 降序排列
if b+c>a:
	s = (a+b+c) / 2
	area = math.sqrt(s*(s-a)*(s-b)*(s-c))
	print(f'YES\n{area:.2f}')
else:
	print('NO')
'''

# 判断是否为直角三角形
a = float(input())
b = float(input())
c = float(input())
list = [a, b, c]
list.sort()
a, b, c = list[0], list[1], list[2]
if a**2 + b**2 == c**2:
	print('YES')
else:
	print('NO')
# 失败。没排除三角形边长小于等于0的情况
	
a = float(input())
b = float(input())
c = float(input())
if a <= 0 or b <= 0 or c <= 0:
	print('NO')
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
	print('YES')
else:
	print('NO')