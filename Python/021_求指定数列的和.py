# 求数列2/1, 3/2, 5/3, 8/5...前20项的和

sum = 0
up = 2
down = 1
for i in range(20):
	sum += up/down
	a = up
	up += down
	down = a
print(sum)