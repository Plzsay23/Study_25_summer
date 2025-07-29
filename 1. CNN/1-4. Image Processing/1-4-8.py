import cv2

src1 = cv2.imread("./images/Citlali.jpg")
src2 = cv2.imread("./images/Raiden.jpg")

img = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

cv2.imshow("src1", src1)
cv2.imshow("src2", src2)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

