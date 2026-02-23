"""
问题1：请编写程序，提取《论语》文档中所有原文内容，输出保存到
“论语-提取版.txt”文件。输出文件格式要求：去掉文章中原文部分每
行行首空格及如“1.11”等的数字标志，行尾无空格、无空行。

问题2：请编写程序，在“论语-提取版.txt”基础上，进一步去掉每行文
字中所有括号及其内部数字，保存为“论文-原文.txt”文件。
"""

import re

contents = []
# 去除行首空格及数字
with open("057_论语-网络版.txt",encoding="UTF-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.lstrip("0123456789· ")
        contents.append(line)

with open("057_论语-提取版.txt","w",encoding="UTF-8") as f:
    for i in contents:
        f.write(i)


contents2 = []
# 去除文字中的括号及数字
for line in contents:
    line = re.sub(r"\(.*?\)", "", line)  # 去除()及其中中一切字符
    contents2.append(line)

with open("057_论语-原版.txt","w",encoding="UTF-8") as f:
    for i in contents2:
        f.write(i)


