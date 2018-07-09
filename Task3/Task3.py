# ref : https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
import cv2
import sys
import pytest
from skimage.measure import compare_ssim, compare_nrmse

def printImageDiff(img1Path, img2Path):
    imA = cv2.imread(img1Path)
    imB = cv2.imread(img2Path)

    grayA = cv2.cvtColor(imA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imB, cv2.COLOR_BGR2GRAY)

    (score, grad) = compare_ssim(grayA, grayB, full=True)
    #grad = (grad * 255).astype("uint8")

    nrmse = compare_nrmse(grayA, grayB)

    return (score, nrmse)
    #thresh = cv2.threshold(grad, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # show the output images
    #cv2.imshow("Image 1", imA)
    #cv2.imshow("Image 2", imB)
    #cv2.imshow("Diff", grad)
    #cv2.imshow("Thresh", thresh)
    #cv2.waitKey(0)

def test_same_image():
    (ssim, nrmse) = printImageDiff(".\\data\\diff_test\\test_image_1.png",".\\data\\diff_test\\test_image_1.png")
    assert abs(ssim - 1.0) < 0.01
    assert abs(nrmse - 0.0) < 0.01

(ssim, nrmse) = printImageDiff(sys.argv[1],sys.argv[1])
print("structural similarity (SSIM) index is: %f" % ssim)
print("normalized root mean square is: %f" % nrmse)


