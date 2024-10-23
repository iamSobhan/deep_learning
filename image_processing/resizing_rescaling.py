import cv2


#read the image
image = cv2.imread("cats.jpg")

#resize the image
resized_image1 = cv2.resize(image, (500, 500))

#display the resized image
cv2.imshow("Resized Image1", resized_image1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#Resizing by scaling factor

#resize the image by scaling
scale_percent = 50  # scaling by 50%
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

#resize image
resized_image2 = cv2.resize(image, dim)

#display the resized image
cv2.imshow("Resized Image2", resized_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
#Resizing Video Frames

#Open a video file
cap = cv2.VideoCapture("dog.mp4")

#checking if the video is opened successfully
if not cap.isOpened():
    print("Error: Could not open the video.")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

        #resize the frame
        scale_percent = 50
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)

        resized_frame = cv2.resize(frame, dim)

        #display the resized frame
        cv2.imshow("Resized Frame", resized_frame)

        if cv2.waitKey(50) & 0xFF == ord("b"):
            break

cap.release()
#cv2.waitKey(0)
cv2.destroyAllWindows()
"""