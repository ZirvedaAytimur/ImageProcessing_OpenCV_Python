import cv2
import numpy as np

img = cv2.imread("helicopter.jpg", 0)

kernel = np.ones((5, 5), np.uint8)

# thinning
# erosion = cv2.erode(img, kernel, iterations=1)

# thicker
# dilation = cv2.dilate(img, kernel, iterations=1)

# removes the distortions in the picture
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# elimination of incompatibilities
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# the picture is drawn out and the rest of the places are left black
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# the object darkens and the outer parts remain white.
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original", img)
# cv2.imshow("Erosion", erosion)
# cv2.imshow("Dilation", dilation)
# cv2.imshow("Opening", opening)
# cv2.imshow("Closing", closing)
# cv2.imshow("Gradient", gradient)
cv2.imshow("Tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
