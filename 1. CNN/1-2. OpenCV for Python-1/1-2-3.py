import cv2

img_bgr = cv2.imread("./images/test.jpg")
img_gray = cv2.imread("./images/test.jpg", cv2.IMREAD_GRAYSCALE)

img_bgr = cv2.resize(img_bgr, (500, 600))
img_gray = cv2.resize(img_gray, (500, 600))

cv2.imshow("BGR", img_bgr)
cv2.imshow("GRAY", img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()

