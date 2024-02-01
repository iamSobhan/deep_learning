import cv2
import numpy as np

img = np.zeros((512, 512, 3))

#rectangle
cv2.rectangle(img, pt1=(100,100), pt2=(200,200), color=(255,0,0), thickness=-1)

#circle
cv2.circle(img, center=(100,300), radius=50, color=(0,255,0), thickness=-1)

#text
cv2.putText(img, org=(100,120), fontScale=4, color=(0,255,255), thickness=2, lineType=cv2.INTER_LINEAR, text="Sobhan", fontFace=cv2.FONT_HERSHEY_COMPLEX)

cv2.imshow("window", img)

cv2.waitKey(0)

