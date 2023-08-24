from mtcnn import MTCNN #mtcnn Multi-task Cascaded Convolutional Networks

#importing opencv
import cv2

#creating an instance of the MTCNN detector
detector = MTCNN()

#loading an image
image = cv2.imread("images/messi_wc.jpg")

#detect faces in the image
faces = detector.detect_faces(image)
print(faces)

#Iterate through detected faces
for i in faces:
    x, y, width, height = i["box"]

    #Extract facial keypoints
    left_eyeX, left_eyeY = i["keypoints"]["left_eye"]
    right_eyeX, right_eyeY = i["keypoints"]["right_eye"]
    noseX, noseY = i["keypoints"]["nose"]
    mouth_leftX, mouth_leftY = i["keypoints"]["mouth_left"]
    mouth_rightX, mouth_rightY = i["keypoints"]["mouth_right"]

    #Draw rectangles and circles around the detected face and facial keypoints
    cv2.circle(image, center=(left_eyeX, left_eyeY), color=(255, 0, 0), thickness=3, radius=2)
    cv2.circle(image, center=(right_eyeX, right_eyeY), color=(255, 0, 0), thickness=3, radius=2)
    cv2.circle(image, center=(noseX, noseY), color=(255, 0, 0), thickness=3, radius=2)
    cv2.circle(image, center=(mouth_leftX, mouth_leftY), color=(255, 0, 0), thickness=3, radius=2)
    cv2.circle(image, center=(mouth_rightX, mouth_rightY), color=(255, 0, 0), thickness=3, radius=2)
    cv2.rectangle(image, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 0), thickness=3)


#Display the image with detected faces and keypoints
cv2.imshow("window", image)

cv2.waitKey(0)





