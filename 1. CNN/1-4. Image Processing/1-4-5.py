import cv2

img = cv2.imread("./images/Citlali.jpg")

img_add = cv2.add(img, 100)

cv2.imshow("img", img)
cv2.imshow("img_add", img_add)
cv2.waitKey(0)
cv2.destroyAllWindows()

