import cv2

cap = cv2.VideoCapture("./images/Billiard.mp4")

if not cap.isOpened():
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (600, 1000))

    cv2.imshow("Frame", frame)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()

