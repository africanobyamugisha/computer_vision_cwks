import cv2
import os

def create_video_from_frames(frame_folder, output_video, frame_rate=30):
    frames = [f for f in sorted(os.listdir(frame_folder)) if f.endswith('.jpg')]
    if not frames:
        print(f"No frames found in {frame_folder}")
        return

    # Get the dimensions of the first frame
    frame = cv2.imread(os.path.join(frame_folder, frames[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    for frame_filename in frames:
        frame_path = os.path.join(frame_folder, frame_filename)
        frame = cv2.imread(frame_path)
        video.write(frame)

    video.release()
    print(f"Video created at {output_video}")

# Create a video from the annotated frames
frame_folder = 'data/frames'
output_video = 'data/annotated_output.avi'
create_video_from_frames(frame_folder, output_video, frame_rate=30)