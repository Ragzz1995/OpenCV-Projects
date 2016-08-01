import cv2
import numpy as np
img = cv2.imread("sudoku.png")
img_gray = cv2.imread("sudoku.png",0)

thresh_img = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,2)

th2 = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,10)



cv2.imshow("asdfa",thresh_img)
cv2.imshow("asdf",th2)

cv2.waitKey(0)
cv2.destroyAllWindows()

