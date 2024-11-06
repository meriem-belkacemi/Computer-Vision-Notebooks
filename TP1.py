import cv2
import numpy as np

img2 = cv2.imread("Meriem.jpeg",cv2.IMREAD_GRAYSCALE)
img = np.zeros((500,500),np.uint8)

# img[:] = 255
# Afficher le contenu du bit 100,100
print(img[100,100])
img[100:300,100:200]=255



#cv2.imshow("Image2",img2)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
