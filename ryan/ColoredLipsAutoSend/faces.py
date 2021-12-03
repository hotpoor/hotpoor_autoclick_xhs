import cv2
import dlib
import time
import glob
import numpy as np
from cv2 import imread, imwrite
from fourfaces import x4faces
from twofaces import x2faces

def x3faces(num):
    imgs, heights, widths = [], [], []
    # read imgs
    for f in glob.glob("pics/afterWork/*.jpg"):
        if 'MM0' in f:
            img = imread(f, -1)  # 参数-1表示返回原图
            h, w = img.shape[:2]  # 切片
            heights.append(h)
            widths.append(w)
            imgs.append(img)
    # set minimum heights and weights
    min_height = min(heights)
    min_width = min(widths)
    # resize imgs
    for i, x in enumerate(imgs):
        # i为每个图像的序号, x为每个图像的多维像素矩阵
        imgs[i] = x[:min_height:4, :min_width:4]  # 切片 以步长为3
    # concatenation
    img0 = np.concatenate(imgs[:3], 1)  # 横着拼三个
    img1 = np.concatenate(imgs[3:6], 1)  # 横着拼三个
    img2 = np.concatenate(imgs[6:9], 1)  # 横着拼三个
    # resize logo
    imgLogo = imread('/Users/ryan/PycharmProjects/detect_mouth/venv/pics/logo/Puco.jpeg',cv2.IMREAD_UNCHANGED)
    h, w = img0.shape[:2]
    dim = (w, int(h/2))
    imgLogo = cv2.resize(imgLogo, dim, interpolation = cv2.INTER_AREA)
    img9 = np.concatenate([img0, img1, img2,imgLogo], 0)# 竖着拼起来
    #resize final pic
    print(min_width,min_height)
    h,w = img9.shape[:2]
    if int(h * 0.75) != w:
        print('not 4:3')
        x = int(h * 0.75) - w
        img9 = cv2.copyMakeBorder(img9, 0, 0, int(x / 2), int(x / 2), cv2.BORDER_CONSTANT, value=(0, 0, 0))
    #img9 = cv2.resize(img9,(1080,1439), interpolation = cv2.INTER_AREA)
    imwrite("pics/final/3x3%s.jpg"% num, img9)
    x2faces(num)
    x4faces(num)

    #cv2.imshow('9',img9)


