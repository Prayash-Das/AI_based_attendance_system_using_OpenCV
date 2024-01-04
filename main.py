#Source Code for comparing two images and calculating the similarities/dissimilarities.
#importing libraries
import cv2
import numpy as np
import face_recognition

img=face_recognition.load_image_file('/Users/prayashdas/Downloads/Attendance2/Elon.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #loading image and test image
imgtest=face_recognition.load_image_file('/Users/prayashdas/Downloads/Attendance2/Sachin.jpg')
imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceLock=face_recognition.face_locations(img)[0]
encode=face_recognition.face_encodings(img)[0] #finding the encodings of the image
cv2.rectangle(img,(faceLock[3],faceLock[0]),(faceLock[1],faceLock[2]),(255,0,255),2)

faceLocktest=face_recognition.face_locations(imgtest)[0]
encodetest=face_recognition.face_encodings(imgtest)[0] #finding the encodings of the test image
cv2.rectangle(imgtest,(faceLocktest[3],faceLocktest[0]),(faceLocktest[1],faceLocktest[2]),(255,0,255),2)

results=face_recognition.compare_faces([encode],encodetest) #comparison of 2 images
facedistance=face_recognition.face_distance([encode],encodetest)
print(results,facedistance)
cv2.putText(imgtest,f'{results} {round(facedistance[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Image',img)
cv2.imshow('Test',imgtest)
cv2.waitKey(0)