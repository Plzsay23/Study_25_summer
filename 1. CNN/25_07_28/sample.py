import cv2

img = cv2.imread("./images/seoyoungs.png")

rects = [
    ((51, 39), (260, 263)),
    ((304, 28), (564, 260)),
    ((61, 340), (271, 551)),
    ((391, 310), (535, 568))
]

visible = [False] * len(rects)

base_img = img.copy()

def is_inside_rect(pos, rect):
    (x1, y1), (x2, y2) = rect
    return x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2

def mouse_event(event, x, y, flags, param):
    global visible, img

    if event == cv2.EVENT_LBUTTONDOWN:
        for i, rect in enumerate(rects):
            if is_inside_rect((x, y), rect):
                visible[i] = not visible[i]  # 토글

                img = base_img.copy()
                for j, show in enumerate(visible):
                    if show:
                        cv2.rectangle(img, rects[j][0], rects[j][1], (0, 255, 255), 2)

                cv2.imshow("img", img)
                break

cv2.namedWindow("img")
cv2.setMouseCallback("img", mouse_event)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
