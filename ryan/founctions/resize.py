import os
import time
import cv2


local_path = '/Users/ryan/Desktop/red/local_web/static/upload/'
pics = os.listdir(local_path)

for i in pics:
    i1 = local_path + i
    img = cv2.imread(i1, cv2.IMREAD_UNCHANGED)
    width = 600
    height = 800
    dim = (width, height)
    print('resizing the img... file name: %s'% i)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(i1, resized)
    print('resize suceed!')






