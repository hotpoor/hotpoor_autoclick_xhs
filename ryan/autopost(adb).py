# coded by Ryan， 目前适用于carol。
import os
import time
from PIL import Image

save = 1


# ---refreshing the photos---
def re_fresh_photo():
    i = 1

    # edit
    os.system('adb shell input tap 310 2100')
    time.sleep(1)

    # beautify
    os.system('adb shell input tap 139 1857')
    time.sleep(2)

    # save
    os.system('adb shell input tap 938 173')
    time.sleep(3)
    global save
    save += 1
    print('save + 1')

    while i != save:
        print('i not equal save,i:' + str(i) + ' save: ' + str(save))
        # drag to right
        os.system('adb shell input swipe 931 1150 174 1090 135')
        i += 1
        time.sleep(1)

    # delete original file
    os.system('adb shell input tap 751 2091')
    time.sleep(0.5)
    os.system('adb shell input tap 751 2091')
    time.sleep(0.5)


# ---select photos---
def select_photos():
    x_base = 307
    x_add = 365
    y_base = 420
    y_add = 360

    for i in range(0, loop):
        x = x_base + x_add * (i % 3)
        y = y_base + y_add * (int(i / 3))
        os.system("adb shell input tap %s %s" % (x, y))


# adding photos into phone
def push_photos():
    print(str(loop) + ' files detected. ')
    for i in pics:
        i1 = Image.open(local_path + i)
        i1.save(local_path + i)
        os.system('adb push ' + local_path + i + ' ' + phone_path)
        print('file name: ' + i + ' sent to phone')
        time.sleep(1)
    print('all files has been sent... waitting system to respone..')
    time.sleep(3)


# --- put text into title and main text---
def text():
    f = open('文案（标题前标注T）.txt')
    check = 0
    for line in f:
        if check == 0 and line[0] == 'T':
            os.system('adb shell input tap 311 634')
            os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\'" % line[1:])
            check += 1
            os.system('adb shell input tap 330 824')
        else:
            os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\' ' % line)
            os.system('adb shell am broadcast -a ADB_INPUT_CODE --ei code 66')
    f.close()


local_path = '/Users/ryan/Desktop/red/pics_for_post/'
# sort file names (place photos with correct pattern)
pics = os.listdir(local_path)
pics.sort()
# sort end
phone_path = '/sdcard/DCIM/Camera'
loop = len(pics)
loop_count = 0

push_photos()

# home
os.system('adb shell input tap 555 2280')
time.sleep(1)

# photo icon
os.system('adb shell input tap 416 1057')
time.sleep(2)

# move to latest
os.system('adb shell input tap 140 510')
time.sleep(1)

# looping ->让手机tmd刷新一遍tmd相簿
while loop_count != loop:
    re_fresh_photo()
    loop_count += 1

# open red
os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
time.sleep(5)

# add new thread
os.system('adb shell input tap 540 2150')
time.sleep(1)

# -----adding photo
select_photos()

# next
os.system('adb shell input tap 935 2150')
time.sleep(0.5)

# next again
os.system('adb shell input tap 990 170')
time.sleep(0.5)

# ---main--- put text in thread boxes
text()

# done & send
os.system('adb shell input tap 580 2111')
