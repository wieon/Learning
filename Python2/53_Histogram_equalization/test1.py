# 直方图均衡化
# 用于增强图像对比度

import matplotlib.pyplot as plt
import cv2

path = r'E:\All_Code\Python_Notepad++\53_Histogram equalization\img1.jpeg'
# 读入图像
img = cv2.imread(path)
# 估计噪声，观察直方图
plt.hist(img.ravel(), bins=256)
plt.title('origin')
plt.show()  # 原始直方图
plt.title('origin')
plt.imshow(img)
plt.show()  # 原始灰度图
'''
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.equalizeHist(img)
plt.hist(img.ravel(), bins=256)
plt.title('systemEqualize')
plt.show()  # 均衡化直方图
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title('systemEqualize')
plt.show()  # 均衡化灰度图
'''
