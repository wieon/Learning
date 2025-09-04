
def read_file(f):
    with open(f,'r',encoding='gbk') as f:
        data_ls = [i.strip().split(',') for i in f]
        return data_ls[1:]
        
def type_judge(input_str):
    if input_str == 'record':
        record(data)
    elif input_str == 'rank':
        rank(data)
    elif input_str == 'maxcomment':
        pass
    elif input_str == 'maxname':
        pass
    else:
        pass

# 统计输出图书数据的总数量 KO
def record(data):
    print(len(data))

# 输入一个书籍编号，分别输出编号对应的书籍信息 KO
def rank(data):
    num = eval(input())
    if num < 86:
        # print(data[num-1])
        [print(i) for i in data[num-1]]
    else:
        [print(i) for i in data[num-2]]

# 输出评论数量最多的10本书的书名和评论数，按评论数量降序排序  wrong!
def maxcomment(data):
    for i in data:
        ls = i[-2][:-3]
    print(ls)
    comment_sort = sorted(ls, key=lambda x: eval(x[-2]), reverse=True)
    print(comment_sort)
    for i in comment_sort[:10]:
        print('{} {}'.format(i[1], i[-2]))

if __name__ == '__main__':
    file = r'E:\All_Code\Python_Notepad++\62_Book_statistics\CBOOK.csv'
    data = read_file(file)
    question = input()
    type_judge(question)

'''
import pandas as pd

def type_judge(input_str):
    if input_str == 'record':
        record(data)
    elif input_str == 'rank':
        rank(data)
    elif input_str == 'maxcomment':
        pass
    elif input_str == 'maxname':
        pass
    else:
        pass

# 统计输出图书数据的总数量 KO
def record(data):
    print(data['编号'].max())

# 输入一个书籍编号，分别输出编号对应的书籍信息 KO
def rank(data):
    num = eval(input())
    info = data[data['编号'] == num]
    print(info)
    
if __name__ == '__main__':
    path = r'E:\All_Code\Python_Notepad++\62_Book_statistics\CBOOK.csv'
    data = pd.read_csv(path, encoding='gbk')
    question = input()
    type_judge(question)
'''

#!!!!!!!为什么这个可以成功啊！！！！！！
def maxname(n):  # 输出名字最长的十本书,长度相同以现价从高到低排序
    ls.sort(key=lambda x: (len(x[1]), eval(x[3])), reverse=True)
    for i in ls[:n]:
        print(i[1])

def number():
    print(len(ls))

def maxcomment():  # 评论数量多的书籍前10
    l = sorted(ls, key=lambda x: eval(x[-2][:-3]), reverse=True)
    for i in l[:10]:
        print(i[1], i[-2])

def rank():
    n = input()
    for i in ls:
        if n == i[0]:
            for j in i:
                print(j)
            break

with open('CBOOK.csv', 'r', encoding='GBK') as f:
    ls = []
    for i in f.readlines()[1:]:
        ls.append(i.strip().split(','))

c = input().lower()
if c == 'record':
    number()
elif c == 'rank':
    rank()
elif c == 'maxname':
    n=eval(input())
    maxname(n)
elif c == 'maxcomment':
    maxcomment()
else:
    print('无数据')
