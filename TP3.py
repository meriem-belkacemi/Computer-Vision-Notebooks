import cv2
import numpy as np
import matplotlib.pyplot as plt

vois=7

def filtreMoy(img):
    h,w = img.shape
    imgMoy = np.zeros(img.shape, img.dtype)
    for y in range(h):
        for x in range(w):
            if(y<int(vois/2) or y>int(h-vois/2) or x<int(vois/2) or x>int(w-vois/2)) :
                imgMoy[y,x] = img[y,x]
            else : 
                imgV = img[int(y-vois/2):int(y+vois/2), int(x-vois/2): int(x+vois/2)]
                # moy=0
                # for yv in range(imgV.shape[0]) :
                    # for xv in range(imgV.shape[1]):
                        # moy += imgV[yv, xv]
                # moy /= vois*vois
                # imgMoy[y,x] = moy
                imgMoy[y,x] = np.mean(imgV)

    return imgMoy
                
def filtreMediane(img):
    h,w = img.shape
    imgMediane = np.zeros(img.shape, img.dtype)
    for y in range(h):
        for x in range(w):
            if(y<int(vois/2) or y>int(h-vois/2) or x<int(vois/2) or x>int(w-vois/2)) :
                imgMediane[y,x] = img[y,x]
            else : 
                imgV = img[int(y-vois/2):int(y+vois/2), int(x-vois/2): int(x+vois/2)]
                t = np.zeros((vois*vois), np.uint8)
                
                for yv in range(imgV.shape[0]):
                    for xv in range(imgV.shape[1]):
                        t[yv*vois+xv] = imgV[yv,xv]
                t.sort()
                imgMediane[y,x]= t[int(vois*vois/2)+1]
            
                # imgMediane[y,x] = np.median(imgV)

    return imgMediane

img_avant = cv2.imread("usthb.jpg",cv2.IMREAD_GRAYSCALE)

img_moyenne = filtreMoy(img_avant)

img_mediane = filtreMediane(img_avant)

cv2.imshow("image_avant",img_avant)
cv2.imshow("image_moyenne", img_moyenne)
cv2.imshow("image_mediane", img_mediane)

cv2.waitKey(0)
cv2.destroyAllWindows