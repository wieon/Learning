# 生成快递自提柜取件码
# 每次从'ABCDEFGHIJ0123456789'中随机取一个字符，重复6次，生成一个形如'9I16A4'的取件码，
# 各字符使用次数无限制。随机种子n由用户输入。

import random
n = int(input())
random.seed(n)
code = ''
li = 'ABCDEFGHIJ0123456789'
for i in range(6):
	i = random.randint(0,19)
	num = li[i]
	code += num  # 字符串用+，列表用append
print(code)

# random.choice(seq)从给定序列中随机返回一个元素

'''
# 法二
import random
n = int(input())
random.seed(n)
code = ''
li = 'ABCDEFGHIJ0123456789'
for i in range(6):
	code += random.choice(li)
print(code)
'''