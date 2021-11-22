import cv2
import numpy as np
import dlib

webcam = 1
cap = cv2.VideoCapture(0)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def creatBox(img,points,scale =5,masked = False, cropped = True):
    if masked:
        mask = np.zeros_like(img)
        mask = cv2.fillPoly(mask,[points],(255,255,255))
        img = cv2.bitwise_and(img,mask)


    if cropped:
        bbox = cv2.boundingRect(points)
        x,y,w,h = bbox
        imgCrop = img[y:y+h,x:x+w]
        imgCrop = cv2.resize(imgCrop,(0,0),None,scale,scale)
        return imgCrop

    else:
        return mask

while True:

    if webcam: success , img = cap.read()
    else: img = cv2.imread('2 copy.jpeg')
    #img = cv2.resize(img,(0,0),None,0.5,0.5)
    #imOriginal = img.copy()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector(imgGray)


    for face in faces:
        x1,y1 = face.left(),face.top()
        x2,y2 = face.right(),face.bottom()
        #imgOriginal = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        landmarks = predictor(imgGray,face)
        myPoints = []

        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            myPoints.append([x,y])

        myPoints = np.array(myPoints)
        imgLips = creatBox(img,myPoints[48:61],3,masked=True,cropped=False)
        img1 = img.copy()
        imgColorLips = cv2.fillPoly(img1, [myPoints[48:61]],(23,23,200))
        imgColorLips = cv2.addWeighted(img, 0.5, imgColorLips, 0.3, 0.5)
        cv2.putText(imgColorLips, 'hello', (0, 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 0, 255), 5)
        cv2.imshow('main',imgColorLips)
    cv2.waitKey(1)


