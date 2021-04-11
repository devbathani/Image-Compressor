#pip install pillow

import PIL
from PIL import Image
from tkinter.filedialog import *

# IMAGE PATH OF USER

path = askopenfilename()

#SEND IMAGE TO PILLOW
  
image = PIL.Image.open(path)

#HEIGHT AND WIDTH OF IMAGE FOR COMPRESSING PROCESS

height, width = image.size

#COMPRESSING PROCESS

image = image.resize((height, width) , PIL.Image.ANTIALIAS)

#SAVE PATH FOR IMAGE

savepath = asksaveasfilename()

image.save(savepath + "-compressed.JPG")