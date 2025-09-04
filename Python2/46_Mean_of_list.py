def mean(numlist):
	s = 0.0
	for num in numlist:
		s += eval(num)
	s /= len(numlist)
	return s

ls = input().split(',')
print("average:",mean(ls))