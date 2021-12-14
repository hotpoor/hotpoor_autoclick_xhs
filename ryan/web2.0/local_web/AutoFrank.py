# coded by Ryan， 目前适用于carol。
import os
import time
from PIL import Image
import threading
import json
import shutil

save = 1


# ---select photos---
def select_photos(loop, a):
    x_base = 307
    x_add = 365
    y_base = 420
    y_add = 360
    time.sleep(1)
    loop+=2
    for i in range(0, loop):
        x = x_base + x_add * (i % 3)
        y = y_base + y_add * (int(i / 3))
        os.system("adb %s shell input tap %s %s" % (a, x, y))


# adding photos into phone
def push_photos(loop, pics, a):
    print(str(loop) + ' files detected. ')
    logoPath = (os.path.join(os.path.dirname(__file__) + '/static/poster/'))
    logos = os.listdir(logoPath)
    for o in logos:
        i1 = Image.open(logoPath + o)
        i1.save(logoPath + o)
        os.system('adb %s push ' % a + logoPath + o + ' ' + phone_path)
    for i in pics:
        i1 = Image.open(local_path + i)
        i1.save(local_path + i)
        os.system('adb %s push ' % a + local_path + i + ' ' + phone_path)
        print('file name: ' + i + ' sent to phone')
        time.sleep(1)
    print('all files has been sent... waitting system to respone..')
    os.system(
        'adb %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera' % a)
    time.sleep(2)


# --- put text into title and main text---
def text(a):
    #事先创建一个txt文件，里面放转发链接
    f = open('buy.txt')
    for line in f:
        os.system("adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\'" % (a, line))
    f.close()


