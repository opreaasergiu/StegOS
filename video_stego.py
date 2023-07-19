import cv2

def add_frame_to_video(input_video, output_video, frame_to_add, position):
    # Read the input video
    cap = cv2.VideoCapture(input_video)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create a new video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

    # Iterate over the frames of the input video
    for frame_index in range(total_frames):
        ret, frame = cap.read()

        if not ret:
            break

        # Check if it's the desired position to insert the new frame
        if frame_index == position:
            # Resize the new frame to match the video frame size
            frame_to_add_resized = cv2.resize(frame_to_add, (frame_width, frame_height))

            # Add the new frame to the video
            frame_with_added_frame = cv2.add(frame, frame_to_add_resized)

            # Write the modified frame to the output video
            out.write(frame_with_added_frame)

        # Write the original frame to the output video
        else:
            out.write(frame)

    # Release the video capture and video writer
    cap.release()
    out.release()

    print("Frame added to the video. Saved output video as", output_video)

# # Example usage: Add a frame to the video at position 100
# input_video = 'input_video.mp4'
# output_video = 'output_video.mp4'
# frame_to_add = cv2.imread('frame_to_add.jpg')
# position = 100
#
# add_frame_to_video(input_video, output_video, frame_to_add, position)


# Read the video and capture a frame
# cap = cv2.VideoCapture('video.mp4')
# ret, frame = cap.read()
#
# # Convert the frame to RGB format
# frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
# # Create an Image object from the frame data
# image = Image.fromarray(frame_rgb)

# Display the image
#image.show()

def extract_frame_from_video(video_path, frame_index):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if frame_index >= total_frames:
        raise ValueError('Invalid frame index')

    # Set the position of the video to the desired frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    # Read the frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        raise ValueError('Error reading frame')

    # Display or process the frame as needed
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)
    cv2.imwrite("outputframe.png", frame)
    # Release the video capture
    cap.release()

# Example usage: Extract frame at index 100 from the video
#extract_frame_from_video('cover_video.mp4', 0)



