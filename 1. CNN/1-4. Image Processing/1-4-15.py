import cv2

img = cv2.imread("./images/Miko.jpg")
img_sap = cv2.imread("./images/Miko_sap_noise.jpg")
img_gau = cv2.imread("./images/Miko_gaussian_noise.jpg")

cv2.imshow("Original", img)
cv2.imshow("Gaussian Noise", img_gau)
cv2.imshow("Salt-and-Pepper", img_sap)
cv2.waitKey(0)
cv2.destroyAllWindows()