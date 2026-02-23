# numbers为可变参数
# numbers接受到的是tuple或list
# 调用该函数时，可以传入任意个参数，包括0个参数
"""
【调用】
法一：
calc(1,2,3)

法二：
nums = [1,2,3]
calc(*nums)
"""

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum