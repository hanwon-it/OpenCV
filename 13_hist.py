import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/이미지1', cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread('./images/이미지2')

# 히스토그램
# 이미지 히스토그램: 밝기(또는 색상) 값의 분포를 그래프로 표현
# 어떤 픽셀이 밝기 0(검정)인지 255(흰색)인지, 각 값이 몇 개나 있는지를 확인
# images: 대상 이미지 리스트
# channel: 분석할 채널 번호(B:0, G=1, R=2)
# mask: 분석할 영역 마스크(None: 전체)
# histSize: 히스토그램의 빈 개수
# ranges: 값의 범위
hist = cv2.calcHist([img1], [0], None, [256], [0, 255])

print('shape: ', img2.shape)
print('dtype: ', img2.dtype)

# b = img[:, :, 0]
# g = img[:, :, 1]
# r = img[:, :, 2]

b, g, r = cv2.split(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
plt.plot(hist)
plt.show()
cv2.waitKey()

# candies.png 영상을 컬러로 불러와 3개의 채널을 계산하여 히스토그램을 그리기
# 단, 하나의 plot에서 BGR 그래프를 모두 출력(색상을 다르게 표현)