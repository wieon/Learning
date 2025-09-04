# 比较三个数大小，按从小到大输出
li = input().split()
li = list(map(int, li)) # 将列表中字符串转为数字
li2 = sorted(li)
print(li2[0], li2[1], li2[2])

# sort函数在原位排序，sorted函数产生一个新的列表
'''
# map函数用法，可与匿名函数结合使用
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]
 
TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)
 
print(list(carts))
'''