
# 傅里叶变换
# 写程序实现以下功能：
# 1. 载入图像，进行傅里叶变换，显示得到的频谱图像。
# 2. 去除频谱图像中的高频部分，进行反变换，显示得到的图像。
# 3. 去除频谱图像中的低频部分，进行反变换，显示得到的图像。

'''
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# Numpy实现傅里叶变换及逆变换
def Fourier_Transform_FFT(img):
    # 实现傅里叶变换
    fft_img = np.fft.fft2(img)
    # 将计算出来的DC分量居中
    fff_shift = np.fft.fftshift(fft_img)
    fff_result = np.log(np.abs(fff_shift))
    # 实现傅里叶逆变换
    ifft_shift = np.fft.ifftshift(fff_shift)
    ifft_t = np.fft.ifft2(ifft_shift)
    ifft_img = np.abs(ifft_t)
    plt.subplot(121)
    plt.title("Origin")
    plt.imshow(img)
    plt.subplot(122)
    plt.title("Fourier_Transform_FFT")
    plt.imshow(fff_result)
    plt.show()
    plt.subplot(121)
    plt.title("Origin")
    plt.imshow(img)
    plt.subplot(122)
    plt.title("Fourier_Transform_TFFT")
    plt.imshow(ifft_img)
    plt.show()
    plt.subplot(121)
    plt.title("Fourier_Transform_FFT")
    plt.imshow(fff_result)
    plt.subplot(122)
    plt.title("Fourier_Transform_TFFT")
    plt.imshow(ifft_img)
    plt.show()
if __name__ == '__main__':
    path = r'E:\All_Code\Python_Notepad++\55_Fourier_transformation\img1.jpg'
    img = cv.imread(path,0)
    Fourier_Transform_FFT(img)
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


# 傅里叶变换
path = r'E:\All_Code\Python_Notepad++\55_Fourier_transformation\img1.jpg'
img = cv2.imread(path,0)
# 傅里叶变换函数
f = np.fft.fft2(img)
# 函数参数主要是np.fft.fft2()函数的输出，即复数数组。此函数可以将零频率分量移到频谱中心。
# 变换之后的频谱显示范围从[0, N]变为：[-N/2,N/2-1]（N为偶数）或[-(N-1)/2,(N-1)/2]（N为奇数）。
fshift = np.fft.fftshift(f)
# 函数参数主要是np.fft.fftshift()函数的输出，傅里叶变换得到的结果是一个复数数组，
# 不能直接用于显示图像，要想得到频谱灰度图像，需要一个映射，把复数映射[0, 255]之间。
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
