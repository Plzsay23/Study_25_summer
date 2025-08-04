import cv2
import numpy as np

img_raw = cv2.imread("./images/Mavuika_raw.jpg")
cv2.imshow("img_raw", img_raw)
bg = cv2.imread("./images/background.jpg")
cv2.imshow("bg", bg)

img_raw = cv2.cvtColor(img_raw, cv2.COLOR_BGR2HSV)

lower = np.array([50, 150, 0])
upper = np.array([80, 255, 255])

mask = cv2.inRange(img_raw, lowerb=lower, upperb=upper)

mask_inv = cv2.bitwise_not(mask)

img_fg = cv2.bitwise_and(img_raw, img_raw, mask=mask_inv)
img_fg = cv2.cvtColor(img_fg, cv2.COLOR_HSV2BGR)
img_bg = cv2.bitwise_and(bg, bg, mask=mask)

result = cv2.add(img_fg, img_bg)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


