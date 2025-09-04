with open('E:\\All_Code\\C_vscode\\python练习题2\\admit2.csv', 'r', encoding='utf-8') as f:
    # data = f.readlines()  # 每行末尾有换行符
    # readline()每次返回一行，返回字符串
    # readlines()返回全部，返回列表
    # data = [i.strip() for i in f.readlines()]  # strip()函数去掉每行末尾换行符
    data = [i.strip().split(',') for i in f.readlines()[1:]]  # 输出二维列表，不要表头
# print(data)

n = input()
if n == '1':
    data = [i for i in data if eval(i[-1]) >= 0.8]
    data_tar = [i for i in data if eval(i[11]) > 4]
    print('Top University in >=80%:{:.2f}%'.format(len(data)/len(data_tar)*100))
elif n == 'Research':
    data2 = [i for i in data if eval(i[-1]) >= 0.9]
    data3 = [i for i in data if eval(i[-1]) <= 0.7]
    data_tar = [i for i in data if eval(i[-4]) == 1]
    print('Research in >=90%:{:.2f}%'.format(len(data2)/len(data_tar)*100))
    print('Research in <=70%:{:.2f}%'.format(len(data3)/len(data_tar)*100))
elif n == '2':
    data = [eval(i[3]) for i in data if eval(i[-1]) >= 0.8]
    # print(data)
    print('TOEFL Average Score:{:.2f}'.format(sum(data)/len(data)))
    print('TOEFL Max Score:{:.2f}'.format(max(data)))
    print('TOEFL Min Score:{:.2f}'.format(min(data)))
elif n == '3':
    data = [eval(i[4]) for i in data if eval(i[-1]) >= 0.8]
    print('CGPA Average Score:{:.3f}'.format(sum(data)/len(data)))
    print('CGPA Max Score:{:.3f}'.format(max(data)))
    print('CGPA Min Score:{:.3f}'.format(min(data)))
else:
    print('ERROR')