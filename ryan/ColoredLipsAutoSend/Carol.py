import time
import os
from random import randrange
import random
from PIL import Image


a = '-s 927aaf0d0421'

while True:
#-- randomise list
    with open('num.txt') as f:
        count = f.readline()
        print(count)
        f.close()
    with open('total.txt') as b:
        Max=b.readline()
        b.close()
    if count == Max:
        exit()

    with open ('num.txt','w') as f:
        f.write(str(int(count)+1))
        f.close()

    newList=[]
    for i in os.listdir('pics/final'):
        if count == i[3:-4] or 'd' + count == i[3:-4]:
            newList.append(i)

    list = os.listdir('pics/final')
    newList.sort()
    NewList=[]
    num = random.sample((0, 1, 2), 3)
    NewList.append(newList[num[0]])
    NewList.append(newList[num[1]])
    NewList.append(newList[num[2]])
    NewList.append(newList[3])
    loop = len(NewList) +1
    print(NewList)
    print(loop)
    # push photos (path)
    local_path = '/Users/ryan/PycharmProjects/kpi冲鸭/venv/pics/final/'
    phone_path = '/sdcard/DCIM/Camera'
    def push_photos(loop,a,NewList):
        print(str(loop) + ' files detected. ')
        # path
        i1 = Image.open('/Users/ryan/PycharmProjects/kpi冲鸭/venv/pics/original/%s.jpg'%count)
        i1.save('/Users/ryan/PycharmProjects/kpi冲鸭/venv/pics/original/%s.jpg'%count)
        NewList = reversed(NewList)
        for i in NewList:
            i1 = Image.open('pics/final/%s'%i)
            i1.save('pics/final/%s'%i)
            os.system('adb %s push ' % a + local_path + i + ' ' + phone_path)
            print('file name: ' + i + ' sent to phone')
            time.sleep(1)

            os.system(
                'adb %s push /Users/ryan/PycharmProjects/kpi冲鸭/venv/pics/original/%s.jpg /sdcard/DCIM/Camera' % (a,count))

        print('file original has been sent...')
        print('all files has been sent... waitting system to respone..')
        os.system(
            'adb %s shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera' % a)
        time.sleep(2)
    push_photos(loop,a,NewList)

    # open red
    os.system('adb %s shell am force-stop com.xingin.xhs' % a)
    time.sleep(1)
    os.system("adb %s shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1" % a)
    time.sleep(10)
    # press new button
    os.system('adb %s shell input tap 544 2150' % a)
    time.sleep(0.5)
    # ---select photos---
    def select_photos(loop, a):
        x_base = 307
        x_add = 365
        y_base = 420
        y_add = 360
        time.sleep(1)
        for i in range(0, loop):
            x = x_base + x_add * (i % 3)
            y = y_base + y_add * (int(i / 3))
            os.system("adb %s shell input tap %s %s" % (a, x, y))


    select_photos(loop,a)
    # next
    os.system('adb %s shell input tap 935 2150' % a)
    time.sleep(0.5)
    # next again
    os.system('adb %s shell input tap 990 170' % a)
    time.sleep(0.5)

    def text():
        n = randrange(1,26)
        f = open('%s.txt'%n)
        print('choosing text example number: %s'% n)
        for line in f:
            if line[0] == 'T':
                print('inputting title')
                os.system('adb %s shell input tap 311 634'% a)
                os.system('adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\' ' % (a, line.replace(' ', '\ ')[1:]))
                os.system('adb %s shell input tap 330 824'% a)
            else:
                os.system('adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\' ' % (a, line.replace(' ', '\ ')))
                #enter key
                os.system('adb %s shell am broadcast -a ADB_INPUT_CODE --ei code 66'% a)
        f.close()
    os.system('adb %s shell ime set com.android.adbkeyboard/.AdbIME' % a)
    text()
    os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    #done
    os.system('adb %s shell input tap 580 2111' % a)
    # click done
    time.sleep(15)
    os.system('adb %s shell input tap 540 2135' % a)
    # to mine
    os.system('adb %s shell input tap 976 2153' % a)
    time.sleep(0.5)
    farmCount = 0
    farm = True
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




