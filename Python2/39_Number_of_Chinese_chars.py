# 键盘输入一个字符串，统计中文字符的个数。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
# 基本中文字符的Unicode编码范围是：4E00~9FA5。

text = input()
count = 0
for i in range(len(text)):
    if ord(text[i]) > 0x4E00 and ord(text[i]) < 0x9FA5:
       count += 1
print(count)