from random import randrange

title = 'asdfghjkl;'
a = randrange(0 , (len(title)-1))
title = title.replace(title[a],'口红',1)

print(a)
print(title)