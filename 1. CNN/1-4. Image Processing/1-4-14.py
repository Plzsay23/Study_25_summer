import cv2

img = cv2.imread("./images/Raiden.jpg")
img_blur = cv2.GaussianBlur(img, (0, 0), 2)

img_sharp = cv2.addWeighted(img, 1.6, img_blur, -0.5, 0)

cv2.imshow("img", img)
cv2.imshow("img_blur", img_blur)
cv2.imshow("img_sharp", img_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()

