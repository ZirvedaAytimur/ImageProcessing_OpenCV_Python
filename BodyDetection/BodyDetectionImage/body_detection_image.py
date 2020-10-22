import cv2

img = cv2.imread("body.jpg")

# most of body detection haar cascades don't work well
upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

upper = upper_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in upper:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
