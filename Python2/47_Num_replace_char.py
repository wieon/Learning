# 获得用户输入的一个数字，替换其中 0~9 为中文字符“〇一
# 二三四五六七八九”，输出替换后结果。


n = input()
s = "〇一二三四五六七八九"

for i in range(len(n)):
	num = eval(n[i])
	# n.replace()一次只能替换一个，且不会保存在n，需要再次赋值给n
	n = n.replace(n[i], s[num], 1) 
print('请输入一个数字：{}'.format(n))  # 杀匕网站


# replace()查到旧字符串中有符合的就全换了，故而第二次有相同的就会
# 没的换。故输入'2,2'会报错。
# str.replace(old, new[, count])
# count（可选）：替换次数，默认为全部替换。
