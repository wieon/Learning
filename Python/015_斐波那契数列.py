# 斐波那契数列1,1,2,3,5...，找出第n项

def fib(n):
	if n==1 or n==2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(5))