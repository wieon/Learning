'''
def Dayup(df):
	dayup = 1.0
	for i in range(365):
		if i % 7 in [6, 0]:
			dayup *= (1-0.01)
		else:
			dayup *= (1+df)
	return dayup
dayfactor = 0.01
while(Dayup(dayfactor)<37.78):
	dayfactor += 0.001
print("工作日的努力参数是: {:.3f}".format(dayfactor))
'''

# 法二
#共有261个工作日，104个休息日，若全年无休，若每周休两天
result = (1+0.01)**365 / (1-0.01)**104  
base = result**(1/261)
factor = base - 1
print('{:.3f}'.format(factor))
#失败，为什么输出是0.018，而不是0.019？？？