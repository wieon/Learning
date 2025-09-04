import random

target = random.randint(1,99)
count = 7
while count != 0:
	num = int(input("请输入你要猜的数字："))
	if num == target:
		print('bingo!')
		break
	elif num > target:
		print(f'大了，往小点猜~还有{count}次机会喔^-^')
		count -= 1
	else:
		print(f'小了，往大点猜~还有{count}次机会喔^-^')
		count -= 1
else:
	print("机会用尽，游戏结束咯`>_<`")