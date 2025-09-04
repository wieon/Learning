def peach(n):
	a = 1
	for i in range(10-n):
		a += 1
		a *= 2
	return a

for i in range(10,0,-1):
    print("第{}天有{}只桃子".format(i,peach(i)))