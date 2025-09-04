#获取用户输入一批数字，每个数字一行，即输入一个数字之后
# 回车在下一行输入下一个数字，最后以空回车为结束（即空输入）。

num = input()
sum = 0
while num != '':
	sum += eval(num)
	num = input()
print(sum)
