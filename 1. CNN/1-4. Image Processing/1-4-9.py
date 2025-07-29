import cv2

src = cv2.imread("./images/candies.png")

dst = cv2.inRange(src, lowerb=(0, 128, 0), upperb=(100, 255, 200))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

