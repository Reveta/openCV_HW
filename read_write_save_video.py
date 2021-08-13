import cv2

# Create a video capture object, in this case we are reading the video from a file
vid_capture = cv2.VideoCapture('media/video_new.gif')

if (vid_capture.isOpened() == False):
    print("Error opening the video file")
# Read fps and frame count
else:
    print("Getting video metadata...")
    print(vid_capture.get(0))
    print(vid_capture.get(1))
    print(vid_capture.get(2))
    print(vid_capture.get(3))
    print(vid_capture.get(4))
    print(vid_capture.get(5))
    print()

    # Get frame rate information
    # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
    fps = vid_capture.get(5)
    print('Frames per second : ', fps, 'FPS')

    # Get frame count
    # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
    frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print('Frame count : ', frame_count)

frame_index = 0
while (vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool
    # and the second is frame
    ret, frame = vid_capture.read()

    if ret == True:
        window_name = f"Frame {frame_index}"
        frame_index += 1

        cv2.imshow(window_name, frame)
        # 20 is in milliseconds, try to increase the value, say 50 and observe
        key = cv2.waitKey(1000)
        cv2.destroyWindow(window_name)

        if key == ord('q'):
            break
    else:
        break

# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()