import cv2
import numpy as np
import matplotlib.pyplot as plt

img_avant = cv2.imread("ferrari.jpg",cv2.IMREAD_GRAYSCALE)

img_avant[:] = img_avant[:]/2 
cv2.imwrite('usthb_max.jpg', img_avant)

if img_avant is None :
    print("Erreur de chargement")
    exit(0)
h,w = img_avant.shape
min, max = 255,0
for y in range (h) :
    for x in  range(w) :
        if img_avant[y,x] > max :
            max = img_avant[y,x]
        if img_avant[y,x] < min:
            min = img_avant[y,x]

print("Min :", min, " Max :", max)


img_apres = np.zeros(img_avant.shape, img_avant.dtype)

for y in range(h):
    for x in range(w):
        img_apres[y,x]=(img_avant[y,x]-min)*255/(max-min)

#HISTOGRAMME

his_avant=np.zeros((256,1), np.uint16)
for y in range(h) :
    for x in range(w):
        his_avant[img_avant[y,x]]+=1

his_apres= cv2.calcHist([img_apres],[0],None,[256],[0,255])

plt.figure()
plt.title("Image normalisee")
plt.xlabel("NG")
plt.ylabel("Nombre de pixels")
plt.plot(his_avant)
plt.plot(his_apres)
plt.xlim([0,255])
plt.show()

cv2.imshow("Image avant", img_avant)
cv2.imshow("Image apres", img_apres)
cv2.waitKey(0)
cv2.destroyAllWindows()