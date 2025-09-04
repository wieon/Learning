# 学习使用pd.describe()函数

import pandas as pd

# 创建一个简单的DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# 使用describe()函数
description = df.describe()
print(description)
description[]

'''
import pandas as pd
from matplotlib import pyplot as plt

# 创建一个简单的DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# 使用describe()函数定制输出
custom_description = df.describe(percentiles=[.30, .60, .90])
print(custom_description)

# 绘制箱线图
df.boxplot()
plt.show()
'''

'''
# include, exclude: 有all,number,object,none
import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# 只统计数值型数据
print(df.describe(include='number'))
'''
