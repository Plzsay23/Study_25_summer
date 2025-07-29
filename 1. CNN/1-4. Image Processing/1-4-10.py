import cv2
import numpy as np

src = cv2.imread("./images/candies.png")

dst = cv2.inRange(src, lowerb=(0, 128, 0), upperb=(100, 255, 200))

src_add = cv2.add(src, (dst, dst, dst))

cv2.imshow("src_add", src_add)
cv2.waitKey(0)
cv2.destroyAllWindows()

