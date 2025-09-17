import cv2
import numpy as np

cap = cv2.VideoCapture("input_video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("corrupted_video.mp4", fourcc, 30.0, (640, 480))

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Simulate corruption every 50th frame
    if frame_count % 50 == 0:
        corrupted_frame = np.zeros_like(frame)  # Blank frame
        out.write(corrupted_frame)
    else:
        out.write(frame)

    frame_count += 1

cap.release()
out.release()

def is_corrupted(frame, threshold=5):
    # Check if frame is nearly blank (low pixel variance)
    return np.std(frame) < threshold

cap = cv2.VideoCapture("corrupted_video.mp4")
recovered_frames = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if is_corrupted(frame):
        print("⚠️ Corrupted frame detected")
        # Recovery strategy: skip, interpolate, or reuse last good frame
        if recovered_frames:
            recovered_frames.append(recovered_frames[-1])  # Reuse previous
        else:
            recovered_frames.append(np.zeros_like(frame))  # Fallback
    else:
        recovered_frames.append(frame)

cap.release()