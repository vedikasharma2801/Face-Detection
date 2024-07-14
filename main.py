import cv2
import os

# Define the path to the Haar Cascade classifier file
cascade_path = 'haarcascade_frontalface_default.xml'

# Check if the Haar Cascade file exists
if not os.path.isfile(cascade_path):
    print(f"Error: The file {cascade_path} was not found.")
    exit()

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("Error: Could not load Haar Cascade classifier.")
    exit()

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is the default ID for the primary webcam

if not cap.isOpened():
    print("Error: Could not open video stream from webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not read frame from webcam.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the windows
cap.release()
cv2.destroyAllWindows()
