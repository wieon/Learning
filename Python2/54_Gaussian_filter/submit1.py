# 直方图均衡化
# 用于增强图像对比度

import matplotlib.pyplot as plt
import cv2

path = r'E:\All_Code\Python_Notepad++\53_Histogram equalization\img1.jpeg'
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.hist(img.ravel(), bins=256)
plt.title('origin')
plt.show()  # 原始直方图
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.title('origin')
plt.imshow(img)
plt.show()  # 原始灰度图
 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.equalizeHist(img)
plt.hist(img.ravel(), bins=256)
plt.title('systemEqualize')
plt.show()  # 均衡化直方图
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title('systemEqualize')
plt.show()  # 均衡化灰度图

# 高斯滤波
# 去除噪点
path = r'E:\All_Code\Python_Notepad++\54_Gaussian_filter\img1.jpeg'
Gn=cv2.imread(path) 
Gf=cv2.GaussianBlur(Gn,(3,3),0,0)
cv2.imshow("噪声图像",Gn)
cv2.imshow("高斯滤波处理结果图像",Gf)
cv2.waitKey()
cv2.destroyAllWindows()