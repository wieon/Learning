import sys
pay = float(input())
INDIVIDUAL_EXEMPTION = 5000
pay2 = pay - INDIVIDUAL_EXEMPTION 
if pay2 >= -5000 and pay2 <= 0:
	rate, deduction = 0, 0
elif pay2 > 0 and pay2 <= 3000:
	rate, deduction = 0.03, 0
elif pay2 > 3000 and pay2 <= 12000:
	rate, deduction = 0.10, 210
elif pay2 > 12000 and pay2 <= 25000:
	rate, deduction = 0.20, 1410
elif pay2 > 25000 and pay2 <= 35000:
	rate, deduction = 0.25, 2660
elif pay2 > 35000 and pay2 <= 55000:
	rate, deduction = 0.30, 4410	
elif pay2 > 55000 and pay2 <= 80000:
	rate, deduction = 0.35, 7160
elif pay2 > 80000:
	rate, deduction = 0.45, 15160
else:
	print('error')
	sys.exit()
tax = pay2 * rate - deduction
get = pay - tax
print(f'应缴税款{tax:.2f}元，实发工资{get:.2f}元')
# 失败！！！

s = float(input())
# 先判断输入是正数，然后根据输入的工资范围定税率和速算扣除数
if s < 0:
    print("error")
else:
    salary = s - 5000
    if salary <= 0:
        fee, num = 0, 0
    elif salary <= 3000:
        fee, num = 3, 0
    elif salary <= 12000:
        fee, num = 10, 210
    elif salary <= 25000:
        fee, num = 20, 1410
    elif salary <= 35000:
        fee, num = 25, 2660
    elif salary <= 55000:
        fee, num = 30, 4410
    elif salary <= 80000:
        fee, num = 35, 7160
    else:
        fee, num = 45, 15160
    tax = abs(salary * fee / 100 - num)
    print("应缴税款{:.2f}元，实发工资{:.2f}元。".format(tax, salary + 5000 - tax))