import cv2

img = cv2.imread("face.png")
face_cascade = cv2.CascadeClassifier("frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# will give the location of the faces on the picture
# 1.3 -> scaling value
# 7 -> in how many different windows we want it to find faces
faces = face_cascade.detectMultiScale(gray, 1.3, 7)
# There are 4 parameters in the 'faces',
# the first 2 are the upper left coordinate and the other 2 are height and width.

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