def text1(a,i):
    os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    os.system("adb %s shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(1)
    os.system('adb %s shell input tap 130 1098 ' % a)
    time.sleep(0.5)
    # swtich back, enter title
    os.system("adb %s shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(1)
    os.system('adb %s shell input tap 311 634' % a)
    time.sleep(0.5)
    os.system('adb %s shell input swipe 205 416 205 416 800' % a)
    os.system('adb %s shell input tap 102 255' % a)
    time.sleep(0.5)

    # back, copy main text
    os.system("adb %s shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(1)
    os.system('adb %s shell input tap 130 1425' % a)
    # red, main text
    os.system("adb %s shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(1)
    os.system('adb %s shell input swipe 228 796 228 796 800' % a)
    os.system('adb %s shell input tap 116 591' % a)
    # @sb
    os.system('adb %s shell input tap 314 1088' % a)
    time.sleep(1)
    os.system('adb %s shell ime set com.android.adbkeyboard/.AdbIME' % a)
    time.sleep(1)
    with open(os.path.join(os.path.dirname(__file__) + '/static/files/%s%s') % (i, '.json')) as f:
        js = json.load(f)
        name = js['poster_name']
        f.close()
    os.system('adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\' ' % (a, name))
    time.sleep(1)
    os.system('adb %s shell input tap 302 1230' % a)
    time.sleep(1)






def get_short(a):
    os.system('adb %s shell am force-stop com.xingin.xhs' % a)
    time.sleep(1)
    os.system("adb %s shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(8)
    # os.system('adb %s shell input tap 400 1000' % a)
    # time.sleep(0.7)
    # os.system('adb %s shell input text "http://192.168.0.104:8000/demo/article"' % a)
    # http://10.20.30.7:8000/demo/article
    # time.sleep(1)
    # os.system('adb %s shell input tap 945 156' % a)
    os.system('adb %s shell input tap 970 150' % a)
    time.sleep(0.5)
    os.system('adb %s shell input swipe 235 711 235 711 800' % a)
    time.sleep(1)
    os.system('adb %s shell input tap 148 564' % a)
    time.sleep(0.5)
    os.system('adb %s shell input tap 250 808' % a)
    time.sleep(10)


def sentReview(a):
    #切换输入法
    os.system('adb %s shell ime set com.android.adbkeyboard/.AdbIME' % a)
    time.sleep(1)
    #点入第一篇文章
    os.system('adb %s shell input tap 800 1300' % a)
    #点击评论
    os.system('adb %s shell input tap 976 2135' % a)
    time.sleep(2)
    text(a)
    time.sleep(0.5)
    #点击发送
    os.system('adb %s shell input tap 1000 1950' % a)
    #切换回正常输入法
    os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    time.sleep(0.5)
    #左上角返回
    os.system('adb %s shell input tap 50 160' % a)


def frank():
    global ip
    global eventLock
    global fdone
    print('frank is waitting the light')
    eventLock.wait()
    print('light is green, frank is on go')
    a = '-s a022d1760821'
    if ip == 0:
        i = shorts[ip][:-5]
        print('frank current ip is : %s' % ip)
        ip += 1
    else:
        i = shorts[ip][:-5]
        print('frank current ip is : %s' % ip)
        ip += 1

    eventLock.set()
    print('frank showing green now')
    print('jason file for frank is : %s' % i)
    os.system("adb %s shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(3)
    os.system('adb %s shell input tap 970 150' % a)
    time.sleep(1)
    # click input box (json)
    os.system('adb %s shell input tap 370 374' % a)
    time.sleep(1)
    os.system('adb %s shell input text "%s"' % (a, i))
    time.sleep(1)
    os.system('adb %s shell input tap 263 475' % a)
    time.sleep(5)

    # ---open red
    os.system("adb %s shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1" % a)

    # sort file names (place photos with correct pattern)
    pics = []
    for pic in os.listdir(local_path):
        if pic[:-6] in i:
            pics.append(pic)

    pics.sort(reverse=True)
    loop = len(pics)
    if loop == 9:
        pics=pics[:-2]

    # --- push photos
    push_photos(loop, pics, a)
    # press new button
    os.system('adb %s shell input tap 544 2150' % a)

    # add new thread
    os.system('adb %s shell input tap 540 2150' % a)
    time.sleep(1)

    # -----adding photo
    select_photos(loop, a)

    # next
    os.system('adb %s shell input tap 935 2150' % a)
    time.sleep(0.5)

    # next again
    os.system('adb %s shell input tap 990 170' % a)
    time.sleep(0.5)

    # ---main--- put text in thread boxes
    # os.system('adb %s shell ime set com.android.adbkeyboard/.AdbIME' % a)
    # text()
    # os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    text1(a,i)
    # done & send
    time.sleep(1)
    os.system('adb %s shell input tap 580 2111' % a)
    os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    
    # click done
    time.sleep(10)
    os.system('adb %s shell input tap 540 2135' % a)
    # to 'mine'
    os.system('adb %s shell input tap 976 2153' % a)
    time.sleep(0.5)
    farm = True
    farmCount = 0
    #sentReview(a)
    while farm:
        time.sleep(0.5)
        os.system("adb -s a022d1760821 shell input tap 800 1300")
        time.sleep(0.3)
        os.system("adb -s a022d1760821 shell input swipe 900 900 300 900 130")
        os.system("adb -s a022d1760821 shell input swipe 900 900 300 900 130")
        os.system("adb -s a022d1760821 shell input swipe 900 900 300 900 130")
        time.sleep(0.3)
        os.system("adb -s a022d1760821 shell input tap 759 2280")

        farmCount += 1
        print('loop count: %s' % farmCount)
        if farmCount == 500:
            farm = False
            os.system('adb %s shell am force-stop com.xingin.xhs' % a)
            time.sleep(1)
            fdone=1


def carol():
    global cdone
    global eventLock
    cdone = 0
    print('carol is waitting the light')
    eventLock.wait()
    global ip
    print('light is green, carol is on go')
    a = '-s 927aaf0d0421'
    if ip == 0:
        i = shorts[ip][:-5]
        print('Carol current ip is : %s' % ip)
        ip += 1
    else:
        i = shorts[ip][:-5]
        print('Carol current ip is : %s' % ip)
        ip += 1

    eventLock.set()
    print('carol showing green now')
    print('jason file for carol is : %s' % i)
    os.system("adb %s shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(3)
    os.system('adb %s shell input tap 970 150' % a)
    time.sleep(1)
    # click input box (json)
    os.system('adb %s shell input tap 370 374' % a)
    time.sleep(1)
    os.system('adb %s shell input text "%s"' % (a, i))
    time.sleep(1)
    os.system('adb %s shell input tap 263 475' % a)
    time.sleep(5)

    # ---open red
    os.system("adb %s shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1" % a)

    # sort file names (place photos with correct pattern)
    pics = []
    for pic in os.listdir(local_path):
        print(os.listdir(local_path))
        print('shorts')
        print(pic)
        print('a pic')
        if pic[:-6] in i:
            print('true,append')
            pics.append(pic)
    pics.sort(reverse=True)
    loop = len(pics)
    if loop == 9:
        pics = pics[:-2]

    # --- push photos
    push_photos(loop, pics, a)

    # press new button
    os.system('adb %s shell input tap 544 2150' % a)

    # add new thread
    os.system('adb %s shell input tap 540 2150' % a)
    time.sleep(1)

    # -----adding photo
    select_photos(loop, a)

    # next
    os.system('adb %s shell input tap 935 2150' % a)
    time.sleep(0.5)

    # next again
    os.system('adb %s shell input tap 990 170' % a)
    time.sleep(0.5)

    # ---main--- put text in thread boxes
    # os.system('adb %s shell ime set com.android.adbkeyboard/.AdbIME' % a)
    # text()
    # os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    text1(a,i)
    # done & send
    time.sleep(1)
    os.system('adb %s shell input tap 580 2111' % a)
    os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    
    # click done
    time.sleep(10)
    os.system('adb %s shell input tap 540 2135' % a)
    # to 'mine'
    os.system('adb %s shell input tap 976 2153' % a)
    time.sleep(0.5)
    farm = True
    farmCount = 0
    #sentReview(a)
    while farm:
        time.sleep(0.5)
        os.system("adb -s 927aaf0d0421 shell input tap 800 1300")
        time.sleep(0.3)
        os.system("adb -s 927aaf0d0421 shell input swipe 900 900 300 900 130")
        os.system("adb -s 927aaf0d0421 shell input swipe 900 900 300 900 130")
        os.system("adb -s 927aaf0d0421 shell input swipe 900 900 300 900 130")
        time.sleep(0.3)
        os.system("adb -s 927aaf0d0421 shell input tap 759 2280")

        farmCount += 1
        print('loop count: %s' % farmCount)
        if farmCount == 500:
            farm = False
            cdone = 1
            os.system('adb %s shell am force-stop com.xingin.xhs' % a)
            time.sleep(1)


local_path = os.path.join(os.path.dirname(__file__), r'static/upload/')

# delete DS file for MAC users
if os.path.isfile(local_path + '.DS_store'):
    print('DS file detected.')
    os.remove(local_path + '.Ds_store')
    print('Ds file deleted!')

phone_path = r'/sdcard/DCIM/Camera'
loop_count = 0

# --- get short link
# get_short()

shorts_path = os.path.join(os.path.dirname(__file__), r'static/files/')

if os.path.isfile(shorts_path + '.DS_store'):
    print('DS file in shorts detected.')
    os.remove(shorts_path + '.Ds_store')
    print('Ds file in shorts deleted!')

shorts = os.listdir(os.path.join(os.path.dirname(__file__), r'static/files/'))
ip = 0
fdone = 1
cdone = 1
if __name__ == '__main__':

    while ip < len(shorts) and fdone and cdone:
        subThread01 = threading.Thread(target=frank)
        subThread02 = threading.Thread(target=carol)
        eventLock = threading.Event()
        print('current ip: %s' % ip)
        subThread01.start()
        print('starting frank...')
        eventLock.set()
        subThread02.start()
        print('starting carol...')

        subThread01.join()
        subThread02.join()
