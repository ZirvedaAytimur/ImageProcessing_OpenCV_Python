import cv2

img = cv2.imread("triangle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

# finding area
area = cv2.contourArea(cnt)
print(area)
M = cv2.moments(cnt)
print(M["m00"])

# finding perimeter
# True means the shape is full
perimeter = cv2.arcLength(cnt, True)
print(perimeter)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
