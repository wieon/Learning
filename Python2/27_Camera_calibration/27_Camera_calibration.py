# 题目：
# 编程实现从给定的文件中读入三维点坐标，自己设定相机的内外参数，
# 将三维点进行投影，得到对应的像素坐标。并根据像素坐标和三维点坐标，
# 通过SVD分解和QR分解，得到相机的内参数矩阵K以及外参数R和T。

# 要求：输出自己设定的内外参数以及计算得到的内外参数。


'''
# 打开文件读取数据，法一
file = open(r'E:\All_Code\Python_Notepad++\27_Camera_calibration\house.p3d','r')
file_content = file.read()
file.close()
print(file_content)

# open（）完成后必须调用close()方法关闭文件，因为文件对象会占用
操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的。
with open()则可以避免这样的情况。
'''

'''
# 调用readline()可以每次读取一行内容，一次读取所有内容并按行返回list
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，
# 反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便。

# 法二
import numpy as np

# 在路径前加个r就不会报错 ***
file_path = r'E:\All_Code\Python_Notepad++\27_Camera_calibration\house.p3d'
with open(file_path, 'r') as f: 
	# 读取一行数据，数据按空格分隔，转化为列表
	line = f.readline().split()  
	# 列表中的数据从字符串转化为浮点数
	list = [float(x) for x in line]
	# 将列表转为numpy矩阵，可以用dtype=float确保为浮点数类型矩阵
	matrix = np.array(list)
	matrix2 = np.transpose(matrix)
# 太占内存了，换一种方法！
'''

'''
import numpy as np
import cv2
# from cv2 import VideoCapture, Mat, findHomography

# 读取文件中的数据
file_path = r'E:\All_Code\Python_Notepad++\27_Camera_calibration\house.p3d'
file_path2 = r'E:\All_Code\Python_Notepad++\27_Camera_calibration\house.txt'


# 这段的主要目的是将.p3d中的文件读到.txt文件中，
# 运行一次成功就可以注释掉了，不然文件中的数据
# 会随着每次调试越来越多。
# with open(file_path, 'r') as f: 
    # text = f.read()
    # data_file = open(file_path2, 'a')
    # data_file.write(text)
    # data_file.close()



with open(file_path2, 'r') as f2:
    text2 = f2.read()
    # np.loadtxt()可以高效的导入数据，默认读取float类型的值
    # 读入矩阵，三维点坐标为行，维度为n*3
    data_array = np.loadtxt(file_path2) 
    # print(len(data_array))  # 672
    # print(np.shape(data_array))  # （672,3）

    

# 取简化值
a, b = 1, 1
cx, cy = 10, 10
s = 0
# 定义相机内参数
K = np.array([[a, s, cx], [0, b, cy], [0, 0, 1]])


# 定义相机外参数，取简化值
R = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
T = [[0],[0],[0]]
# 将R和T水平拼接成一个矩阵，维度为3*4
# axis=1为沿着列的轴进行拼接
R_T = np.concatenate((R, T), axis=1)



# 构建世界坐标矩阵，比例（？）为1
rows = len(data_array)
list0 = np.ones((rows, 1), dtype=float)
# 生成世界坐标，维度为4*n
Pw = np.concatenate((data_array, list0), axis=1).T


# 求对应的像素坐标
# 公式：P = M * Pw = K * [R_T] * Pw
M = np.dot(K, R_T)
P = np.dot(M, Pw)


# --------------------目前到这都可以正常运行------------------

# 图像尺寸，以像素为单位，通常是一个元组，(width, height)
image_size = (1080, 720)
# 终止条件,通常是(type, maxCount, epsilon)的元组，其中 type 是终止条件的类型，maxCount 是最大迭代次数，epsilon 是精度要求
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 物体坐标，3*n
Pw_3_n = data_array.T
# cv2.calibrateCamera函数需要多张输入图片，读取成list或者np类型，该类型中每一个存储都是np类型，且object_Points必须是整数
# Pw_3_n中的数据基本都在-2~2之间，小数点后五位，现要将它们变为整数

# Pw_3_n_int = Pw_3_n.astype(int)
# object_points = np.expand_dims(Pw_3_n, axis=0)
# image_points = np.expand_dims(P, axis=0)
obj_points = [Pw_3_n.astype(np.float64)]
img_points = [P.astype(np.float64)]

# print(Pw_3_n)
# print(P)
# print(object_points)
# print(image_points)
# print(obj_points.dtype)
# print(img_points.dtype)


# 畸变矩阵
dist = np.zeros((1, 5))

# 输入：世界坐标系里的位置 像素坐标 图像的像素尺寸大小 3*3矩阵(相机内参数矩阵) 畸变矩阵 畸变系数的标定 迭代优化算法的终止条件
# 输出：标定结果 相机的内参数矩阵 畸变系数 旋转矩阵 平移向量
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, image_size, K, dist, None, criteria)



# 输出
print(f'自己设定的内参数K：{K}')
print(f'自己设定的外参数R：{R}')
print(f'自己设定的内参数T：{T}')
print(f'计算得到的内参数K’：{camera_matrix}')
print(f'计算得到的内参数R’：{rvecs}')
print(f'计算得到的内参数T’：{tvecs}')
'''



import numpy as np
from scipy.spatial.transform import Rotation as R
import copy
import cv2
import matplotlib.pyplot as plt
 
def calculate_world_corner(corner_scale, square_size):
    corner_height, corner_width = corner_scale
    obj_corner = np.zeros([corner_height * corner_width, 3])
    obj_corner[:, :2] = np.mgrid[0:corner_height, 0:corner_width].T.reshape(-1, 2)  # (w*h)*2
    return obj_corner * square_size
 
 
img_size = [960, 960]
focal = 1200
pix_spacing = 0.309
K = np.array([[focal/pix_spacing, 0, img_size[0]/2],
              [0, focal/pix_spacing, img_size[1]/2],
              [0, 0, 1]])
dist = np.zeros((1, 5)) 
 
euler_in = [45, 0, 0]
rvecs_in = R.from_euler('xyz', euler_in, degrees=True).as_rotvec()[None].reshape(3, 1)
tvecs_in = np.array([[0], [0], [1000]]).astype(np.float64)
 
obj_points = calculate_world_corner([5, 5], 25)
img_points, _ = cv2.projectPoints(obj_points, rvecs_in, tvecs_in, K, dist)
 
img_points_list = [img_points.astype(np.float32)]
obj_points_list = [obj_points.astype(np.float32)]
 
K_in = copy.deepcopy(K)  # 这一行是因为输入cv2.calibrateCamera()后K会变化
retval, cameraMatrix, distCoeffs, rvecs, tvecs = cv2.calibrateCamera(obj_points_list, img_points_list, img_size, K_in, dist)
 
euler = R.from_rotvec(rvecs[0].T).as_euler('xyz', degrees=True)
 
print('理论相机内参：\n', K)
print('求解相机内参：\n', cameraMatrix)
# print('理论旋转欧拉角：\n', euler_in)
# print('求解旋转欧拉角：\n', euler[0])
# print('理论旋转向量：\n', rvecs_in)
# print('求解旋转向量：\n', np.asarray(rvecs))
print('理论位移向量：\n', tvecs_in)
print('求解位移向量：\n', np.asarray(tvecs))
# print('重投影误差：\n', retval)
# print('畸变系数：\n', distCoeffs)
