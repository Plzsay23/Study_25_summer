import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, sigma=25):
    # 노이즈 생성 (정규분포)
    gaussian = np.random.normal(mean, sigma, image.shape).astype(np.float32)

    # 이미지에 노이즈 더하기
    noisy = image.astype(np.float32) + gaussian

    # 값 클리핑 후 uint8로 변환
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)

    return noisy

# 이미지 불러오기
img = cv2.imread('./images/Miko.jpg')

# 가우시안 노이즈 추가
noisy_img = add_gaussian_noise(img, mean=0, sigma=25)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Noise", noisy_img)
cv2.imwrite("./images/Miko_gaussian_noise.jpg", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
