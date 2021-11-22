import cv2
import numpy as np


img = cv2.imread('/Users/ryan/Desktop/2.jpeg')
# create average color mask
mask = np.zeros((100,100,3),dtype=np.uint8)
mask[:] = (83,90,213)
# create puco color mask
puco = np.zeros((100,100,3),dtype=np.uint8)
puco[:] = (20,20,138)
# to HSV
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
puco = cv2.cvtColor(puco, cv2.COLOR_BGR2HSV)
# substract values
a1,a2,a3 = puco[1][1]
b1,b2,b3 = mask[1][1]
print(a1,a2,a3)
print(b1,b2,b3)
h= int(a1)-int(b1)
s = int(a2)/int(b2)
v = int(a3)/int(b3)
print(h,s,v)
# aply colors
img1 = img.copy()
for x in img1:
    for y in x:
        if y[1]*s <=255:
            y[1] *= s
        y[2] *= v


img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
img1 = cv2.cvtColor(img1, cv2.COLOR_HSV2BGR)

cv2.imshow('ori',img)
cv2.imshow('aft',img1)

puco = cv2.cvtColor(puco, cv2.COLOR_HSV2BGR)
cv2.imshow('2',mask)
cv2.imshow('3',puco)
cv2.waitKey(0)