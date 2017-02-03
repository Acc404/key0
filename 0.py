from PIL import Image
import math
import random
import time
start = time.time()
im = Image.open(r"C:\Users\Acc404\Desktop\a.jpg")
def hmove(width,y,di):
    ar = []
    for i in range(width/10):
        ar.append([i*10,10*y,i*10+10,10*y+10])
    if di > 0:
        re0 = im.crop(ar[0])
        for j in range(width/10-1):
            re = im.crop(ar[j+1])
            im.paste(re,ar[j])
        im.paste(re0,ar[width/10-1])
    elif di < 0:
        re0 = im.crop(ar[width/10-1])
        for j in range(width/10-1):
            re = im.crop(ar[width/10-j-2])
            im.paste(re,ar[width/10-j-1])
        im.paste(re0,ar[0])
def vmove(height,x,di):
    ar = []
    for i in range(height/10):
        ar.append([10*x,i*10,10*x+10,i*10+10])
    if di > 0:
        re0 = im.crop(ar[0])
        for j in range(height/10-1):
            re = im.crop(ar[j+1])
            im.paste(re,ar[j])
        im.paste(re0,ar[height/10-1])
    elif di < 0:
        re0 = im.crop(ar[height/10-1])
        for j in range(height/10-1):
            re = im.crop(ar[height/10-j-2])
            im.paste(re,ar[height/10-j-1])
        im.paste(re0,ar[0])
x = []
y = []
def key(width,height):
    for i in range(width/10):
        y.append(random.randint(0,height/10))
    for i in range(height/10):
        x.append(random.randint(0,width/10))
def execut(width,height,x,y,a,b):
    for i2 in range(width/10):
        for i in range(y[i2]):
            vmove(height,i2,b)
    for i4 in range(height/10):
        for i in range(x[i4]):
            hmove(width,i4,a)
def deexecut(width,height,x,y,a,b):
    for i4 in range(height/10):
        for i in range(x[i4]):
            hmove(width,i4,a) 
    for i2 in range(width/10):
        for i in range(y[i2]):
            vmove(height,i2,b)
          
            
#def dekey(x,y):
    
key(im.width,im.height)
execut(im.width,im.height,x,y,1,1)

im.save(r"C:\Users\Acc404\Desktop\key.jpg")

start1 = time.time()
deexecut(im.width,im.height,x,y,-1,-1)

im.save(r"C:\Users\Acc404\Desktop\dekey.jpg")

end = time.time()

print("keytime: " + str(start1-start) + "\ndekeytime: " + str(end-start1) + "\ntotaltime: " + str(end-start))
