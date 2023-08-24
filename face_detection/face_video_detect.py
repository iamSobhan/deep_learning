import cv2
from mtcnn import MTCNN

capture = cv2.VideoCapture(0)

detector = MTCNN()

while True:

    ret, frame = capture.read()
    faces = detector.detect_faces(frame)

    for single_faces in faces:
        x, y, width, height = single_faces["box"]

        left_eyeX, left_eyeY = single_faces["keypoints"]["left_eye"]
        right_eyeX, right_eyeY = single_faces["keypoints"]["right_eye"]
        noseX, noseY = single_faces["keypoints"]["nose"]
        mouth_leftX, mouth_leftY = single_faces["keypoints"]["mouth_left"]
        mouth_rightX, mouth_rightY = single_faces["keypoints"]["mouth_right"]


        cv2.rectangle(frame, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 0), thickness=3)
        cv2.circle(frame, center=(left_eyeX, left_eyeY), color=(255, 0, 0), thickness=3, radius=2)
        cv2.circle(frame, center=(right_eyeX, right_eyeY), color=(255, 0, 0), thickness=3, radius=2)
        cv2.circle(frame, center=(noseX, noseY), color=(255, 0, 0), thickness=3, radius=2)
        cv2.circle(frame, center=(mouth_leftX, mouth_leftY), color=(255, 0, 0), thickness=3, radius=2)
        cv2.circle(frame, center=(mouth_rightX, mouth_rightY), color=(255, 0, 0), thickness=3, radius=2)
        cv2.rectangle(frame, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 0), thickness=3)


    cv2.imshow("front_cam", frame)

    if cv2.waitKey(1) & 0xFF == ord("b"):
        break

cv2.destroyAllWindows()