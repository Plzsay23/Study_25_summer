import cv2
from ultralytics import YOLO

model_face = YOLO("yolov8n-face.pt")
model_hand = YOLO('yolov8n-hand.pt')

sticker_img = cv2.imread("./images/ironman-face.png", cv2.IMREAD_UNCHANGED)
hand_sticker_img = cv2.imread("./images/ironman-hand.png", cv2.IMREAD_UNCHANGED)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results_face = model_face(frame, conf=0.6)

    for r in results_face:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            face_width = x2 - x1
            face_height = y2 - y1

            sticker_width = int(face_width * 1.35)
            sticker_height = int(sticker_img.shape[0] * (sticker_width / sticker_img.shape[1]))
            resized_sticker = cv2.resize(sticker_img, (sticker_width, sticker_height), interpolation=cv2.INTER_AREA)

            sticker_x1 = x1 + (face_width - sticker_width) // 2
            sticker_y1 = y1 + (face_height - sticker_height) // 2
            sticker_x2 = sticker_x1 + sticker_width
            sticker_y2 = sticker_y1 + sticker_height

            if sticker_y1 < 0 or sticker_x1 < 0 or sticker_y2 > frame.shape[0] or sticker_x2 > frame.shape[1]:
                continue

            sticker_rgb = resized_sticker[:, :, :3]
            alpha_channel = resized_sticker[:, :, 3] / 255.0

            for c in range(0, 3):
                frame[sticker_y1:sticker_y2, sticker_x1:sticker_x2, c] = \
                    (alpha_channel * sticker_rgb[:, :, c] +
                     (1.0 - alpha_channel) * frame[sticker_y1:sticker_y2, sticker_x1:sticker_x2, c])

    results_hand = model_hand(frame, conf=0.6)
    for r in results_hand:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            hand_width = x2 - x1
            hand_height = y2 - y1

            sticker_width = int(hand_width * 1.2)
            sticker_height = int(hand_sticker_img.shape[0] * (sticker_width / hand_sticker_img.shape[1]))
            resized_sticker = cv2.resize(hand_sticker_img, (sticker_width, sticker_height), interpolation=cv2.INTER_AREA)

            sticker_x1 = x1 + (hand_width - sticker_width) // 2
            sticker_y1 = y1 + (hand_height - sticker_height) // 2
            sticker_x2 = sticker_x1 + sticker_width
            sticker_y2 = sticker_y1 + sticker_height

            if sticker_y1 < 0 or sticker_x1 < 0 or sticker_y2 > frame.shape[0] or sticker_x2 > frame.shape[1]:
                continue

            sticker_rgb = resized_sticker[:, :, :3]
            alpha_channel = resized_sticker[:, :, 3] / 255.0

            for c in range(0, 3):
                frame[sticker_y1:sticker_y2, sticker_x1:sticker_x2, c] = \
                    (alpha_channel * sticker_rgb[:, :, c] +
                     (1.0 - alpha_channel) * frame[sticker_y1:sticker_y2, sticker_x1:sticker_x2, c])

    cv2.imshow('YOLO Face AR Sticker', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()