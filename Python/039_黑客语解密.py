# 将英文字母转换为特殊符号
# 0 1 3 4 5 6 7
# o i e a s g t

num = '0134567'
letter = 'oieasgt'
word = 'M4k3 G006l3 Y0ur H0m3p463!'
origin = ''
for i in range(len(word)):
    if word[i] in num:
        j = num.index(word[i])
        origin += letter[j]
    else:
        origin += word[i]
print(origin)

# table = ''.maketrans(before, after),这条语句可以创建映射表
# str1.translate(table)语句可以将table中的字符按映射表中的顺序进行替换
# 法二

str_before = '0134567'
str_after = 'oieasgt'
# table = 'M4k3 G006l3 Y0ur H0m3p463!'.maketrans(str_before, str_after)
# print(table)
# {48: 111, 49: 105, 51: 101, 52: 97, 53: 115, 54: 103, 55: 116}
table = ''.maketrans(str_before, str_after)
print(word.translate(table))