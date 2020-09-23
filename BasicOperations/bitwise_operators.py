import cv2

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow("First", img1)
cv2.imshow("Second", img2)
cv2.imshow("And", bit_and)
cv2.imshow("Or", bit_or)
cv2.imshow("Xor", bit_xor)
cv2.imshow("Img1 Not", bit_not)
cv2.imshow("Img2 Not", bit_not2)

cv2.waitKey(0)
cv2.destroyAllWindows()
