import cv2
import numpy as np
import dlib

webcam = 0
# cap = cv2.VideoCapture(0)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def creatBox(img,points,scale =5,masked = False, cropped = True):
    if masked:
        mask = np.zeros_like(img)
        mask = cv2.fillPoly(mask,[points],(255,255,255))
        img = cv2.bitwise_and(img,mask)
        cv2.imshow('mask', img)
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
            #cv2.circle(imgOriginal,(x,y),3,(50,50,255),cv2.FILLED)
            #cv2.putText(imgOriginal,str(n),(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(0,0,255),1)
            myPoints.append([x,y])

        myPoints = np.array(myPoints)
        #imgLeftEye = creatBox(img,myPoints[36:42])
        imgLips = creatBox(img,myPoints[48:61],3,masked=True,cropped=False)

        #imgLipsOringinal = creatBox(img,myPoints[48:61])

        imgColorLips = np.zeros_like(imgLips)
        imgColorLips[:] = 41,33,113 #(BGR)
        cv2.imshow('only lip', imgColorLips)
        imgColorLips = cv2.bitwise_and(imgLips,imgColorLips)
        #修改模糊度，最后一个数值不知道啥意思
        imgColorLips = cv2.GaussianBlur(imgColorLips,(5,5),5)
        cv2.imshow('only lip2', imgColorLips)
        #叠加权重，改数值实现亮度和暗度（个人理解）
        imgColorLips = cv2.addWeighted(img,1,imgColorLips,-0.25,0)
        cv2.imshow('Lips new', imgColorLips)

        # cv2.imshow('only lip',imgColorLips)
        #cv2.imshow('Lips',imgLips)
        print(myPoints)
    cv2.imshow('orinal', img)
    cv2.waitKey(1)


