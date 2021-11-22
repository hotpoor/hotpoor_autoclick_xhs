# coded by Ryan， 目前适用于carol。
import os
import time
from PIL import Image
import shutil

save = 1


# ---select photos---
def select_photos():
    x_base = 307
    x_add = 365
    y_base = 420
    y_add = 360

    for i in range(0, loop):
        x = x_base + x_add * (i % 3)
        y = y_base + y_add * (int(i / 3))
        os.system("adb %s shell input tap %s %s" % (a, x, y))


# adding photos into phone
def push_photos():
    print(str(loop) + ' files detected. ')

    for i in pics:
        i1 = Image.open(local_path + i)
        i1.save(local_path + i)
        os.system('adb %s push ' % a + local_path + i + ' ' + phone_path)
        print('file name: ' + i + ' sent to phone')
        time.sleep(1)
    print('all files has been sent... waitting system to respone..')
    os.system(
        'adb %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera' % a)
    time.sleep(3)


# --- put text into title and main text---
def text():
    f = open('文案（标题前标注T）.txt')
    check = 0
    for line in f:
        if check == 0 and line[0] == 'T':
            os.system('adb %s shell input tap 311 634' % a)
            os.system("adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\'" % (a, line.replace(' ', '\ ')[1:]))
            check += 1
            os.system('adb %s shell input tap 330 824' % a)
        else:
            os.system('adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\' ' % (a, line.replace(' ', '\ ')))
            os.system('adb %s shell am broadcast -a ADB_INPUT_CODE --ei code 66' % a)
    f.close()


def text1():
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


def get_short():
    # os.system("adb %s shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1" % a)
    # time.sleep(8)
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


local_path = os.path.join(os.path.dirname(__file__), 'static/upload/')

# delete DS file for MAC users
if os.path.isfile(local_path + '.DS_store'):
    print('DS file detected.')
    os.remove(local_path + '.Ds_store')
    print('Ds file deleted!')

a = '-s a022d1760821'

phone_path = '/sdcard/DCIM/Camera'
loop_count = 0

# --- get short link
# get_short()

shorts_path = os.path.join(os.path.dirname(__file__), 'static/files/')

print('wut')
if os.path.isfile(shorts_path + '.DS_store'):
    print('DS file in shorts detected.')
    os.remove(shorts_path + '.Ds_store')
    print('Ds file in shorts deleted!')

shorts = os.listdir(os.path.join(os.path.dirname(__file__), 'static/files/'))

for i in shorts:
    i = i[:-5]
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
    for i in shorts:
        i = i[:-5]
        pics = []
        for p in os.listdir(local_path):
            if p[:-6] in i:
                pics.append(p)

    pics.sort(reverse=True)
    loop = len(pics)

    # press new button
    os.system('adb %s shell input tap 544 1849' % a)
    # --- push photos
    push_photos()

    # add new thread
    os.system('adb %s shell input tap 540 2150' % a)
    time.sleep(1)

    # -----adding photo
    select_photos()

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
    text1()
    # done & send
    input()
    os.system('adb %s shell input tap 580 2111' % a)
    # delete useless files
    for f in os.listdir(local_path):
        os.remove(os.path.join(local_path, f))
    print('used photos deleted!')
    # click done
    time.sleep(3)
    os.system('adb %s shell input tap 540 2135' % a)
