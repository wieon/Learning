father_height = eval(input())
mother_height = eval(input())
gender = input()
if gender == '男':
	height = (father_height + mother_height) * 1.08 / 2
	print(int(height))
elif gender =='女':
	height = (father_height * 0.923 + mother_height) / 2
	print(int(height))
else:
	print('无对应公式')