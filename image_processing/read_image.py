import cv2

#reading an image from a location
image1 = cv2.imread("C:\\Users\\Sobhan\\Documents\\OneDrive\\Pictures\\wc\\wc67.jpg", 1)
#height & width
image1 = cv2.resize(image1,(1200, 800))
cv2.imshow("World Cup", image1)
print("\n Colour Image",image1)

#for grayscale image
image2 = cv2.imread("C:\\Users\\Sobhan\\Documents\\OneDrive\\Pictures\\wc\\wc67.jpg", 0)
cv2.imshow("World Cup", image2)
print("\n Gray Scale Image",image2)

#orginal/unchanged image
image3 = cv2.imread("C:\\Users\\Sobhan\\Documents\\OneDrive\\Pictures\\wc\\wc67.jpg", -1)
image3 = cv2.resize(image1,(1300, 900))
cv2.imshow("World Cup", image3)
print("\n Orginal Image",image3)

cv2.waitKey(0)
cv2.destroyAllWindows()
