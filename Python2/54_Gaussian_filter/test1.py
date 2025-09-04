# 高斯滤波
# 去除噪点

import cv2
path = r'E:\All_Code\Python_Notepad++\54_Gaussian_filter\img1.jpeg'
Gn=cv2.imread(path) 
Gf=cv2.GaussianBlur(Gn,(3,3),0,0)
cv2.imshow("噪声图像",Gn)
cv2.imshow("高斯滤波处理结果图像",Gf)
cv2.waitKey()
cv2.destroyAllWindows()


'''
import cv2
import numpy as np
import pyps.pyzjr.utility as zjr
path = r'E:\All_Code\Python_Notepad++\54_Gaussian_filter\img1.jpeg'
img = cv2.imread(path)
 
def gaussian_kernel(size, sigma):
    kernel = np.zeros((size, size), dtype=np.float32)
    center = size // 2
 
    for i in range(size):
        for j in range(size):
            x, y = i - center, j - center
            kernel[i, j] = np.exp(-(x**2 + y**2)/(2*sigma**2))
    kernel /= 2 * np.pi * sigma**2
    kernel /= np.sum(kernel)
    return kernel
 
def Gaussian_Filtering(img, kernel_size, sigma):
    kernel = gaussian_kernel(kernel_size, sigma)
    height, width, channels = img.shape
    result = np.zeros_like(img, dtype=np.float32)
 
    pad_size = kernel_size // 2
    img_pad = np.pad(img, [(pad_size, pad_size), (pad_size, pad_size), (0, 0)], mode='constant')
    for c in range(channels):
        for i in range(pad_size, height + pad_size):
            for j in range(pad_size, width + pad_size):
                result[i - pad_size, j - pad_size, c] = np.sum(kernel * img_pad[i - pad_size:i + pad_size + 1, j - pad_size:j + pad_size + 1, c])
    return np.uint8(result)
 
imgGaussianBlur_1 = Gaussian_Filtering(img, 1, 1.5)
imgGaussianBlur_3 = Gaussian_Filtering(img, 3, 1.5)
imgGaussianBlur_5 = Gaussian_Filtering(img, 5, 1.5)
imgGaussianBlur_7 = Gaussian_Filtering(img, 7, 1.5)
imgStack = zjr.stackImages(0.6, ([imgGaussianBlur_1, imgGaussianBlur_3], [imgGaussianBlur_5, imgGaussianBlur_7]))
cv2.imshow("imges",imgStack)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
