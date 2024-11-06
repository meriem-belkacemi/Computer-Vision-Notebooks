import cv2
import numpy as np

sizeDilate = 1
sizeErode = 1
iterationsDilate = 1

cv2.namedWindow('erode')
cv2.namedWindow('dilate')

img = cv2.imread("ferrari.jpg",cv2.IMREAD_GRAYSCALE)
cv2.threshold(img, 130, 255, 0, img)

def dilate (): 
    # MORPH_CROSS signifie que le kernel est sous forme d'un + / check support pour les autres options MORPH_RECT pour rectangle
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (sizeDilate*2+1 , sizeDilate*2+1))
    # img_dilate = cv2.dilate(img, kernel, iterations=iterationsDilate)
    img_dilate = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=iterationsDilate)
    cv2.imshow("dilate", img_dilate)
    
def erode (): 
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (sizeErode*2+1 , sizeErode*2+1))
    img_erode = cv2.erode(img, kernel, iterations=1)
    cv2.imshow("erode", img_erode)

def changeDsize(x) :
    global sizeDilate
    sizeDilate = x
    dilate()
    
def changeEsize(x) :
    global sizeErode
    sizeErode = x
    erode()
    
def changeDiterations(x) :
    global iterationsDilate
    iterationsDilate = x
    dilate()

cv2.createTrackbar("size dilate", "dilate", 0, 21, changeDsize)
cv2.createTrackbar("iterations dilate", "dilate", 0, 10, changeDiterations)

cv2.createTrackbar("size erode", "erode", 0, 21, changeEsize)

dilate()
erode()


cv2.imshow("image_src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
