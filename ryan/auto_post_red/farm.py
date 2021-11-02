import os


# carol 927aaf0d0421
# frank a022d1760821

num = 1
while True:
    #frank
    os.system("adb -s a022d1760821 shell input tap 220 1356")
    os.system("adb -s a022d1760821 shell input swipe 805 752 144 752 130")
    os.system("adb -s a022d1760821 shell input swipe 805 752 144 752 130")
    os.system("adb -s a022d1760821 shell input swipe 521 499 576 1835 130")
    os.system("adb -s a022d1760821 shell input swipe 576 1835 521 499 130")
    os.system("adb -s a022d1760821 shell input tap 67 158")
    num += 1
    print('loop : %s' % num)