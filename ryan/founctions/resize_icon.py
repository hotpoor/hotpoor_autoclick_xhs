import numpy as np
from PIL import Image, ImageDraw

# Open the input image as numpy array, convert to RGB
img=Image.open("/Users/ryan/Desktop/red/local_web/static/upload/111.jpg").convert("RGB")
npImage=np.array(img)
h,w=img.size
# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h,w],0,360,fill=255)
# Convert alpha Image to numpy array
npAlpha=np.array(alpha)
# Add alpha layer to RGB
npImage=np.dstack((npImage,npAlpha))
# Save with alpha
i = Image.fromarray(npImage)

i = i.resize((100,100))
i.save('/Users/ryan/Desktop/red/local_web/static/upload/222.png')