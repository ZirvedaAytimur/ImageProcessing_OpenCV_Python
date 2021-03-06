import cv2
import numpy as np

ellipse = np.zeros((512, 512, 3), np.uint8) + 255
cv2.ellipse(ellipse, (256, 256), (60, 80), 0, 0, 360, (0, 0, 255), -1)

rectangle = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(rectangle, (128, 128), (360, 360), (150, 200, 14), -1)

add = cv2.add(ellipse, rectangle)

cv2.imshow("Ellipse", ellipse)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Add", add)

cv2.waitKey(0)
cv2.destroyAllWindows()
