import numpy as np
import cv2
import pyautogui as pg

#creating resolution
rs = pg.size()

#prompt user for filename and path to store recording
fn = input("Please Enter any file name and Path")

#fixing the frame rate for the video
fps = 20.0

#defining the codec for video writing
fourcc = cv2.VideoWriter_fourcc(*"XVID")

#creating a VideoWriter object to write the video
output = cv2.VideoWriter(fn, fourcc, fps, rs)

#creating a window to display the live recording
cv2.namedWindow("Live_Recording", cv2.WINDOW_NORMAL)

#resize the window
cv2.resizeWindow("Live_Recording", (600, 400))

#start capturing and recording the screen
while True:
    img = pg.screenshot()  #capture screenshot
    f = np.array(img)  #convert screenshot into array
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)  #convert color format
    output.write(f)  #write frame to the output video
    cv2.imshow("screenshot", f)  #display the screenshot
    if cv2.waitKey(1) == ord("b"):  # Exit loop if "b" key is pressed
        break

#release the output video object and close all windows
output.release()
cv2.destroyAllWindows()