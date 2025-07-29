import cv2
import numpy as np

y = (0, 255, 255)
img = np.zeros((600, 600, 3), np.uint8)
img[:] = (0, 0, 0)

pt1, pt2 = (150, 150), (450, 450)

cv2.rectangle(img, pt1, pt2, y, 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

