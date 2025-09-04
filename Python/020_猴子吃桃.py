# 猴子每天吃一半桃子，再多吃一个，到第10天再想吃时只剩一个了，
# 问原来共有多少桃子？

peach = 1
for i in range(1, 10):
	peach = (peach + 1) * 2
print(peach)