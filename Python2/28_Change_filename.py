# 批量修改同一文件夹下的文件名，把空格替换为下划线

import os

# 设置需要修改的文件夹路径
folder_path = 'E:\All_Code\Python_Notepad++'

# 获取文件夹中的所有文件名
file_list = os.listdir(folder_path)

for filename in file_list:
	# 构造新的文件名
	new_filename = filename.replace(' ', '_')
	
	# 构造文件路径
	file_path = os.path.join(folder_path, filename)
	new_file_path = os.path.join(folder_path, new_filename)
	
	# 修改文件名
	os.rename(file_path, new_file_path)
	
print('1')
# 成功！！！