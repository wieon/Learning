
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
 
'''
file_path2 = r'E:\All_Code\Python_Notepad++\27_Camera_calibration\house.txt'
with open(file_path2, 'r') as f2:
    text2 = f2.read()
    # np.loadtxt()可以高效的导入数据，默认读取float类型的值
    # 读入矩阵，三维点坐标为行，维度为n*3
    data_array = np.loadtxt(file_path2)
'''

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

# obj_points = np.array([[0.,0.,0.],[1.,0.,0.],[0.,0.,1.],[0.,1.,0.],[1.,2.,3.],[2.3,3.2,5.6]])
obj_points = calculate_world_corner([5, 5], 25)
# obj_points = data_array
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
