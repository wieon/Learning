'''
大型超市为顾客提供了寄存包裹的保管箱，放入随身包裹时生成一个
取件码发给用户，用户凭取件码自行提取包裹。
取件码的字符包括：数字 0 - 9 和字母 A、B、C、D、E、F、G、H、I、J。
每次从以上字符串'ABCDEFGHIJ0123456789' 中随机取一个字符，重复 6 次， 
生成一个形如 “9I16A4” 的取件码，各字符的使用次数无限制。
随机数种子 n 由用户输入。
'''

import random
n = eval(input())
random.seed(n)
sequence = 'ABCDEFGHIJ0123456789'
for i in range(6):
	print(random.choice(sequence),end='')
	
# 法二
# random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))