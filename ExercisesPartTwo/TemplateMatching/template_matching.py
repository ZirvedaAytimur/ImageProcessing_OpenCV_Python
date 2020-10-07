import cv2
import numpy as np

image = cv2.imread("starwars.jpg")
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread("starwars2.jpg", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
location = np.where(result >= 0.95)

for point in zip(*location[::-1]):
    cv2.rectangle(image, point, (point[0] + w, point[1] + h), (0, 255, 0), 3)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
