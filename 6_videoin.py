import cv2
import sys

cap = cv2.VideoCapture('./images/동영상파일')

print('현재 opencv 버전: ', cv2.__version__)

if not cap.isOpened():
    print('동영상 실행 불가능')
    sys.exit()

print('동영상 불러오기 가능')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(w)
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(h)
frame_cnt1 = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_cnt1)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKet(10) == 27:
        break

cap.release()