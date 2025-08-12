import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8x.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    bbox_frame = np.array([])
    for r in results:
        bbox_frame = r.plot()

    cv2.imshow("YOLO object detection", bbox_frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

