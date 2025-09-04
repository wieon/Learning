list1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
list2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ori_list = input()
ori_list = [char for char in ori_list]
code_list = []
for i in range(len(ori_list)):
	if ori_list[i] in list1:  # 大写字母的加密
		num1 = list1.index(ori_list[i])
		num1 += 3
		code_list.append(list1[num1%26])
	elif ori_list[i] in list2:  # 小写字母的加密
		num2 = list2.index(ori_list[i])
		num2 += 3
		code_list.append(list2[num2%26])
	else:  # 数字和汉字保留不加密，空格也保留（sb网站，为什么不要排除*！%等奇怪的符号，不加提示符，用户误输入了怎么办）
		code_list.append(ori_list[i])
for j in range(len(code_list)):
	print(code_list[j],end="")  # 打印列表中的凯撒密码