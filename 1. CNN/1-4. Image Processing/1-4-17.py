import cv2

img_gau = cv2.imread("./images/Miko_gaussian_noise.jpg")

img_blur = cv2.GaussianBlur(img_gau, (3, 3), 0)

cv2.imshow("img_gau", img_gau)
cv2.imshow("img_blur", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

