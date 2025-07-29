import cv2

img = cv2.imread("./images/Citlali.jpg")

b, g, r = cv2.split(img)

b = cv2.add(b, 100)

img_add = cv2.merge([b, g, r])

cv2.imshow("img", img)
cv2.imshow("img_add", img_add)
cv2.waitKey(0)
cv2.destroyAllWindows()


