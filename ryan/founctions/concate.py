from PIL import Image

icon = '/Users/ryan/Desktop/red/local_web/static/icon/icon.png'
i = '/Users/ryan/PycharmProjects/web2.0/local_web/static/upload/111.jpg'
i1 = Image.open(icon)
i2 = Image.open(i)
layer = Image.new('RGBA', (600,800), (0, 0, 0, 0))
r,g,b,a = i1.split()
i2.convert('RGBA')
layer.paste(i2,(0,0))
i1.convert('RGBA')
layer.paste(i1,(70,630), mask= a)
layer.show()