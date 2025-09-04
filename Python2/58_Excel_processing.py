'''
import pandas as pd
import os

folder_path = r'E:\BUCM\大学生活\一临青协\2024_11_03传统医药大会志愿者招募\报名'
filepath0 = r'E:\BUCM\大学生活\一临青协\2024_11_03传统医药大会志愿者招募\0.xlsx'
extension = 'xlsx'
files = [file for file in os.listdir(folder_path) if file.endswith('.' + extension)]

# print(files)
# print(len(files))

testpath = os.path.join(folder_path, '柴子涵.xlsx')
df = pd.read_excel(testpath, skiprows=3, nrows=1)
df.to_excel(filepath0, index=False)
'''


'''
for file in files:
    filepath = os.path.join(folder_path, file)
    df = pd.read_excel(filepath, skiprows=3, nrows=1)   
    print(df)
  

    # ------- 到这都可以运行 ------
    with open(filepath0, 'a') as f:
        # index=False 参数表示不将行索引写入到Excel文件中
        # 如果想指定特定的工作表或者列名，可以使用sheet_name和columns参数
        df.to_excel(filepath0, index=False)
'''

'''
# 因为之前的编码格式是gbk，一般常用另一个格式是utf-8，所以在这里我们加上编码格式即可正常运行。
with open(filepath0, 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
'''

# ----------------------------以上失败----------------------------------

import xlwt
import os

folder_path = r'E:\BUCM\大学生活\一临青协\2024_11_03传统医药大会志愿者招募\报名'
filepath0 = r'E:\BUCM\大学生活\一临青协\2024_11_03传统医药大会志愿者招募\0.xlsx'
extension = 'xlsx'
files = [file for file in os.listdir(folder_path) if file.endswith('.' + extension)]
for file in files:
    filepath = os.path.join(folder_path, file)
    excel_obj = xlrd.open_workbook(filepath)
    getcontent = excel_obj.row(4)
    sheet = 