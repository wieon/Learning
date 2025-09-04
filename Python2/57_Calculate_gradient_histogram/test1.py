from skimage import feature as ft
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'E:\All_Code\Python_Notepad++\57_Calculate_gradient_histogram\img1.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite(r'E:\All_Code\Python_Notepad++\57_Calculate_gradient_histogram\img2.png', img) # 将图片存储为本地
'''
r'./person.png'：读取图像的路径
cv2.IMREAD_GRAYSCALE：将图像转换为单通道灰度图像
'''

print(img.shape)  # 读取图像的像素值325*126

features = ft.hog(img,orientations=9,pixels_per_cell=[8,8],cells_per_block=[2,2],visualize=True, feature_vector= True)
'''
img:读取的图像
orientations=6：指定块的个数。把所有的方向都转换为0°~180°内，然后按照orientation划分块，
如果你选定的orientation= 6, 则bin一共有6个, 每30°有一个。
pixels_per_cell=[20,20]：每个细胞单元的像素数, 是一个tuple类型数据,例如(20,20)
cells_per_block=[2,2]：每个块内有多少个细胞单元, tuple类型, 例如(2,2), 意思是将block均匀划分为2x2的块。
visualize=True：可视化梯度图
feature_vector:返回特征向量
'''

print(features[0]) # 生成一个特征向量
print(features[0].shape) # 特征的长度 = 39*18*9*2*2

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.imshow(img, cmap=plt.cm.gray)
ax2.imshow(features[1],cmap=plt.cm.gray)
# plt.savefig('hog_image.jpg') # 适用于保存任何 matplotlib 画出的图像，相当于一个 screencapture
# cv2.imwrite('hog_image.png', features[1])
plt.show()

