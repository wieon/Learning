# 法一，find()函数
a = 'hello world'
b = 'world'
c = 'worlds'
print(a.find(b))
print(a.find(c))

# 法二，正则表达式，re模块的search()
# start() 和 end() 方法获取子字符串的起始和结束索引位置
# 通过 group() 方法获取匹配的子字符串
import re
y = 'hello world'
x = 'or'
match = re.search(x, y)
if match:
	start = match.start()
	end = match.end()
	string = match.group()
	print(f'{string} found at {start}-{end-1}')
else:
	print('Not found')
