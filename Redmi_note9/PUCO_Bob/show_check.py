from PIL import Image, ImageGrab
import mss
import mss.tools
import time
import cv2 as cv
import pyautogui


import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib
from setting import android_x0
from setting import android_y0
from setting import android_x1
from setting import android_y1

model = tf.keras.models.load_model('models/my_model')
batch_size = 32
img_width = android_x1 - android_x0
img_height = android_y1 - android_y0

def get_android_img():
    starttime = time.time()
    with mss.mss() as sct:
        region = {
            "top":android_y0,
            "left":android_x0,
            "width":android_x1 - android_x0,
            "height":android_y1 - android_y0,
        }
        img = sct.grab(region)

        path_temp = "./hotpoor_autoclick_cache/record_temp.png"
        mss.tools.to_png(img.rgb,img.size,output=path_temp)
        endtime = time.time()
    return path_temp
def get_check_result(img_now):
    path_temp = "./hotpoor_autoclick_cache/record_temp.png"
    sunflower_path = pathlib.Path(path_temp)

    img = keras.preprocessing.image.load_img(
        sunflower_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    class_names=['home', 'list', 'news', 'search','shop', 'video']
    k = "None"
    if 100 * np.max(score)>=90:
        k = class_names[np.argmax(score)]
        print("当前页面为:",class_names[np.argmax(score)],100 * np.max(score))
    result = k
    actions = ["news","video","shop","list"]
    if result not in actions:
        result = "no action"
    return result
is_debug = True
is_doing = False
is_left = True
action_now = "None"
while True:
    if is_debug:
        base_img = cv.imread(get_android_img(),0)
        action_now = get_check_result(base_img)
        print(action_now)
        cv.imshow("img",base_img)
        key = cv.waitKey(1)
        if key == ord("q"):
            break
    else:
        if not is_doing:
            base_img = cv.imread(get_android_img(),0)
            action_now = get_check_result(base_img)
            if action_now in ["news","video","shop","list"]:
                is_doing = True
            cv.imshow("img",base_img)
            key = cv.waitKey(1)
            if key == ord("q"):
                break
        else:
            if action_now in ["list"]:
                pass


cv.destroyAllWindows()
