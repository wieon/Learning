'''
# 有三个圆柱 A、B、C，初始时 A 上有 N 个圆盘，N 由用
# 户输入给出，最终移动到圆柱 C 上。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# 每次移动步骤的表达方式示例如下：[STEP 10] A->C。其
# 中，STEP 是步骤序号，宽度为 4 个字符，右对齐。

# 请在...补充一行或多行代码
steps = 0
def hanoi(src, des, mid, n):
    global steps
    if n == 1:
        ...
        print("[STEP{:>4}] {}->{}".format(steps, src, des))
    else:
        ...

N = eval(input())
hanoi("A", "C", "B", N)
'''

# 实现这个算法可以简单分为三个步骤：
# （1）把n-1个盘子由A 移到 B；
# （2）把第n个盘子由 A移到 C；
# （3）把n-1个盘子由B 移到 C；
# =>移到的步数必定为奇数步


# 递归：2f(n-1)+1=f(n)
# => Sn = 2^n - 1



# steps = 0
# def hanoi(src, des, mid, n):
	# global steps
	# if n == 1:
        # steps = 1
		# print("[STEP{:>4}] {}->{}".format(steps, src, mid))
		
	# else:
		# hanoi(src, mid, des, n-1)
		# print("[STEP{:>4}] {}->{}".format(2**(n-1), src, mid))
		# hanoi(des, src, mid, n-1)
        
# N = eval(input())
# hanoi("A", "C", "B", N)    
    

def Hanoi(n, current, transit, target):
    if n == 1:
        print(current, "-->", target)
    else:
        Hanoi(n - 1, current, target, transit)
        print(current, "-->", target)
        Hanoi(n - 1, transit, current, target)
 
 
num = int(input("输入汉诺塔的层数："))
Hanoi(num, 'A', 'B', 'C')



