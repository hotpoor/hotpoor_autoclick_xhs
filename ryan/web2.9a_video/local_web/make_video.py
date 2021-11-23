import os
from PIL import Image

#vidify
resize_path = (os.path.join(os.path.dirname(__file__), 'static/resize/'))
vid_path = (os.path.join(os.path.dirname(__file__), 'static/vid/'))
num = 0
if os.path.isfile(resize_path + '.DS_store'):
    print('DS file detected.')
    os.remove(resize_path + '.Ds_store')
    print('Ds file deleted!')

for i in os.listdir(resize_path):
    num +=1
    i1 = Image.open(resize_path + i)
    i1.save(resize_path + str(num) +'.png')
    os.remove(resize_path+i)
os.system('ffmpeg -y -f image2 -r 1.3 -pattern_type glob -i \"%s*.png\" -pix_fmt yuv420p %stest.mp4' % (resize_path, vid_path))
print('vidify success!')



