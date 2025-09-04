# 傅里叶变换
# 写程序实现以下功能：
# 1. 载入图像，进行傅里叶变换，显示得到的频谱图像。
# 2. 去除频谱图像中的高频部分，进行反变换，显示得到的图像。
# 3. 去除频谱图像中的低频部分，进行反变换，显示得到的图像。


import cv2
import numpy as np
import matplotlib.pyplot as plt


# 傅里叶变换
path = r'E:\All_Code\Python_Notepad++\55_Fourier_transformation\img1.jpg'
img = cv2.imread(path,0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
result = 20*np.log(np.abs(fshift))

# 傅里叶逆变换
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(result, cmap = 'gray')
plt.title('result')
plt.axis('off')
plt.show()

plt.subplot(121)
plt.imshow(result, cmap = 'gray')
plt.title('result')
plt.axis('off')
plt.subplot(122)
plt.imshow(iimg, cmap = 'gray')
plt.title('iimg')
plt.axis('off')
plt.show()


# 高通滤波器
# 衰减低频通过高频
# 增强尖锐细节，降低对比度
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
ishift_high = np.fft.ifftshift(fshift)
iimg_high = np.fft.ifft2(ishift_high)
iimg_high = np.abs(iimg_high)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('original'),plt.axis('off')
plt.subplot(122),plt.imshow(iimg_high, cmap = 'gray')
plt.title('iimg_high'),plt.axis('off')
plt.show()

# 低通滤波器
# 变模糊
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fShift = dftShift*mask
ishift = np.fft.ifftshift(fShift)
iImg = cv2.idft(ishift)
iImg= cv2.magnitude(iImg[:,:,0],iImg[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('original'), plt.axis('off')
plt.subplot(122),plt.imshow(iImg, cmap = 'gray')
plt.title('inverse'), plt.axis('off')
plt.show()
