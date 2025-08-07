import cv2
import matplotlib.pyplot as plt

# 이미지 크기는 같아야함
img1 = cv2.imread('./images/이미지')
img2 = cv2.imread('./images/이미지')

# 0 ~ 255 값을 벗아나면 256으로 나눈 나머지가 됨
dst1 = img1 + img2

dst2 = cv2.add(img1, img2)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

img = {'img1': img1, 'img2': img2, 'dst1': dst1, 'dst2':dst2}
for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
plt.show()
