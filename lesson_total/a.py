import os
from PIL import Image

list = os.listdir(r"C:\Users\PC\Desktop\python lesson\sample\photo")

for i in list:
    pa = os.path.join(r"C:\Users\PC\Desktop\python lesson\sample\photo", i)
    if os.path.getsize(pa) >= 204800:
        img = Image.open(pa)
        img.thumbnail((500,400))
        img.save(pa)
 