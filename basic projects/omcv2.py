import cv2
import numpy as np
import mediapipe as mp
import pytesseract

# Initialize MediaPipe Hand solution
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Configure pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Update the path if necessary

def detect_text(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Use pytesseract to detect text
    text = pytesseract.image_to_string(gray)
    h, w = gray.shape
    boxes = pytesseract.image_to_boxes(gray)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(frame, (x, frame.shape[0] - y), (w, frame.shape[0] - h), (0, 255, 0), 2)
    return frame, text

def main():
    cap = cv2.VideoCapture(0)  # Change the index if you have multiple cameras

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Text detection
        frame, text = detect_text(frame)
        print("Detected Text:", text)

        # Hand tracking
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Text Detection and Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
