import os
from random import randrange

i2 = randrange(0,500)
# resize_path = (os.path.join(os.path.dirname(__file__), 'static/resize/'))
# vid_path = (os.path.join(os.path.dirname(__file__), 'static/vid/'))
# os.system('ffmpeg -y -f image2 -r 1.3 -pattern_type glob -i  \"%s/*.png\" -pix_fmt yuv420p %stest.mp4' % (resize_path, vid_path))

for i in range(10):
    i2 = randrange(0,500)

    i1 = randrange(0,700)
    print(i2,i1)