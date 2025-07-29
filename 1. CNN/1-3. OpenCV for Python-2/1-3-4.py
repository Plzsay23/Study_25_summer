import cv2
import numpy as np

w = (255, 255, 255)
img = np.zeros((600, 600, 3), np.uint8)

text = "Hello World!"

pt = (100, 100)

cv2.putText(img, text, pt, cv2.FONT_HERSHEY_TRIPLEX, 2, w)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

