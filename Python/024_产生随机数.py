import random

a = random.random()  # 随机生成0,1之间的浮点数，左闭右开
b = random.randint(1, 10)  # 随机生成一个整数，闭区间
c = random.randrange(1, 10, 2)  # 返回随机整数，步长为2
d= random.uniform(1,10)  # 随机生成浮点数，左闭右开
print(a, b, c, d)

x = list(range(10))  
random.shuffle(x)  # 将列表中元素打乱
print(x)

n = int(input())  # 输入随机数种子
random.seed(n)
print(random.randrange(100))

# 模拟洗牌
n = int(input())
random.seed(n)
card = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
random.shuffle(card)
print(card)

#生成随机大写字母
# chr(randint(ord('A'), ord('Z')))