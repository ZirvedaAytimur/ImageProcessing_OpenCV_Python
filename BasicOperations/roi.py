# roi: region of interest
import cv2

img = cv2.imread("clone.jpg")

roi = img[30:200, 210:350]

cv2.imshow("Clone", img)
cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
