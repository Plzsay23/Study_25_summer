import cv2

img_noise = cv2.imread("./images/Miko_sap_noise.jpg")

img_blur = cv2.medianBlur(img_noise, 3)

cv2.imshow("img_noise", img_noise)
cv2.imshow("img_blur", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

