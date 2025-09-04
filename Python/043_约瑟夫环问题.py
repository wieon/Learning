# 描述
# 据说著名历史学家 Josephus有过以下的故事：Josephus及他的朋友共41人围成一个圆圈，由第1个人开始报数，
# 每数到3该人就必须出去，然后再由下一个人重新报数，直到圆圈上少于3人为止。
# Josephus 将朋友与自己安排在第16个与第31个位置，成为最后剩下的人。

# 扩展这个问题，当人数为n，每次报数为k时，求解最后的K-1个剩下的人的位置

# 输入格式
# 在同一行内输入两个正整数n和k，要求k > = 2且n >= k

# 输出格式
# 以列表形式显示剩余的人的序号（如果k<2 或者n<k,打印"Data Error!")


def Josephus():
    lst = list(range(1, n+1))
    while len(lst) > k-1:
        lst = lst[k:] + lst[:k-1]  # 哪个天才想出来的，太妙了！！！！！
    return lst

n, k = map(int, input().split())
if n < k or k < 2:
    print('Data Error!')
else:
    # lst = [i for i in range(1, n+1)]
    print(Josephus())
        