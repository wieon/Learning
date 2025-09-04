# 微软产品序列号一般25位，格式如下：
# 36XJE-86JXF-MTY63-7Q79Q-6BWJ2
# 'BCEFGHJKMPQRTVWXY2346789'，为了避免相似的字母混淆

import random

def microsoft_code(n):
	for i in range(n):
		li = 'BCEFGHJKMPQRTVWXY2346789'
		list = []
		for i in range(5):
			code = ''
			for i in range(5):
				code += random.choice(li)
			list.append(code)
		key = '-'.join(list)
		print(key)


if __name__ == '__main__':
	num = int(input())
	seed = int(input())
	random.seed(seed)
	microsoft_code(num)