import cv2
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

img = cv2.imread('/Users/ryan/Desktop/WechatIMG9.jpeg')
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
    myPoints = np.array(lipPoints)
    bbox = cv2.boundingRect(myPoints)
    x, y, w, h = bbox
    imgCrop = masked_image[y:y + h, x:x + w]
    #imgCrop = cv2.GaussianBlur(imgCrop, (7, 7), 20)
    # --- crop a box on lower lip
    box = img[y1:y2, x1:x2]
    cv2.imshow('mask2', box)
    # --- end
    # -- find most common color
    box = cv2.cvtColor(box, cv2.COLOR_BGR2RGB)
    unique, counts = np.unique(box.reshape(-1, 3), axis=0, return_counts=True)
    box[:, :, 0], box[:, :, 1], box[:, :, 2] = unique[np.argmax(counts)]
    mostCommon = unique[np.argmax(counts)]
    print('the most common color on lower lip is :' + str(mostCommon))
    # show_img_compar(img, img_temp)
    # -- end
    cv2.imwrite('/Users/ryan/Desktop/2.jpeg',imgCrop)
    cv2.imshow('hi',img)
    cv2.waitKey(0)

