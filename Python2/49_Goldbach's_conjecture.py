'''
1742年，哥德巴赫给欧拉的信中提出了以下猜想“任一大于2的
整数都可写成三个质数之和”。常见的猜想陈述为欧拉的版本，
即任一大于2的偶数都可写成两个素数之和，亦称为“强哥德巴
赫猜想”或“关于偶数的哥德巴赫猜想”。比如：24=5+19，其中5
和19都是素数。

输入一个正整数N，当输入为偶数时，分行按照格式“N = p + q”
输出N的所有素数分解，其中p 、 q均为素数且p ≤ q。当输入为
奇数或N<4时，输出'Data error!' 。
'''

def is_prime(n):
    # 判断素数的函数,接收一个正整数为参数，参数是素数时
	# 返回True，否则返回False
	for i in range(2, int(n**0.5)+1):
		if n%i == 0:
			return False
	return True

    
def goldbach_conjecture(num):
    # 哥德巴赫猜想, 接收一个不小于4的正整数为参数。
    # 当参数为不小于4的偶数时，将其分解为两个素数的加和，
	# 按小数+数的格式输出。有多种组合时全部输出，但不输出
	# 重复的组合，例如输出8=3+5，不输出8=5+3。
    # 参数为奇数或小于4时，输出'Data error!' 
	if num%2 != 0 or num<4:
		print('Data error!')
	else:
		for i in range(2, int(num/2)+1):
			if is_prime(i) == True and is_prime(num-i) == True:
				print(f'{num}={i}+{num-i}')
				
    

if __name__ == '__main__':
	positive_even = int(input())        # 输入一个正数
	goldbach_conjecture(positive_even)