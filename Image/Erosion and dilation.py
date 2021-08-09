import cv2
import numpy as np

img = cv2.imread('pic.png',1)

img = cv2.resize(img,(500,500),interpolation = cv2.INTER_CUBIC)

kernel = np.ones((5,5),np.uint8)

img_erosion = cv2.erode(img,kernel,iterations = 25)
img_dilation = cv2.dilate(img,kernel,iterations = 25)

cv2.imshow('Input',img)
cv2.imshow('Erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)

cv2.waitKey(0)
