import cv2

img = cv2.imread("./images/test.jpg")

img = cv2.resize(img, (600, 600))

cv2.imshow("test", img)

cv2.waitKey()

cv2.destroyAllWindows()