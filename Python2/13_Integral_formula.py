import sympy

# 积分公式
def integral(a):
	sum = 0
	x = sympy.Symbol('x')
	f = (1+1/x) ** x
	for i in range(1,a+1):
		result = f.evalf(subs={x:i})
		sum += result
	print('{:.8f}'.format(sum))

# 计算
a = eval(input())
integral(a)

# 法二
a = eval(input())
sum = 0
for i in range(1,a+1):
    x = i
    f = (1+1/x) ** x
    sum += f
print('{:.8f}'.format(sum))