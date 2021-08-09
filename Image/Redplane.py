import cv2
import numpy as np

pic = cv2.imread('pic.png');
img = cv2.resize(pic,(400,400), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Original Picture',img);

Red_plane = img[: , : , 2];
cv2.imshow('Red Plane Image',Red_plane);

SobelOP = [[-1,-2,-1],[0,0,0],[1,2,1]];
r,c = Red_plane.shape;
op = np.zeros((r,c),dtype = np.uint8);
for i in range (0,r-2):
    for j in range(0,c-2):
        partimg = abs(Red_plane[i,j]*-1 + Red_plane[i+1,j]*-2 + Red_plane[i+2,j]*-1 + Red_plane[1,j+2]*1 + Red_plane[i+1,j+2]*2 + Red_plane[i+2,j+2]*1);
        op[i,j] = partimg;
cv2.imshow('Edge Image',op);
cv2.waitKey(0)
cv2.destroyAllWindows()
