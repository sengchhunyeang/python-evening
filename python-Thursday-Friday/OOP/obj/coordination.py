import cv2
import mediapipe as mp
import pandas as pd

# Initialize MediaPipe pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Store coordinates in a list
all_landmarks = []

# Load video
video_url = 'https://www.facebook.com/share/p/1PZdj2nMzU/'
cap = cv2.VideoCapture(video_url)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB for MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        frame_data = {'frame': frame_count}
        for i, lm in enumerate(landmarks):
            frame_data[f'x_{i}'] = lm.x
            frame_data[f'y_{i}'] = lm.y
            frame_data[f'z_{i}'] = lm.z
            frame_data[f'vis_{i}'] = lm.visibility  # Optional: visibility score
        all_landmarks.append(frame_data)

    frame_count += 1

cap.release()
pose.close()

# Save to CSV
df = pd.DataFrame(all_landmarks)
df.to_csv('pose_coordinates.csv', index=False)
print("✅ Coordinate map saved to pose_coordinates.csv")
