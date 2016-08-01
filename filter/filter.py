import cv2
import numpy as np
img = cv2.imread("obj.png")

kernel = np.ones((5,5),np.float32)/25

p_image = cv2.filter2D(img,-1,kernel)

cv2.imshow("adf",cv2.blur(img,(5,5)))

cv2.imshow("addf",p_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
