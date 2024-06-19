#drawing functions in image

import numpy as np
import cv2

#read the image
img = cv2.imread("C:\\Users\\Sobhan\\PycharmProjects\\image_processing_opencv\\wc12.jpg")

#resize the image
img = cv2.resize(img,(600,700))

#for white screen
#img = np.zeros([512, 512, 3], np.unit8) * 255

#for black screen
#img = np.ones([512, 512, 3], np.unit8) * 255

#line
img = cv2.line(img, (0,0), (150, 150), (50, 166, 168), 5)

#arrow
img = cv2.arrowedLine(img, (0, 100), (200, 200), (168, 115, 50), 6)

#rectangle
img = cv2.rectangle(img, (350, 250), (230, 120), (168, 50, 62), 7)

#circle
img = cv2.circle(img, (400, 130), 60, (127, 50, 22), 4)

#font
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, "Di Maria", (10, 400), font, 5, (168, 27, 50), 10, cv2.LINE_AA )


cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()