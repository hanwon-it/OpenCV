import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라가 인식되지 않음')
    sys.exit()

print('카메라 인식됨')

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(w)
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(h)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKet(10) == 27:
        break