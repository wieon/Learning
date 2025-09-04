# 找出三位数的水仙花数
# 各数字的立方和等于该数字本身

for i in range(1, 10):
	for j in range(10):
		for k in range(10):
			if i**3 + j**3 + k**3 == 100*i+10*j+k:
				print(100*i+10*j+k)