import cv2
import numpy as np

gold = (0, 215, 255)
img = np.zeros((600, 600, 3), np.uint8)
img[:] = (0, 0, 0)

pt1 = (300, 180)
pt2 = (360, 390)
pt3 = (200, 260)
pt4 = (400, 260)
pt5 = (240, 390)

cv2.line(img, pt1, pt2, gold, 2)
cv2.line(img, pt2, pt3, gold, 2)
cv2.line(img, pt3, pt4, gold, 2)
cv2.line(img, pt4, pt5, gold, 2)
cv2.line(img, pt5, pt1, gold, 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

