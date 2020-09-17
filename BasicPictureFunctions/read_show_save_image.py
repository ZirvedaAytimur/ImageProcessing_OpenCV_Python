import cv2

# read the image
# img = cv2.imread("clone.jpg")

# read the image as gray
img = cv2.imread("clone.jpg", 0)

# print matrix of the image
# print(img)

# create resizable window
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# show the image
cv2.imshow("image", img)

# save used image as another image
cv2.imwrite("clone1.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
