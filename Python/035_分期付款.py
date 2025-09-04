'''
等额本息(Average Capital Plus Interest, ACPI):
每月还款额=贷款本金*月利率*（1+月利率）**总还款月数/（（1+月利率）**总还款月数-1）
等额本金(Average Capital, AC):
每月还款额=贷款本金/总还款月数+（贷款本金-累计已还款本金）*月利率

第一行输入一个浮点数，表示贷款本金
第二行输入一个整数，表示分期月数
第三行输入一个字符串，限定只能输入ACPI和AC
第四行输入一个浮点数，表示月利率
'''

price, month, mode, rate = float(input()), int(input()), input(), float(input())
if mode == 'ACPI':
	money = price*rate*(1+rate)**month/((1+rate)**month-1)
	print(money)
elif mode == 'AC':
	li = []
	paid = 0
	for i in range(month):
		money = price / month + (price-(price/month)*i)*rate
		li.append(round(money, 2))
	print(li)
else:
	print('还款方式输入错误')