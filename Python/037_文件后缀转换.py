import os
for root, dirs, files in os.walk("E:\\All_Code\\python练习题"):
    for file in files:
        # # print(os.path.join(root, file))
        # filepath = os.path.join(root, file)
        # # print(filepath[-3:])
        # if filepath[-3:] == 'txt':
        #     filepath = filepath.replace(filepath[-3:], 'py')
        # print(filepath)

        oldpath = os.path.join(root, file)
        if oldpath[-3:] == 'txt':
            newpath = oldpath.replace(oldpath[-3:], 'py')
            os.rename(oldpath, newpath)
        # 当文件已存在时，无法创建该文件。

