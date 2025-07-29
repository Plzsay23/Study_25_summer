import cv2

img = cv2.imread("./images/Dr.Mundo.png", cv2.IMREAD_UNCHANGED)

b, g, r, a = cv2.split(img)

cv2.imshow("img", img)
cv2.imshow("alpha", a)
cv2.waitKey(0)
cv2.destroyAllWindows()

