import cv2
from ultralytics import YOLO

# Load an official or custom model
model = YOLO('yolov8n.pt')  # Load an official Detect model

# Perform tracking with the model
results = model.track(source='traffic.mp4', show=True, tracker="bytetrack.yaml")  # Tracking with default tracker
results = model.track(source='traffic2.mp4', show=True, tracker="bytetrack.yaml")  # Tracking with default tracker
results = model.track(source='traffic3.mp4', show=True, tracker="bytetrack.yaml")  # Tracking with default tracker