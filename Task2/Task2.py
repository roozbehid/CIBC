import cv2
import sys
from skimage.measure import compare_ssim, compare_nrmse

imA = cv2.imread(sys.argv[1])
imB = cv2.imread(sys.argv[2])

grayA = cv2.cvtColor(imA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imB, cv2.COLOR_BGR2GRAY)

(score, grad) = compare_ssim(grayA, grayB, full=True)
grad = (grad * 255).astype("uint8")
print("SSIM: {}".format(score))

nrmse = compare_nrmse(grayA, grayB)
print("NRMSE: {}".format(nrmse))

thresh = cv2.threshold(grad, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] 

# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
cv2.imshow("Image 1", imA)
cv2.imshow("Image 2", imB)
cv2.imshow("Diff", grad)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)