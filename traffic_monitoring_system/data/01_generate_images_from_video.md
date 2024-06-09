# Creating Images from Video

From the fact taht we are going to use LabelImg whic is primarily designed for labeling images, not videos, we shall need to extract frames from the video and then use LabelImg to annotate those frames.

## Steps 

1. **Extract Frames from the Video**: We shall use OpenCV to extract frames from the video.
2. **Annotate the Extracted Frames with LabelImg**: Use LabelImg to label the extracted frames.
3. **(Optional) Convert Annotations Back to Video Format**: If needed, you can later use the annotations with the original video frames, i will do this just to experiment as a **Video Labelling**

### Step 1: Extract Frames from the Video

[HERE](traffic_monitoring_system\data\extract_frames.py) is a Python script using OpenCV to extract frames from your video:

### Step 2: Annotate the Extracted Frames with LabelImg
Use LabelImg to annotate the frames. Save the annotations in the desired format (e.g., Pascal VOC XML or YOLO format) as explained [HERE](traffic_monitoring_system\data\02 Setting Up LabelImg.md)

### Step 3 (My Experimentation): Convert Annotations Back to Video Format

A script to overlay the annotations on the video frames and reassemble them into a video. 