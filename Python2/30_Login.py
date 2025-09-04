# 三次输入用户名、密码的机会
# Kate 666666 => 登录成功！
# 失败返回：3次用户名或者密码均有误！退出程序。

count = 0
for i in range(3):
	username = input()
	pwd = input()
	if username == 'Kate' and pwd == '666666':
		print('登录成功！')
	else:
		count += 1
		if count == 3:
			print('3次用户名或者密码均有误！退出程序。')
		else:
			continue