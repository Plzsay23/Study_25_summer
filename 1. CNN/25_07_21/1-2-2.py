import cv2

img_gray = cv2.imread("./images/test.jpg", cv2.IMREAD_GRAYSCALE)

img_gray = cv2.resize(img_gray, (600, 600))

cv2.imshow("test", img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()

