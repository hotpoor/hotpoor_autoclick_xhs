import cv2
import numpy as np
import dlib

webcam = 1
cap = cv2.VideoCapture(0)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def empty(a):
    pass


cv2.namedWindow('BGR')
cv2.resizeWindow('BGR',640,240)
cv2.createTrackbar('Blue','BGR',0,255,empty)
cv2.createTrackbar('Green','BGR',0,255,empty)
cv2.createTrackbar('Red','BGR',0,255,empty)


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
            #cv2.circle(imgOriginal,(x,y),3,(50,50,255),cv2.FILLED)
            #cv2.putText(imgOriginal,str(n),(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(0,0,255),1)
            myPoints.append([x,y])

        myPoints = np.array(myPoints)
        #imgLeftEye = creatBox(img,myPoints[36:42])
        imgLips = creatBox(img,myPoints[48:61],3,masked=False,cropped=True)
        #cv2.imshow('mask',imgLips)

        #imgLipsOringinal = creatBox(img,myPoints[48:61])

        imgColorLips = np.zeros_like(imgLips)



        #cv2.imshow('red',imgColorLips)


        imgLips1 = cv2.cvtColor(imgLips,cv2.COLOR_BGR2GRAY)
        # # threshhold
        # (thresh, thimg) = cv2.threshold(imgLips1, 60, 255, cv2.THRESH_BINARY)
        # imgLips1 = cv2.cvtColor(thimg, cv2.COLOR_GRAY2BGR)

        imgLips1 = cv2.cvtColor(imgLips1, cv2.COLOR_GRAY2BGR)
        imgColorLips = cv2.bitwise_and(imgLips1, imgColorLips)
        cv2.imshow('a',imgColorLips)

        # b = cv2.getTrackbarPos('Blue', 'BGR')
        # print(b)
        # g = cv2.getTrackbarPos('Green', 'BGR')
        # print(g)
        # r = cv2.getTrackbarPos('Red', 'BGR')
        # print(r)
        # imgColorLips[:] = b, g, r  # (BGR)
        #
        #
        #
        # # imgColorLips = cv2.bitwise_and(imgLips,imgColorLips)
        # #cv2.imshow('only lip', imgColorLips)
        # #修改模糊度
        # imgColorLips = cv2.GaussianBlur(imgColorLips,(7,7),10)



        #cv2.imshow('0',imgColorLips)

        # # ---
        # img1 = img.copy()
        #
        #
        #
        # imgColorLips = cv2.fillPoly(img1, [myPoints[48:61]],(b,g,r))
        # # 41,33,113   58,54,167  #206,106,114  138,21,22, 26,26,144，
        # # cv2.imshow('cut', imgColorLips)
        # imgColorLips = cv2.GaussianBlur(imgColorLips, (5, 5), 7)
        #
        #
        # imgColorLips = cv2.addWeighted(img, 0.7, imgColorLips, 0.3, 1)
        #
        # cv2.putText(imgColorLips, str(b), (10, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 0, 0), 2)
        # cv2.putText(imgColorLips, str(g), (55, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2)
        # cv2.putText(imgColorLips, str(r), (100, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        #
        #
        # cv2.imshow('BGR',imgColorLips)

        #cv2.imshow('oringanl',img)

        #------end




        #叠加权重
        # imgColorLips = cv2.addWeighted(img,1,imgColorLips,-0.5,1)
        # # cv2.putText(imgColorLips, 'MM05',(0,150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 0, 255), 5)
        # cv2.imshow('Lips new', imgColorLips)

        # cv2.imshow('only lip',imgColorLips)
        #cv2.imshow('Lips',imgLips)

    #cv2.imshow('orinal', img)
    cv2.waitKey(1)


