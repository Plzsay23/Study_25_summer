import cv2

img = cv2.imread("./images/Miko_gaussian_noise.jpg")

bilat = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imshow("img", img)
cv2.imshow("bilat", bilat)
cv2.waitKey(0)
cv2.destroyAllWindows()

