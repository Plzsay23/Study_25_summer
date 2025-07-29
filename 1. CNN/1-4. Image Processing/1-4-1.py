import cv2

img = cv2.imread("./images/candies.png")

b, g, r = cv2.split(img)

cv2.imshow("img", img)
cv2.imshow("BLUE", b)
cv2.imshow("GREEN", g)
cv2.imshow("RED", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

