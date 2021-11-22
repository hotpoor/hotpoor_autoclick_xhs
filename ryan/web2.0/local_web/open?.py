import os
import time
from PIL import Image

local_path = os.path.join(os.path.dirname(__file__), 'static/upload/')
shorts = os.listdir( os.path.join(os.path.dirname(__file__), 'static/files/'))


for i in shorts:
    i = i[:-5]
    pics = []
    for p in os.listdir(local_path):
        if p[:-6] in i:
            pics.append(p)


    pics.sort(reverse=True)
    loop = len(pics)
print(pics)
print(loop)