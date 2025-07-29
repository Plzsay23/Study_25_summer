import cv2

img = cv2.imread("./images/Citlali.jpg")

img_blur = cv2.GaussianBlur(img, (9, 9), 5)

cv2.imshow("img", img)
cv2.imshow("img_blur", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

