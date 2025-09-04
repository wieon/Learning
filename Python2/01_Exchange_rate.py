Money = input("请输入美元或人民币，如RMB123或USD123：")
EXCHANGE_RATE = 6.78
Len = len(Money)
if Money[0:3] == 'RMB':
	TransToUSD = eval(Money[3:Len+1]) / EXCHANGE_RATE
	print("转换后的币值为：USD{:.2f}".format(TransToUSD))
else:
	TransToRMB = eval(Money[3:Len+1]) * EXCHANGE_RATE
	print("转换后的币值为：RMB{:.2f}".format(TransToRMB))