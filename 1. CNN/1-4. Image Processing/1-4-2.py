import cv2
import numpy as np

b = np.zeros((500, 500), np.uint8) + 125
g = np.ones((500, 500), np.uint8) * 30
r = np.full((500, 500), 100, np.uint8)

list_bgr = [b, g, r]

img = cv2.merge(list_bgr)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

