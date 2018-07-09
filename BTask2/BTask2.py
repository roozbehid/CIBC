import cv2
import sys
import os
from pandas import read_csv
import numpy as np

print("usage is : BTask2.py img1 img2 coress1 corres2")
if len(sys.argv) < 5:
    print("not enought arguments")
    exit

img1 = cv2.imread(sys.argv[1])
rows,cols,ch = img1.shape
img2 = cv2.imread(sys.argv[2])

corr1 = read_csv(sys.argv[3], header = None, names = ['x','y'], sep="\s+")
corr2 = read_csv(sys.argv[4], header = None, names = ['x','y'], sep="\s+")


M = cv2.getAffineTransform(corr1.head(3).astype(np.float32).values, corr2.head(3).astype(np.float32).values)
dst = cv2.warpAffine(img1,M,(cols,rows))

cv2.imshow('img1',img1)
cv2.imshow('img2',dst)
cv2.waitKey(0)