import cv2
import numpy as np

img =  cv2.imread("ferrari.jpg",cv2.IMREAD_COLOR)


img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_uint16 = np.uint16(img)
img_uint16 *= 255

img_float32 = np.float32(img)
img_float32 /= 255


img_b = np.zeros(img.shape, img.dtype)
img_g = np.zeros(img.shape, img.dtype)
img_r = np.zeros(img.shape, img.dtype)

h,w,c = img.shape

for y in range(h) :
    for x in range(w) :
        img_b[y,x,0] = img[y,x,0]
        img_g[y,x,1] = img[y,x,1]
        img_r[y,x,2] = img[y,x,2]
        

# img_b[:,:,0] = img[:,:,0] avec les crochets on modifie une image deja existante donc de 3 dimensions 
# img_b= img[:,:,0] par contre celle-ci crée une nouvelle image de deux dimensions donc le niveau de gris est considéré 


cv2.imshow('Image', img)
cv2.imshow('Image HSV', img_HSV)
cv2.imshow('Image uint16', img_uint16)
cv2.imshow('Image float32', img_float32)
cv2.imshow('Image B', img_b)
cv2.imshow('Image G', img_g)
cv2.imshow('Image R', img_r)

cv2.waitKey(0)
cv2.destroyAllWindows