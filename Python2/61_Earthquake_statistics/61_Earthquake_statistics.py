def type_judge(input_str):
    # 接收一个字符串为参数，根据参数调用不同的函数进行运算。
    if input_str == '震源深度':
        depth_of_focus(data)
    elif input_str == '震级':
        magnitude(data)
    else:
        others(data)

def depth_of_focus(data_lst):
    n = int(input())
    data_sort_asc = sorted(data_lst, key=lambda x: eval(x[-2]))
    print('从低到高前{}名:'.format(n))
    for i in data_sort_asc[:n]:
        print('{}:{}千米'.format(i[-1], i[-2]))
    print()

    print('从高到低前{}名:'.format(n))
    data_sort_desc = sorted(data_lst, key=lambda x: eval(x[-2]),reverse=True)
    for i in data_sort_desc[:n]:
        print('{}:{}千米'.format(i[-1], i[-2]))


def magnitude(data_lst):
    n = int(input()) 
    data_sort = sorted(data_lst, key=lambda x: eval(x[1]), reverse=True)
    for i in data_sort[:n]:
        print('{}:{}级'.format(i[-1], i[1]))


def others(data_lst):
    """不是上述情况，在地名中查找输入的字符串，如果存在，则输出该地区数据"""
    flag = 0  # 如果不存在，则输出无数据
    for line in data_lst:
        if question in line[-1]:
            print('{}:{}'.format(line[-1], line[1]))
            flag = 1
    if flag == 0:
        print('无数据')

def read_file(f):
    with open (path,'r',encoding='utf-8') as f:
        data_lst = [i.strip().split(',') for i in f]
        return data_lst[1:]
        
if __name__ == '__main__':
    path = r'E:\All_Code\Python_Notepad++\61_Earthquake_statistics\quake.csv'
    data = read_file(path)
    question = input()
    type_judge(question)

