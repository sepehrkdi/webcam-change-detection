import cv2
import time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Capturing frame_t in 3 seconds...")
time.sleep(3)
ret, frame1 = cap.read()
cv2.imwrite("frame_t.jpg", frame1)

print("Move something in the scene. Capturing frame_t1 in 3 seconds...")
time.sleep(3)
ret, frame2 = cap.read()
cv2.imwrite("frame_t1.jpg", frame2)

cap.release()
cv2.destroyAllWindows()
print("Done.")
