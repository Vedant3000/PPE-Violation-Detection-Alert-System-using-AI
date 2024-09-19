import cv2

# Replace CAMERA_URL with the URL of your IP camera
CAMERA_URL = "http://192.168.12.10:4747/video"

# Create a VideoCapture object and set the URL of the camera
capture = cv2.VideoCapture(CAMERA_URL)

# Check if the camera is opened
if not capture.isOpened():
  print("Unable to connect to camera")
  exit()

# Read and display the video stream
while True:
  # Capture the frame from the camera
  success, frame = capture.read()

  # Check if the frame was successfully captured
  if not success:
    print("Unable to read frame")
    break

  # Display the frame
  cv2.imshow('Video Stream', frame)

  # Check if the user pressed 'q' to quit
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# Release the VideoCapture object
capture.release()