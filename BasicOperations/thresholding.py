import cv2

# it must be gray scale
img = cv2.imread("helicopter.jpg", 0)

ret, th1 = cv2.threshold(img, 150, 200, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)

cv2.imshow("Image", img)
cv2.imshow("Image-Th1", th1)
cv2.imshow("Image-Th2", th2)
cv2.imshow("Image-Th3", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
