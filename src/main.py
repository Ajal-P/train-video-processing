import cv2
import os

def process_video(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 50 == 0:
            cv2.imwrite(f"{output_folder}/frame_{frame_count}.jpg", frame)

    cap.release()
    print(f"✅ Extracted {frame_count//50} frames to {output_folder}")

if __name__ == "__main__":
    process_video("../data/train.mp4", "../processed/sample_coach")

