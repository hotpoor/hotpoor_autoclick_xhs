import os

dir = '/Users/ryan/PycharmProjects/web2.0/local_web/static/upload/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
print('used photos deleted!')


dir = '/Users/ryan/PycharmProjects/web2.0/local_web/static/resize/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
print('used resized photo deleted!')

dir = '/Users/ryan/PycharmProjects/web2.0/local_web/static/vid/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
print('used vid deleted!')

dir = '/Users/ryan/PycharmProjects/web2.0/local_web/static/files/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
print('used jason deleted!')