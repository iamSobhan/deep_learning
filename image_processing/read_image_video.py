import cv2 as cv

#reading image
img = cv.imread("cats.jpg")
cv.imshow("Cats", img)


#reading videos
capture = cv.VideoCapture("dog.mp4")

while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow("Video", frame)
        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    else:
        break


cv.waitKey(0)
capture.release()
cv.destroyAllWindows()