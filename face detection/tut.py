import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("D:/project/face detection/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

#id=raw_input('enter user id')
#sampleNum=0;

while True:
    ret,img = cap.read();

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4);

    for(x, y, w, h) in faces:
        #sampleNum=sampleNum+1;
        #cv2.imwrite("dataSet/user."+str(id)+"."+ (sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.waitKey(100);

    cv2.imshow('Face',img);
    k=cv2.waitKey(30) & 0xff;
    

   
    if(k==27):
        break
cap.release()
cv2.destroyAllWindows()
