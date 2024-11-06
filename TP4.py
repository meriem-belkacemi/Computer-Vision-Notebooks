import cv2
import numpy as np

th = 0
type = 0

img = cv2.imread("ferrari.jpg",cv2.IMREAD_GRAYSCALE)
imgRes = np.zeros(img.shape, img.dtype)


# # Laplacien
# kernel1 = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

# # Gaussien
# kernel2 = np.array([[1,2,1],[2,4,2],[1,2,1]])
# kernel2 = kernel2 / 16

# imagesResLaplacien = cv2.filter2D(img , -1, kernel1)
# imagesResGaussien = cv2.filter2D(img , -1, kernel2)


def afficher() :
    cv2.threshold(img, th, 255, type, imgRes)
    cv2.imshow("result" , imgRes)

def changeTh(x) :
    global th
    th = x
    afficher()
     
def changeType(x) :
    global type
    type = x
    afficher()

cv2.namedWindow("result")
afficher()
cv2.createTrackbar("threshold", "result", 0, 255, changeTh)
cv2.createTrackbar("type", "result", 0, 4, changeType)
cv2.waitKey(0)
cv2.destroyAllWindows()
