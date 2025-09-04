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