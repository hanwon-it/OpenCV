import cv2

img = cv2.imread('./images/sun.jpg')

x = 182
y = 22
w = 119
h = 108

roi = img[y:y+h, x:x+w]
roi_copy = roi.copy()
img[y:y+h, x+w:x+w+w] = roi

# 두 태양을 박스로 감싸기

cv2. imshow('img', img)
cv2.waitKey()