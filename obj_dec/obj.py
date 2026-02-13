import cv2
import time
from ultralytics import YOLO

# -----------------------------------
# 1. Load YOLOv8 Model (More Accurate)
# -----------------------------------
# Use yolov8s.pt for better accuracy (slower but more precise)
model = YOLO("yolov8s.pt")

# -----------------------------------
# 2. Video Source
# -----------------------------------
video_source = 0  # 0 = webcam
cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print("Error: Could not open video source")
    exit()

# Get video properties for saving
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = 20

# Save output video
out = cv2.VideoWriter(
    "output_tracking.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (frame_width, frame_height)
)

prev_time = 0

# -----------------------------------
# 3. Processing Loop
# -----------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection + tracking
    results = model.track(
        frame,
        persist=True,
        conf=0.5,        # Higher confidence = more accurate
        iou=0.5          # Better box overlap control
    )

    boxes = results[0].boxes

    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            track_id = int(box.id[0]) if box.id is not None else 0

            label = f"{model.names[cls]} ID:{track_id} {conf:.2f}"

            # Draw rectangle
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

    # ---------------- FPS Calculation ----------------
    current_time = time.time()
    fps_value = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    cv2.putText(frame, f"FPS: {int(fps_value)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2)

    # Show frame
    cv2.imshow("Advanced Object Detection & Tracking", frame)

    # Save frame
    out.write(frame)

    # Stop with Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------------
# 4. Cleanup
# -----------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()