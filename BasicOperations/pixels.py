import cv2

img = cv2.imread("clone.jpg")

# shows the size of the picture
dimension = img.shape
print(dimension)

# access color in selected pixel
color = img[420, 500]
print("BGR: ", color)

# find the blue ratio
blue = img[420, 500, 0]
print("Blue: ", blue)

# find the green ratio
green = img[420, 500, 1]
print("Green: ", green)

# find the red ratio
red = img[420, 500, 2]
print("Red: ", red)

# change the color of the pixel
img[420, 500, 0] = 250
print("New blue: ", img[420, 500, 0])

# change the color of the pixel with item
blue1 = img.item(150, 200, 0)
print("Blue1: ", blue1)
img.itemset((150, 200, 0), 172)
print("New blue1: ", img[150, 200, 0])

cv2.imshow("Clone Soldier", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
