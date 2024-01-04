#AI Based Attendance System project and marking it to a real time database using csv file.
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path='/Users/prayashdas/Downloads/Attendance2' # the list contains the images to be trained with
images=[]
classnames=[]
mylist=os.listdir(path)
#print(mylist)
for cls in mylist:
    if cls.endswith(('.jpg','.jpeg','.png')): #will accept only jpg,jpeg or png format images
        curimg=cv2.imread(f'{path}/{cls}')
        if curimg is not None:
            images.append(curimg)
            classnames.append(os.path.splitext(cls)[0])
#print(classnames)

def findencodings(images): #defining a function for finding the encodings of the images
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def Attendance(name):
    with open('Attendance.csv','r+') as f:
        mydata=f.readlines()
        nameList=[]
        for line in mydata:
            entry=line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')





encodelistknown=findencodings(images)
print('Encoding Complete') #once encoding is completed successfully

capture=cv2.VideoCapture(0) #initiate the camera of your local machine

while True:
    success,img=capture.read()
    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    facecurframe=face_recognition.face_locations(imgs)
    encodecurframe=face_recognition.face_encodings(imgs,facecurframe)

    for encodeFace,faceLock in zip(encodecurframe,facecurframe):
        matches=face_recognition.compare_faces(encodelistknown,encodeFace)
        facedistance=face_recognition.face_distance(encodelistknown,encodeFace)
        #print(facedistance)
        matchIndex=np.argmin(facedistance)

        if matches[matchIndex]:
            name=classnames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1=faceLock
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4 #create a rectangular box around to detect your face.
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            Attendance(name)


    cv2.imshow('Webcam',img)
    cv2.waitKey(1)

