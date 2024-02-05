import cv2

#read from web camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print("check:", cam.isOpened())

#define the codec and create a VideoWriter object for the output
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480), 0)

#loop to capture frames from the camera
while cam.isOpened():
    #read a frame from the camera
    ret, frame = cam.read()

    #check if the frame is successfully captured
    if ret == True:
        #convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #write the grayscale frame to the output video file
        output.write(gray)

        #display the grayscale and color frames
        cv2.imshow("Gray Frame", gray)
        cv2.imshow("Colorframe", frame)

        #break the loop if the "b" key is pressed
        if cv2.waitKey(1) & 0xFF == ord("b"):
            break
    else:
        break

#release the camera and output video objects, and close all windows
cam.release()
output.release()
cv2.destroyAllWindows()
