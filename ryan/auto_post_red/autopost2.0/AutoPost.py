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
    os.system('adb %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera'% a)
    time.sleep(3)


# --- put text into title and main text---
def text():
    f = open('文案（标题前标注T）.txt')
    check = 0
    for line in f:
        if check == 0 and line[0] == 'T':
            os.system('adb %s shell input tap 311 634'% a)
            os.system("adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\'" % (a, line.replace(' ', '\ ')[1:]))
            check += 1
            os.system('adb %s shell input tap 330 824'% a)
        else:
            os.system('adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\' ' % (a, line.replace(' ', '\ ')))
            os.system('adb %s shell am broadcast -a ADB_INPUT_CODE --ei code 66'% a)
    f.close()



local_path = '/Users/ryan/Desktop/red/local_web/static/upload/'

# delete DS file for MAC users
if os.path.isfile(local_path + '.DS_store'):
    print('DS file detected.')
    os.remove(local_path + '.Ds_store')
    print('Ds file deleted!')

# sort file names (place photos with correct pattern)
pics = os.listdir(local_path)
pics.sort(reverse=True)
loop = len(pics)


a = input('is this for Frank or Carol? pls enter first letter of the name to continue...')

if a == 'c':
    a = '-s 927aaf0d0421'
elif a == 'f':
    a = '-s a022d1760821'
else:
    a = input('is this for Frank or Carol? pls enter first letter of the name to continue...')


phone_path = '/sdcard/DCIM/Camera'
loop_count = 0

# --- push photos
push_photos()


# ---open red
os.system("adb %s shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1" % a)
time.sleep(5)

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
os.system('adb %s shell ime set com.android.adbkeyboard/.AdbIME' % a)
text()
os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)


# done & send
input()
os.system('adb %s shell input tap 994 1378' % a)
os.system('adb %s shell input tap 580 2111' % a)

# 清楚缓存
os.system('cd %s' % local_path)
os.system('rm -rf *')
input()
os.system('cd /Users/ryan/Desktop/red/local_web/static/files')
os.system('rm - rf *')

