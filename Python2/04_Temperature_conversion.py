temp = input()
if temp[0] == "C":
	F = eval(temp[1:]) * 1.8 +32
	print("F{:.2f}".format(F))
else:
	C = (eval(temp[1:]) - 32) / 1.8
	print("C{:.2f}".format(C))
	
# temp[1:] 和 temp[1:len(temp)+1] 等价