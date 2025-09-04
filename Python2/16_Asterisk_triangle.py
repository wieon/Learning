N = eval(input())
line = (N+1) // 2  #防止变成浮点数
for i in range(line):
	text = '*' * (2*i+1)
	print(text.center(N))