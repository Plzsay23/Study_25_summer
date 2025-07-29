import cv2
import numpy as np

img = cv2.imread("./images/Raiden.jpg")

kernel = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]], np.float32)

img_sharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("img", img)
cv2.imshow("img_sharp", img_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()

