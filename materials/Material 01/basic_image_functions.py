# -*- coding: utf-8 -*-
"""basic_image_functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fYUp_9tH-dzvu-gaf5EPQX2PKXOAs0fC

<a href="https://colab.research.google.com/github/labviros/computer-vision-topics/blob/version2020/lesson01-basics/basic_image_functions.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# How to open images and make basic changes such as convert to gray scale, rotate and resize.

To open and show an image you can use PIL and matplotlib as shown in the following code.
If you uncomment the two last lines, the axis values will desapear.
"""

# Commented out IPython magic to ensure Python compatibility.
from PIL import Image
import matplotlib.pyplot as plt
# %matplotlib inline

im = Image.open("castle.jpg")
plt.imshow(im)
#plt.xticks([0,100,500,1000])
plt.yticks([])

"""Another way to show an image is to use the display method."""

from PIL import Image
im = Image.open("castle.jpg")
display(im)

"""The following code shows how to convert an image to gray scale and show both the original and gray scale image in the same figure using "subplot".
Also note the alternative way to remove the axis in the second subplot.
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open("castle.jpg")

fig = plt.figure(figsize=(20,10))
fig.add_subplot(1,2,1)
plt.imshow(im)
plt.xticks([])
#plt.yticks([])
#plt.axis('off')

im2 = im.convert('L')
fig.add_subplot(1,2,2)
plt.imshow(im2,cmap='gray')
plt.axis('off')

plt.show()

"""You can also save an image."""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from PIL import Image
import matplotlib.pyplot as plt


im = Image.open("castle.jpg")
im2 = im.convert('L')
im2.save('teste.jpg')

im = Image.open('teste.jpg')
plt.imshow(im,cmap='gray')

"""Rotate an image according to an angle described in degress."""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from PIL import Image
# %matplotlib inline

im = Image.open("castle.jpg")

im2 = im.rotate(90)
plt.imshow(im2)
plt.axis('off')

"""Let's now read the size of an image and resize it."""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from PIL import Image
# %matplotlib inline

im = Image.open("castle.jpg")
width, height = im.size
print ("Width: ", width, " Height: ", height)

im2 = im.resize((int(width/5),int(height/3)))

width, height = im2.size
print ("Width: ", width, " Height: ", height)


fig = plt.figure(figsize=(15,10))
fig.add_subplot(2,1,1)
plt.imshow(im)
plt.xticks([])
plt.yticks([])

fig.add_subplot(2,1,2)
plt.imshow(im2)
plt.xticks([])
plt.yticks([])

"""As the next step we are going to crop a region from the image, rotate and paste it in the same image.

"""

# Commented out IPython magic to ensure Python compatibility.
from PIL import Image
import matplotlib.pyplot as plt
# %matplotlib inline

im = Image.open("castle.jpg")

# define the box to be cropped
box = (300,400,800,700)

# make a copy of the original image
im2 = im.copy()
# crop the part of the image inside the box
region = im2.crop(box)



# you can rotate using one of the following commands:
region = region.rotate(135)
#region = region.transpose(Image.ROTATE_180)

im2.paste(region,box)

fig = plt.figure(figsize=(15,30))
fig.add_subplot(1,2,1)
plt.imshow(im)
plt.xticks([])
plt.yticks([])

fig.add_subplot(1,2,2)
plt.imshow(im2)
plt.xticks([])
plt.yticks([])