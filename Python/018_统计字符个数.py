# 输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数

char = 0
number = 0
space = 0
other = 0

string = input()
for i in string:
	if i.isalpha():
		char += 1
	elif i.isdigit():
		number += 1
	elif i.isspace():
		space += 1
	else:
		other += 1
		
print(f'英文字母{char}个，数字{number}个，空格{space}个，其他字符{other}个')

# 缺点：汉字被算到英文字母里了