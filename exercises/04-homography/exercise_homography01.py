# -*- coding: utf-8 -*-
"""Antonio Sant Ana de Oliveira - exercise_homography01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WN8oZfxYKteElsXlWOPG_z_mkPgN45ol

<a href="https://colab.research.google.com/github/labviros/computer-vision-topics/blob/version2020/lesson05-homography/sift_homography.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

#Homography Applications Examples

We are going to install OpenCV to use the homography function, as well the SIFT detector and some matching functions that are available at the OpenCV libraries.

#Rectifying a Document
"""

def my_DLT(pts1,pts2):

  # Add homogeneous coordinates
  pts1 = pts1.T
  pts1 = np.vstack((pts1, np.ones(pts1.shape[1])))

  pts2 = pts2.T
  pts2 = np.vstack((pts2, np.ones(pts2.shape[1])))

  # Compute matrix A

  for i in range(pts1.shape[1]):
    Ai = np.array([[0,0,0, *-pts2[2,i]*pts1[:,i], *pts2[1,i]*pts1[:,i]],
                   [*pts2[2,i]*pts1[:,i], 0,0,0, *-pts2[0,i]*pts1[:,i]]])
    if i == 0:
      A = Ai
    else:
      A = np.vstack((A,Ai))
      # A = np.concatenate(A,axis=0)

  print(A)
  # Perform SVD(A) = U.S.Vt to estimate the homography

  U,S,Vt = np.linalg.svd(A)

  # Reshape last column of V as the homography matrix

  h = Vt[-1]
  H_matrix = h.reshape((3,3))

  return H_matrix

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import imutils
#import plotly.express as px
# %matplotlib inline

### Setting printing options
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
np.set_printoptions(precision=3,suppress=True)


#MIN_MATCH_COUNT = 10
img1 = cv.imread('comicsStarWars02.jpg',0) # queryImage


corners_img1 = np.array([[105,123],[650,55],[580,1055],[58,920]])
corners_img2 = np.array([[58,123],[650,123],[650,1000],[58,1000]])

print(corners_img1)

src_pts = np.float32(corners_img1)
dst_pts = np.float32(corners_img2)

print(src_pts)

#####################################################
# Substitute OpenCv function for your homography function

# M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC,5.0)
M = my_DLT(src_pts, dst_pts)
#####################################################


img4 = cv.warpPerspective(img1, M, (img1.shape[1],img1.shape[0])) #, None) #, flags[, borderMode[, borderValue]]]]	)

fig = plt.figure()
fig, axs = plt.subplots(1,2,figsize=(20,10))
ax1 = fig.add_subplot(1,2,1)
plt.imshow(img1, 'gray')
plt.plot(corners_img2[:,0],corners_img2[:,1],'*b')
plt.plot(corners_img1[:,0],corners_img1[:,1],'*r')
ax2 = fig.add_subplot(1,2,2)
plt.imshow(img4,'gray')
plt.plot(corners_img2[:,0],corners_img2[:,1],'*b')
plt.show()