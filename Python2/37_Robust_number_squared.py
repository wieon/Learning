'''
获得用户输入的一个数字，可能是浮点数或复数，
如果是整数仅接收十进制形式，且只能是数字。
对输入数字进行平方运算，输出结果。

要求：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
（1）无论用户输入何种内容，程序无错误；‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
（2）如果输入有误，请输出"输入有误"。
'''

'''
def is_complex(str):
	try:
		complex(str)
		return True
	except ValueError:
		return False
		

# isinstance()函数判断数据类型
if isinstance(eval(num), int) == True or isinstance(eval(num), float) == True:
	print(eval(num)**2)
elif is_complex(num) == True:
	print(complex(num))
else:
	print('输入有误')
# 失败！！！
'''
'''
a = input()
# 排除十六、八、二进制
if a[1] in [x,X,o,O,b,B]:
	print('输入有误')
# 排除字符串
try:
	num = eval(a)
except NameError:
	print('输入有误')
try:
	int(num)
	float(num)
if isinstance(num,complex) == True or isinstance(num,int) or :
	print(num**2)
# 失败！！！
'''

a = input()
# 判断是否为复数
if a[-1] == 'j':
	print(eval(a)**2)
# 判断输入是否是小数
elif eval(a) != round(eval(a)):  # 蛙趣还能这样！
	print(eval(a)**2)
#判断输入是否是可计算的内容,ord()返回字符的Unicode编码
else:
	for i in a:
		if ord(i)<ord('0') or ord(i)>ord('9'):
			print('输入有误')
			break
	else:  # 全码精华！！！！！！记住！！！
		print(eval(a)**2)