# 获取用户输入月份，输出该月有多少天（考虑闰年）。

# 可以分别同时赋列表中的值
y, m = input().split(',')
year = int(y)
month = int(m)

def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 400 != 0 and year % 100 != 0:
		return False
	elif year % 400 != 0 and year % 4 == 0:
		return True
	else:
		return False

if month in [1,3,5,7,8,10,12]:
	print('31')
elif month in [4,6,9,11]:
	print('30')
else:
	if is_leap_year(year) == True:  # 要输入参数啊啊啊
		print('29')
	else:
		print('28')

	
