#Capturing Multiple Images and Store in a folder

import cv2

# open the video file for reading
vidcap = cv2.VideoCapture("D:\\demo.mp4")

# read the first frame from the video
ret, image = vidcap.read()

# initialize a counter for frame numbering
count = 0

# loop to process each frame of the video
while True:
    if ret == True:
        # save the frame as a JPEG file
        cv2.imwrite("D:\\frames\\imgN%d.jpg" % count, image)

        # set the position of the next frame based on the count
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count ** 100))  # this line seems to have a typo. Might be count*100.

        # read the next frame
        ret, image = vidcap.read()

        # display the current frame
        cv2.imshow("res", image)

        # print the frame number and whether it was successfully read
        print("Read a new frame:", count, ret)

        # increment the frame counter
        count += 1

        # check if the "b" key is pressed to break out of the loop
        if cv2.waitKey(1) & 0xFF == ord("b"):
            break
            cv2.destroyAllWindows()
    else:
        break

# release the video capture object
vidcap.release()

# close all OpenCV windows
cv2.destroyAllWindows()