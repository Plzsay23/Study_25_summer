import cv2

img = cv2.imread("./images/test.jpg")
img = cv2.resize(img, (600, 600))

cv2.imshow("img", img)

while True:
    key = cv2.waitKey(0)

    if key == ord("i") or key == ord("I"):
        img = ~img
        cv2.imshow("img", img)
    elif key == ord("q") or key == ord("Q"):
        break

cv2.destroyAllWindows()

