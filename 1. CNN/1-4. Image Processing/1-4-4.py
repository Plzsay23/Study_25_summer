import cv2

img1 = cv2.imread("./images/Dr.Mundo.png", cv2.IMREAD_UNCHANGED)
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.imread("./images/Tahm_Kench.png", cv2.IMREAD_UNCHANGED)
img2 = cv2.resize(img2, (500, 500))

b1, g1, r1, a1 = cv2.split(img1)
b2, g2, r2, a2 = cv2.split(img2)

bgra_list = [b2, g2, r2, a1]

img3 = cv2.merge(bgra_list)

cv2.imshow("Dr.Mundo", img1)
cv2.imshow("Tahm_Kench", img2)
cv2.imshow("img", img3)

cv2.imwrite("./images/test.png", img3)

retval = cv2.imwrite("./images/test.png", img3)
if retval:
    print("Save Success")
else:
    print("Save Failed")

# cv2.imwrite("./images/test.png", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()

