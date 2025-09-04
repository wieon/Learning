# 输入一个数，判断是不是回文数

a = input()
b = a[::-1]
if a == b:
	print("是回文数")
else:
	print("不是回文数")