'''
在一个由若干个排列整齐的数组成的正方形中，图中任意一横行、一纵行及对角线的几个数之和都相等，
具有这种性质的图表，称为“幻方”。中国古代称为“河图”、“洛书”。
洛书蕴含奇门遁甲的布阵之道，九宫之数源于《易经》。幻方也称九宫图、纵横图、魔方、魔阵，它是科学的结晶与吉祥的象征。

古人总结的三阶幻方口诀为：

二四为肩，
六八为足，
载九履一，
左三右七，
五居中央

幻方不限于3阶，当N为奇数时，可用以下的方法来填数。

（1）将1填入第一行的中间；

（2）将每一个数字依次放在前一个数的右上方一格（行号减1列号加1）。

    （i）  出现越界。如果这个数所要放的格已经超出了第一行，那么就把他放在最后一行，仍然放在右一列（列号加1，参考数字“2”）。
    如果这个数所要放的格已经超过最右列，那么就把他放在最左列的上面一行（行号减1，参考数字“57”）。

    （ii）没越界，如果这个数所要放的格已经有数了，此时将其填在这个数的正下方一格（行号加1列号不变，参考数字“10”）。

（3）矩阵的最右上方的格子（第一行最后一列）中数的下一个数填在这个数的正下方一格（参考数字“46”）。

参考9阶幻方的结果，理解幻方填数方法，编程输出奇数阶幻方。

输入格式：
输入一个大于0的奇数N

输出格式：
N阶幻方
'''


def magic_square(n):
    m = [[0 for i in range(n)] for i in range(n)]
    row, col = 0, n//2
    for i in range(1, n**2+1):
        m[row][col] = i
        rowa = row - 1  # 如果这里没有另设一个数就会算错
        cola = col + 1  # 另设一个数表示假设情况
        if rowa < 0:  # 移动情况
            rowa = n-1
        if cola > n-1:
            cola = 0
        if m[rowa][cola] != 0:  # 占位情况
            row = row + 1
            if row > n-1:
                row = 0
        else:  # 最右上角的那种情况，由于左下角已经有数了，所以相当于占位情况
            row, col = rowa, cola
    return m

n = int(input())
if __name__ == '__main__':
    lst = magic_square(n)
    for i in range(n):
        print(*lst[i])



# def magic_square(n):
#     # 构造二维列表
#     lst = [[0 for i in range(n)] for i in range(n)]
#     # 初始化列表位置
#     x, y = 0, n // 2
#     for num in range(1, n * n + 1):
#         lst[x][y] = num
#         xa, ya = x - 1, y + 1
#         # 回绕情况
#         if xa < 0:
#             xa = n - 1
#         if ya > n - 1:
#             ya = 0
#         # 占位情况
#         if lst[xa][ya] != 0:
#             x = x + 1
#             if x > n - 1:
#                 x = 0
#         else:
#             x, y = xa, ya
#     return lst
 
 
# m = int(input())
# ls = magic_square(m)
# for row in ls:
#     print(*row)