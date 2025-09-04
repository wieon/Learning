# 输入整数a, b表示一个闭区间，找出区间内素数并打印

def prime_or_not(n):
	for i in range(2, n):
		if n%i == 0:
			return False
	return True
			
a, b = input().split()
for i in range(eval(a), eval(b)+1):
	if prime_or_not(i) == True:
		print(i)