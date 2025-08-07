import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라가 인식되지 않음')
    sys.exit()

print('카메라 인식됨')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('camera.avi', fourcc, fps1, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    out.write(frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()
out.release()