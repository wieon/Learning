# def menu():
#     print('''\n欢迎使用PYTHON学生通讯录
# 1：添加学生
# 2：删除学生
# 3：修改学生信息
# 4：搜索学生
# 5：显示全部学生信息
# 6：退出并保存''')

# dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}

# 首先输出字典原始数据，再调用menu函数输出用户选择界面，接下来读用户输入：

# 输入‘1’ 进行添加学生，输入姓名，如果该姓名已存在，则输出“Fail”的提示信息，如果不存在，继续输入电话和所在学院。
# 添加完毕后输出“Success”提示信息。
# 无论是否添加成功，结束后需要输出操作后的字典数据。
# 如果输入其他选项，无需再读姓名，直接输出“ERROR”。


def menu():
    print('''\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存''')

dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}

def add_student():
    name = input()
    if name in dic:
        print('Fail')
    else:
        phone = input()
        college = input()
        dic[name] = [phone, college]
        print('Success')
        print(dic)

if __name__ == '__main__':
    print(dic)
    menu()
    num = input()
    if num == '1':
        add_student()
    else:
        print('ERROR')
