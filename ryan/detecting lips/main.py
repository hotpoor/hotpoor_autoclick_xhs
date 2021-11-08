import cv2 as cv
import numpy as np
import copy

mouth_cascade = cv.CascadeClassifier('/Users/ryan/PycharmProjects/detect_mouth/venv/mouth2.xml')
#recognizer = cv.face.LBPHFaceRecognizer_create()
a = 1
#capture = cv.VideoCapture(0)
while a:
    #ret, frame = capture.read()
    #img = frame
    img = cv.imread(r'/Users/ryan/Desktop/2.jpeg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.2, 40)
    for (x,y,w,h) in mouth_rects:
        # print(mouth_rects)

        cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        #img_crop = img[y+4:y+h-10,x+5:x+w-5]
        img_crop = img[y+2:y+h-2,x+2:x+w-2]
        # 复制嘴图
        img_temp1 = img_crop.copy()
        img_temp = img_crop.copy()

        gray1 = cv.cvtColor(img_temp, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray1,(5,5),0)
        (T,thresh) = cv.threshold(blurred,155,255,cv.THRESH_BINARY)
        img_temp2 = copy.deepcopy(thresh)


        #orinal pic
        unique1, counts1 = np.unique(img_temp1.reshape(-1, 3), axis=0, return_counts=True)
        img_temp1[:, :, 0], img_temp1[:, :, 1], img_temp1[:, :, 2] = unique1[np.argmax(counts1)]

        #threshfy pic
        unique, counts = np.unique(img_temp2.reshape(-1, 2), axis=0, return_counts=True)

        img_temp2[:, 0], img_temp2[:, 1] = unique[np.argmax(counts)]

        print('unqiue color:')
        print(unique)
        print(counts)
        cv.imshow('most common color', img_temp2)
        # print('no1')
        #
        # print(img_temp1[:, :, 0])
        # print('no2')
        # print(img_temp1[:, :, 1])
        #print(str((img_temp[:, :, 0])[0])[0])

        #print(str(((img_temp[:, :, 0])[0])[0]))
        # print('done')





    # cv.imshow('gray1', gray1)
    # cv.imshow('bl',blurred)
    cv.imshow('th',thresh)
    cv.imshow('most common color 2',img_temp1)
    cv.waitKey(1)