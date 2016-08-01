import cv2
import numpy as np

img = cv2.imread("sudoku.png",0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)

sobel = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)

canny = cv2.Canny(img,200,100,9)

cv2.imshow("adf",canny)

cv2.imshow("ad",laplacian)

cv2.waitKey(0)

cv2.destroyAllWindows()
