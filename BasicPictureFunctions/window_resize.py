import cv2

cv2.namedWindow("Clone")
img = cv2.imread("clone.jpg")

# resize function
img = cv2.resize(img, (640, 480))

cv2.imshow("Clone", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
