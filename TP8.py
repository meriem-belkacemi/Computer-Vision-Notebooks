import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 2, (frame_width, frame_height))

if not cap.isOpened():
    print("erreur")
    exit(0)

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret :
        print("erreur cap.read")
        break
    out.write(frame)
    cv2.imshow("frame", frame)
    
    if(cv2.waitKey(200) & 0xFF == ord('q')) :
        break
    
cap.release()    
cv2.destroyAllWindows()
    