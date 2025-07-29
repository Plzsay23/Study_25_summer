import cv2
import numpy as np

def add_salt_pepper_noise(image, prob):
    noisy = image.copy()
    height, width = image.shape[:2]
    total_pixels = height * width

    # Salt (255)
    num_salt = int(prob * total_pixels / 2)
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    if image.ndim == 2:
        noisy[coords[0], coords[1]] = 255
    else:
        noisy[coords[0], coords[1], :] = 255

    # Pepper (0)
    num_pepper = int(prob * total_pixels / 2)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    if image.ndim == 2:
        noisy[coords[0], coords[1]] = 0
    else:
        noisy[coords[0], coords[1], :] = 0

    return noisy

# 이미지 불러오기
img = cv2.imread('./images/Miko.jpg')

# 노이즈 추가 (5% 확률)
noisy_img = add_salt_pepper_noise(img, prob=0.05)

cv2.imshow("Original", img)
cv2.imshow("Salt and Pepper Noise", noisy_img)
cv2.imwrite("./images/Miko_sap_noise.jpg", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
