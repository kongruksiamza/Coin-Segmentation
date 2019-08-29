import cv2
import numpy as np
cap=cv2.VideoCapture("Coin2.mp4")

while(cap.read()) :
     ref,frame = cap.read()
     roi=frame[:1080,0:1920]

     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     gray_blur=cv2.GaussianBlur(gray,(15,15),0)
     thresh=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
     kernel=np.ones((3,3),np.uint8)
     closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=4)

     result_img=closing.copy()
     contours,hierachy=cv2.findContours(result_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
     counter=0
     for cnt in contours:
         area = cv2.contourArea(cnt)
         if area<5000 or area > 35000:
             continue
         ellipse = cv2.fitEllipse(cnt)
         cv2.ellipse(roi,ellipse,(0,255,0),2)
         counter+=1
    
     cv2.putText(roi,str(counter),(10,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),2,cv2.LINE_AA)
     cv2.imshow("Show",roi)

     if cv2.waitKey(1) & 0xFF==ord('q'):
         break

cap.release()
cv2.destroyAllWindows()