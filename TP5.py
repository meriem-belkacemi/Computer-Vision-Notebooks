import cv2
import numpy as np

img = cv2.imread("ferrari.jpg",cv2.IMREAD_GRAYSCALE)

# Laplacien
kernel1 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

# Gaussien
kernel2 = np.array([[1,2,1],[2,4,2],[1,2,1]])
kernel2 = kernel2 / 16

# Laplacien + image 
kernel3 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])


imagesResLaplacien = cv2.filter2D(img , -1, kernel1)
imagesResGaussien = cv2.filter2D(img , -1, kernel2)
imagesResLaplacienModified = cv2.filter2D(img , -1, kernel3)



cv2.imshow('image', img)
cv2.imshow('imageResLaplacien', imagesResLaplacien)
cv2.imshow('imageResGaussien', imagesResGaussien)
cv2.imshow('imageResGaussienModified', imagesResLaplacienModified)


cv2.waitKey(0)
cv2.destroyAllWindows
