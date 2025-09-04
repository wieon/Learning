with open('E:\\All_Code\\python练习题\\admit2.csv', 'r', encoding='utf-8') as f:
	# data = f.readlines()  # 每行数据末尾有换行符
    data = [i for i in f.readlines()]
print(data)