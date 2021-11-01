import pyautogui as py
import os
import time
import pyperclip as pc

save = 1


# ---refreshing the photos---
def re_fresh_photo():
    i = 1

    # edit
    py.moveTo(x=97, y=698)
    py.click()
    time.sleep(1)

    # beautify
    py.moveTo(x=39, y=621)
    py.click()
    time.sleep(2)

    # save
    py.moveTo(x=291, y=99)
    py.click()
    time.sleep(1)
    global save
    save += 1
    print('save + 1')

    while i != save:
        print('i not equal save,i:' + str(i) + ' save: ' + str(save))
        # drag to right
        py.moveTo(x=295, y=407)
        time.sleep(1)
        py.dragTo(x=40, y=407, duration=0.3, button='left')
        i += 1
        time.sleep(1)

    # delete original file
    py.moveTo(x=229, y=699)
    py.click()
    time.sleep(1)
    py.click()
    time.sleep(1)


# ---select photos---
def select_photos():
    x_base = 320
    x_add = 350
    y_base = 420
    y_add = 330

    for i in range(0, loop):
        x = x_base + x_add * (i % 3)
        y = y_base + y_add * (int(i / 3))
        os.system("adb shell input tap %s %s" % (x, y))


# adding photos into phone
def push_photos():
    print(str(loop) + 'files detected. ')
    for i in pics:
        os.system('adb push ' + local_path + i + ' ' + phone_path)
        print(i + ' sent to phone')
    print('all files has been sent... waitting system to respone..')
    time.sleep(5)


# local_path = '/Users/ryan/Desktop/red/pics_for_post/'
# pics = os.listdir(local_path)
# phone_path = '/sdcard/DCIM/Camera'
# loop = len(pics)
# loop_count = 0
#
# push_photos()
#
# # home
# py.moveTo(x=165, y=747)
# py.click()
# time.sleep(1)
#
# # photo icon
# py.moveTo(x=132, y=393)
# py.click()
# time.sleep(2)
#
# # move to latest
# py.moveTo(x=44, y=181)
# py.click()
# time.sleep(1)
#
# # looping ->让手机tmd刷新一遍tmd相簿
# while loop_count != loop:
#     re_fresh_photo()
#     loop_count += 1

# open red
os.system("adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
time.sleep(5)

# add new thread
py.moveTo(x=165, y=707)
py.click()
time.sleep(1)

# -----adding photo
loop = 6
select_photos()

# next
py.moveTo(x=287, y=712)
py.click()
time.sleep(1)

# next again
py.moveTo(x=308, y=102)
py.click()
time.sleep(2)

# title text
pc.copy('这也太美了叭')
py.moveTo(x=114, y=249)
py.click()
py.hotkey('command', 'v')
time.sleep(2)

# main text
pc.copy('''美到犯规，秋季出游出片率贼高耶~
 
精致的女孩子 不仅要穿好看的衣服还要涂好看的口红
多变的服装总不能每套都要搭配不同颜色的，个性穿搭彰显本色！
薄涂厚涂都各有气质。双十一的购物清单如何能缺席美艳。
牢牢锁4！！！ 狠狠爱上！！！''')
py.moveTo(x=83, y=275)
py.click()
py.hotkey('command', 'v')
time.sleep(1)

# done & send
py.moveTo(x=305, y=479)
py.click()
time.sleep(2)
py.moveTo(x=189, y=703)
py.click()









