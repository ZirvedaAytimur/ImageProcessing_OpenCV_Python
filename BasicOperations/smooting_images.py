import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

# blur the image
# Blur, gaussian, median only work with positive odd numbers
blur = cv2.blur(img_filter, (11, 11))

gaussian_blur = cv2.GaussianBlur(img_filter, (6, 5), cv2.BORDER_DEFAULT)

median_blur = cv2.medianBlur(img_median, 5)

bilateral = cv2.bilateralFilter(img_bilateral, 9, 95, 95)

cv2.imshow("Original", img_bilateral)
# cv2.imshow("Blur", blur)
# cv2.imshow("Gaussian Blur", gaussian_blur)
# cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Filter", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()
