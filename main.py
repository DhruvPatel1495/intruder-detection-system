import cv2
import time
import os
from alert import send_email_alert

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create folder for intruder images
if not os.path.exists("intruders"):
    os.makedirs("intruders")

cap = cv2.VideoCapture(0)

print("[INFO] Starting Intruder Detection...")
time.sleep(2)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Intrusion logic
    if len(faces) > 1:
        filename = f"intruders/intruder_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print("[ALERT] Multiple faces detected!")

        send_email_alert(filename)
        time.sleep(5)

    cv2.imshow("Intruder Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()