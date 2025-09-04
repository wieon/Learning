# 获取三位的水仙花数

list = []
for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			num = 100*a+10*b+c
			if a**3+b**3+c**3 == num:
				list.append(num)
print(*list, sep=',')
			