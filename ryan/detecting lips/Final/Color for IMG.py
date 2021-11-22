import cv2
import numpy as np
import dlib
import time
from PIL import Image
import cvzone

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


#webcam = 1
#cap = cv2.VideoCapture(0)

while True:
    #ret, img = cap.read()
    #img = cv2.resize(img,(640,360))
    img = cv2.imread('/Users/ryan/Desktop/WechatIMG9.jpeg')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector(imgGray)

    if len(faces) > 0:
        face = faces[0]

    #for face[0] in faces:
        x1,y1 = face.left(),face.top()
        x2,y2 = face.right(),face.bottom()
        #imgOriginal = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        landmarks = predictor(imgGray,face)
        myPoints = []

        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            # # add text on roi
            #cv2.circle(img,(x,y),3,(50,50,255),cv2.FILLED)
            #cv2.putText(img,str(n),(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(0,0,255),1)
            myPoints.append([x,y])
        # -- set ROI
        y1 = myPoints[60][1]
        y2 = myPoints[57][1]
        x1 = myPoints[58][0]
        x2 = myPoints[56][0]
        # --- crop lip
        lipPoints = myPoints[48:61]
        mask = np.zeros(img.shape, dtype=np.uint8)
        roi_corners = np.array([lipPoints], dtype=np.int32)
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
        cv2.fillPoly(mask, roi_corners, ignore_mask_color)
        # # from Masterfool: use cv2.fillConvexPoly if you know it's convex
        masked_image = cv2.bitwise_and(img, mask)
        # ---end
        # ---crop lip
        myPoints1 = np.array(lipPoints)
        bbox = cv2.boundingRect(myPoints1)
        x, y, w, h = bbox
        imgCrop = masked_image[y:y + h, x:x + w]
        # --- crop a box on lower lip
        box = img[y1:y2, x1:x2]
        # --- end
        # -- find most common color
        box = cv2.cvtColor(box, cv2.COLOR_BGR2RGB)
        unique, counts = np.unique(box.reshape(-1, 3), axis=0, return_counts=True)
        box[:, :, 0], box[:, :, 1], box[:, :, 2] = unique[np.argmax(counts)]
        mostCommon = unique[np.argmax(counts)]
        print('the most common color on lower lip is :' + str(mostCommon))
        box = cv2.cvtColor(box, cv2.COLOR_RGB2BGR)
        # show_img_compar(img, img_temp)
        # -- end

        # ---create average color mask
        mask = np.zeros((100, 100, 3), dtype=np.uint8)
        mask[:] = (mostCommon[2], mostCommon[1], mostCommon[0])
        # create puco color mask
        puco = np.zeros((100, 100, 3), dtype=np.uint8)
        puco[:] = (20, 20, 138)
        # to HSV
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
        imgCrop = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2HSV)
        puco = cv2.cvtColor(puco, cv2.COLOR_BGR2HSV)
        # substract values
        a1, a2, a3 = puco[1][1]
        b1, b2, b3 = mask[1][1]
        print(a1, a2, a3)
        print(b1, b2, b3)
        h = int(a1) - int(b1)
        s = int(a2) / int(b2)
        v = int(a3) / int(b3)
        print(h, s, v)
        #aply colors

        for x in imgCrop:
            for y in x:
                if y[1] ==0 and y[2]==0 and y[0]==0:
                    continue
                else:
                    if y[1] * s <= 255:
                        y[1] *= s
                    else:
                        y[1] = 255 - ((y[1] * s) - 255)
                    y[2] *= v
                    # lets fucking go baby!!!!!!!!!!!!!
        imgCrop = cv2.cvtColor(imgCrop, cv2.COLOR_HSV2BGR)
        #concatenation 1
        imgl = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2BGRA)
        cv2.imwrite('/Users/ryan/Desktop/3.png', imgl)

        # delete black background
        img1 = Image.open('/Users/ryan/Desktop/3.png')

        img1 = img1.convert("RGBA")
        datas = img1.getdata()
        newData = []
        for item in datas:
            if item[0] <= 55 and item[1] <= 55 and item[2] <= 55:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img1.putdata(newData)
        img1.save("/Users/ryan/Desktop/4.png", "PNG")

        imgl = cv2.imread('/Users/ryan/Desktop/4.png', cv2.IMREAD_UNCHANGED)

        imgResult = cvzone.overlayPNG(img, imgl, [bbox[0], bbox[1]])
        cv2.imshow('final',imgResult)


    cv2.imshow('hi',img)
    cv2.waitKey(1)

# concatenation (failed)
# maskImg = np.zeros_like(img)
# maskImg = cv2.fillPoly(maskImg,[myPoints1],(255,255,255))
# maskImg = cv2.bitwise_not(maskImg)
# after = cv2.bitwise_and(maskImg,img)
# after = cv2.bitwise_or(after,masked_image)

