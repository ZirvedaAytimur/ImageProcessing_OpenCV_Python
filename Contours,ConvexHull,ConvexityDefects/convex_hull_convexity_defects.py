import cv2

img = cv2.imread("star.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

# when false returns the indices of the values from convexHull
hull = cv2.convexHull(cnt, returnPoints=False)

defects = cv2.convexityDefects(cnt, hull)

for i in range(defects.shape[0]):
    # s = start point
    # e = end point
    # f = farthest point
    # d = distance
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])

    cv2.line(img, start, end, (0, 255, 255), 2)
    cv2.circle(img, far, 5, (0, 255, 0), -1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
