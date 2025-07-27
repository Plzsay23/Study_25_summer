import cv2
import numpy as np

oldx = oldy = -1

def mouse_event(event, x, y, flags, param):
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 0, 0), 2)
            cv2.imshow("img", img)
            oldx, oldy = x, y

img = np.full((600, 600, 3), 255, np.uint8)

cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse_event, img)

cv2.imshow("img", img)

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        img[:] = (255, 255, 255)
        cv2.imshow("img", img)

    elif key == ord('q') or key == ord('Q'):
        break

cv2.destroyAllWindows()

