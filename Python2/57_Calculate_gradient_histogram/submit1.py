from skimage import feature as ft
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'E:\All_Code\Python_Notepad++\57_Calculate_gradient_histogram\img3.JPEG', cv2.IMREAD_GRAYSCALE)
features = ft.hog(img,orientations=9,pixels_per_cell=[16,16],cells_per_block=[20,30],visualize=True, feature_vector= True)

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.imshow(img, cmap=plt.cm.gray)
ax2.imshow(features[1],cmap=plt.cm.gray)
plt.show()
