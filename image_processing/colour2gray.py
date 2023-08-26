import cv2

#convert image into grayscale
img1 = cv2.imread("C:\\Users\\Sobhan\\Documents\\OneDrive\\Pictures\\wc\\wc12.jpg", 0)
img1 = cv2.resize(img1, (560, 700))
img1 = cv2.flip(img1, 0)
cv2.imshow("Gray Image", img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("b"):
    cv2.destroyAllWindows()

elif k == ord("n"):
    cv2.imwrite("C:\\Users\\Sobhan\\Documents\\OneDrive\\Pictures\\wc\\wc12gray.png", img1)
    cv2.destroyAllWindows()