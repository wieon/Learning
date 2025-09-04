# 输入两个整数，以它们的和为随机数种子，
# 并在 32-127 之间（含）随机产生 20 个整数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# 以这些数字为 Unicode 码产生字符，并将组成字符串输出。

import random
a,b = input().split(',')
c = eval(a)+eval(b)
random.seed(c)
list = []
for i in range(20):
	d = random.randint(32,127)
	list.append(chr(d))
for x in list:
	print(x,end='')
