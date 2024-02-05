from pytube import YouTube
import cv2

# YouTube video URL
url = "https://youtube.com/shorts/1f8waQSy6Ag?feature=share"
#url = "https://youtu.be/UffhcOlLxPg?si=5YuV1uMXpdcJL0J4"

# Get YouTube video
yt = YouTube(url)
yt_stream = yt.streams.filter(file_extension='mp4').first()

# Open a video capture object using the camera and the YouTube video stream
vid = cv2.VideoCapture()
vid.open(yt_stream.url)

print("check:", vid.isOpened())

# Loop to capture frames from the video stream
while vid.isOpened():
    # Read a frame from the video stream
    ret, frame = vid.read()

    # Check if the frame is successfully captured
    if ret == True:
        # Resize the frame to (650, 650)
        frame = cv2.resize(frame, (650, 650))

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale and color frames
        cv2.imshow("Gray Frame", gray)
        cv2.imshow("Colorframe", frame)

        # Break the loop if the "b" key is pressed
        if cv2.waitKey(1) & 0xFF == ord("b"):
            break
    else:
        break

# Release the video capture object and close all windows
vid.release()
cv2.destroyAllWindows()







