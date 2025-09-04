# 假设山洞里共有'A', 'B', 'C', 'D', 'E', 'F', 'G'这七件宝物。
# 它们的重量分别是10, 40, 30, 50, 35, 40, 30，
# 它们的价值分别是35, 30, 16, 50, 40, 10, 25。
# 给定承重为150的背包, 怎么装背包，可以才能带走最多的财富。

'''
f1 = [['A','B','C','D','E','F','G'],[10,40,30,50,35,40,30],[35,30,16,50,40,10,25]]
f2= [['A',10,35],['B',40,30],['C',30,16],['D',50,50],['E',35,40],['F',40,10],['G',30,25]]


# 回溯算法，暴力求解
goods = f2
best_v, w, v = 0, 0, 0  # 最大价值best_v，当前重量w，当前价值v
n, c = 7, 150  # n个物品，最大承重c
best_x = []
x = [0 for i in range(n)]  # 放、不放列表，初始化，不放为0，放为1
def backtrack(i):  # i层，共n件物品
    global v, w, best_v, best_x, x  # 当前重量w，当前价值v，最大值v，最优解best_x，当前解x
    if i == n:  # >=也可以
        if best_v < v:
            best_v = v
            best_x = x[:]  # 赋值更新后的x，不写[:]则永远是x，x=[0,0,0,0,0,0,0]
    else:
        if w + goods[i][1] <= c:  # 当前重量加这层物品重量小于等于承重，可以放入背包
            x[i] = 1  # 物品放入背包，更新‘放不放’列表x
            w += goods[i][1]  # 更新重量
            v += goods[i][2]  # 更新价值
            backtrack(i+1)  # 进入下一层（如果符合i==n条件就到底了）
            w -= goods[i][1]  # 到底后回退，准备进入另一侧节点
            v -= goods[i][2]
        x[i] = 0  # 超重则不放入背包，初始化物品状态
        backtrack(i+1)  # 进入下一层
backtrack(0)
result = [goods[i][0] for i in range(n) if best_x[i]==1]  # 根据‘放不放’列表得到符合的物品编号
result = ''.join(result)
result_w = sum([goods[i][1] for i in range(n) if best_x[i]==1])  # 根据‘放不放’列表得到符合的物品总重量
print(f'({result}, ({result_w},{best_v}))')
# print(best_x)
'''

# 动态规划之二维dp数组
lst = [['1', 1, 3], ['2', 3, 4], ['3', 4, 6]]  # 物品编号，重量，价值
bagsize = 4

# 初始化数组
import numpy as np
n, col = 3, 5
dp = np.zeros((n, col), dtype=int)

# 填充数组
for i in range(n):
    for j in range(col):
        if bagsize < lst[i][1]:  # 当前背包放不下物品i
            dp[i][j] = dp[i-1][j]  # 前i-1个物品的价值就是当前的最大价值
        else:
            # 放的下时，可以放也可以不放，取价值更大的那个
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i][1]]+lst[i][2])  # max用()而不是{}

# 打印数组
print(dp)
for i in range(n):
    print()
    for j in range(bagsize+1):
        print(dp[i][j], end='\t')
        


# 优化
# dp算法有后无效性原则，01背包每次只看前一行，前一行之前的那些都是没用的，那就没必要留着
# dp[j] = max(dp[j], dp[j - wᵢ ] + vᵢ )

# n = 7
# max = 150
# w = f[1]
# dp = []
# for i in range(1,n+1):
#     for j in range(150,w[i],-1):    # 注意：这里是逆序
#         if dp[j] >= w[i]:
#             dp[j] = max{dp[j], dp[j-w[i]]+v[i]}

