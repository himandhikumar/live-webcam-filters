import cv2
import time
import numpy as np

# Load face cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)
current_filter = 'normal'
prev_time = time.time()

print("Controls: g = grayscale | b = blur | e = edge | c = cartoonify | s = sepia | f = face detect | n = normal | q = quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Filters
    if current_filter == 'grayscale':
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    elif current_filter == 'blur':
        frame = cv2.GaussianBlur(frame, (21, 21), 0)
    elif current_filter == 'edge':
        edges = cv2.Canny(frame, 100, 200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif current_filter == 'cartoonify':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        frame = cartoon
    elif current_filter == 'sepia':
        sepia_matrix = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
        frame = cv2.transform(frame, sepia_matrix)
        frame = np.clip(frame, 0, 255).astype(np.uint8)

    elif current_filter == 'face_detect':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Overlay FPS and filter info
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f'Filter: {current_filter}', (10, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Webcam Filters", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        current_filter = 'grayscale'
    elif key == ord('b'):
        current_filter = 'blur'
    elif key == ord('e'):
        current_filter = 'edge'
    elif key == ord('c'):
        current_filter = 'cartoonify'
    elif key == ord('s'):
        current_filter = 'sepia'
    elif key == ord('f'):
        current_filter = 'face_detect'
    elif key == ord('n'):
        current_filter = 'normal'

cap.release()
cv2.destroyAllWindows()
