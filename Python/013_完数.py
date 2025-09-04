# 找出1000以内所有完数
# 完数：一个数恰好等于除了它以外的因子之和

for n in range(2, 1000):
	sum = 0
	for i in range(1, n):
		if n%i == 0:
			sum += i
	if sum == n:
		print(n)