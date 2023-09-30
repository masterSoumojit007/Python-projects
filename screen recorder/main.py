import cv2
import pyautogui
import numpy as np
import time

# Get screen dimensions using pyautogui
width, height = pyautogui.size()

dimension = (width, height)

# Define the codec and create a VideoWriter object
f = cv2.VideoWriter_fourcc(*"H264")

output = cv2.VideoWriter("test.mp4", f, 30.0, dimension)

# Set the recording start time
start_time = time.time()

# Set the desired duration for the recording (in seconds)
duration = 10  # Change this to the desired duration

# Calculate the end time
end_time = start_time + duration

while True:
    # Capture a screenshot
    image = pyautogui.screenshot()
    frame = np.array(image)

    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    output.write(frame)

    # Check if the recording duration has elapsed
    current_time = time.time()
    if current_time > end_time:
        break

# Release the VideoWriter and print a message
output.release()
print("Video recording complete.")
