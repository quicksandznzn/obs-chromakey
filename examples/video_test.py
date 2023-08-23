import cv2
from chromakey import chroma_key
import numpy as np

# Open the video file
video_path = "input_video.mov"
cap = cv2.VideoCapture(video_path)
# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# Define the codec and create a VideoWriter object
output_path = "output_video.mov"
fourcc = cv2.VideoWriter_fourcc(*"MJPG")  # Specify the codec for MOV format
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
# Parameters for chroma keying
tola = 25  # Tolerance levels
tolb = 50


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Create a black background image
    background_image = np.zeros_like(frame)

    # Apply chroma keying
    masked_frame, _ = chroma_key(
        frame,
        keycolor="#6dff8b",
        background_image=background_image,
        tola=tola,
        tolb=tolb,
    )

    out.write(masked_frame)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
