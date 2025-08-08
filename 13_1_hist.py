# candies.png 영상을 컬러로 불러와 3개의 채널을 계산하여 히스토그램을 그리기
# 단, 하나의 plot에서 BGR 그래프를 모두 출력(색상을 다르게 표현)

import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/candies.png')
img2 = cv2.imread('./images/gram.jpg', cv2.IMREAD_GRAYSCALE)
# 히스토그램
# 이미지 히스토그램: 밝기(또는 색상) 값의 분포를 그래프로 표현
# 어떤 픽셀이 밝기 0(검정)인지 255(흰색)인지, 각 값이 몇 개나 있는지를 확인
# images: 대상 이미지 리스트
# channel: 분석할 채널 번호(B:0, G=1, R=2)
# mask: 분석할 영역 마스크(None: 전체)
# histSize: 히스토그램의 빈 개수
# ranges: 값의 범위

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([img1], [1], None, [256], [0, 255])
hist3 = cv2.calcHist([img1], [2], None, [256], [0, 255])
hist4 = cv2.calcHist([img1], [0], None, [256], [0, 255])

print('shape: ', img1.shape)
print('dtype: ', img1.dtype)

b, g, r = cv2.split(img)

# plt.plot(hist1)
# plt.plot(hist2)
# plt.plot(hist3)
# plt.title("RGB 1: hist1, hist2, hist3")

# 두 번째 그래프
# plt.figure()
# plt.plot(hist4, color="gray")
# plt.title("GRAY SCALE 2: hist4")

# 1행 2열로 그래프 2개 나눠서 하나의 창에 배치
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# 왼쪽 그래프: hist1, hist2, hist3
axs[0].plot(hist1, label='B')
axs[0].plot(hist2, label='G')
axs[0].plot(hist3, label='R')
axs[0].set_title("B ,G, R")
axs[0].legend()

# 오른쪽 그래프: hist4 (회색)
axs[1].plot(hist4, color='gray', label='GRAY_SCALE')
axs[1].set_title("GRAY_SCALE")
axs[1].legend()

# 전체 레이아웃 자동 정리
plt.tight_layout()
plt.show()

cv2.waitKey()