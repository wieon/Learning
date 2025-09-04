# 输入一组数字，采用逗号分隔，输出其中的最大值。

'''
a = input().split(',')
print(max(a))
# 失败！！！
# 要把列表中的数由字符串转为数字
# 不然如果有相同数，比大小会错误
# ['9','9','10'] => 9
'''
a = input().split(',')
b = [eval(x) for x in a]
print(max(b))
