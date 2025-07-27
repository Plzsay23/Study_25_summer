import cv2
import numpy as np

b, g, r = (255, 0, 0), (0, 255, 0), (0, 0, 255)
img = np.zeros((400, 600, 3), np.uint8)
img[:] = (0, 0, 0)

pt1, pt2 = (50, 50), (200, 50)
pt3, pt4 = (50, 200), (200, 200)

cv2.line(img, pt1, pt2, b)
cv2.line(img, pt3, pt4, g)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

