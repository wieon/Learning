# 获得用户输入数字 N，计算并输出从 N 开始的 5 个质数，
# 单行输出，质数间用逗号、分割。
# 注意：需要考虑用户输入的数字 N 可能是浮点数，应对输
# 入取整数；最后一个输出后不用逗号。

import math

n = math.ceil(eval(input()))

count = 0
list = []
while count <= 4:
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			break
	else:
		list.append(n)
		count += 1
	n += 1

# repr()函数给字符加"",使之变为字符串
print(",".join(repr(x) for x in list))
	
