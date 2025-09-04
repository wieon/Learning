def fib(months):
	if months == 0:
		return 0
	elif months == 1:
		return 1
	else:
		return fib(months-1) + fib(months-2)

n = int(input())
print(fib(n), '{:.3f}'.format(fib(n-1)/fib(n)))
