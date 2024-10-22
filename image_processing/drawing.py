import cv2
import numpy as np

#blank
blank = np.zeros((512,512,3), dtype = "uint8")
#cv2.imshow("Blank", blank)

#image
blank[150:250, 250:350] = 0,0,255
cv2.imshow("img", blank)

#rectangle
cv2.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -1)
cv2.imshow("Rectangle", blank)

#circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 30, (0,0,255), thickness= -1)
cv2.imshow("Circle", blank)

#line
cv2.line(blank, (50,100), (150,250), (255,255,255), thickness=10)
cv2.imshow("Line", blank)

#text
cv2.putText(blank, "Drawing Shapes", (0,225), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (112,90,0), 2)
cv2.imshow("Text", blank)

#ellipse
cv2.ellipse(blank, (256, 256), (100, 50), 45, 0, 360, (255, 255, 0), thickness = 3)
cv2.imshow("Ellipse", blank)

#polygon
points = np.array([[100, 100], [200, 300], [400, 300], [300, 100]], np.int32)
points = points.reshape((-1, 1, 2))

cv2.polylines(blank, [points], isClosed = True, color=(0, 255, 255), thickness = 3)
cv2.imshow("Polygon", blank)


cv2.waitKey(0)
cv2.destroyAllWindows()