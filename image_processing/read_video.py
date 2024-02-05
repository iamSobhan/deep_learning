import cv2

#read from a video
video = cv2.VideoCapture("faces01.mp4")

while True:
    #read each frame from the video
    ret, frame = video.read()

    #print frame height and width
    print("Height:", video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Width:", video.get(cv2.CAP_PROP_FRAME_WIDTH))

    #resize the frame and convert it to grayscale
    frame = cv2.resize(frame, (700, 450))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #flip the frame horizontally
    frame = cv2.flip(frame, -1)

    #display the color and gray frames
    cv2.imshow("Colorframe", frame)
    cv2.imshow("Gray Frame", gray)

    #break the loop if "b" key is pressed
    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

#release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()
