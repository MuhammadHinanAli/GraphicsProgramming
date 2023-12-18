import cv2
from ultralytics import YOLO
from PIL import Image
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Load an official or custom model
model = YOLO('yolov8n.pt')  # Load an official Detect model

# Perform tracking with the model
#results = model.track(source='traffic.mp4', show=True)  # Tracking with default tracker
#results = model.track(source='traffic2.mp4', show=True)  # Tracking with default tracker
#results = model.track(source='traffic3.mp4', show=True)  # Tracking with default tracker


# Open the video file
video_path = "traffic.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image