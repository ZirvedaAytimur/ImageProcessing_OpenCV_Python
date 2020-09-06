import cv2 as cv
import numpy as np

W = 400
# if thickness is negative means fill it
thickness = -1
# line_4 : 4-connected line
# line_8 : 8-connected line
# line_aa : antialiased line
line_type = 8


def petal(img, angle):
    # cv.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness, lineType, shift)
    cv.ellipse(img,
               (W // 2, W // 2),
               (W // 8, W // 64),
               angle,
               0,
               360,
               (202, 81, 210),
               thickness,
               line_type)


def center_of_flower(img, center):
    # cv.circle(img, center, radius, color, thickness, lineType, shift)
    cv.circle(img,
              center,
              W // 24,
              (0, 255, 255),
              thickness,
              line_type)


def branch(img, start_point, end_point):
    # cv.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
    cv.rectangle(img,
                 start_point,
                 end_point,
                 (24, 101, 39),
                 thickness,
                 line_type)


def cloud(img, center):
    # cv.circle(img, center, radius, color, thickness, lineType, shift)
    cv.circle(img,
              center,
              W // 24,
              (255, 255, 255),
              thickness,
              line_type)


# Window name
flower_window = "Drawing a flower"

# Create black empty images
size = W, W, 3
flower_image = np.zeros(size, dtype=np.uint8)

# Drawing cloud
cloud_center_x = W // 8
cloud_center_y = W // 8
cloud(flower_image, (cloud_center_x, cloud_center_y))
cloud(flower_image, (cloud_center_x + 20, cloud_center_y - 10))
cloud(flower_image, (cloud_center_x + 20, cloud_center_y + 15))
cloud(flower_image, (cloud_center_x + 40, cloud_center_y - 10))
cloud(flower_image, (cloud_center_x + 40, cloud_center_y + 15))
cloud(flower_image, (cloud_center_x + 60, cloud_center_y))

# Drawing branch
branch(flower_image, (195, W // 2), (205, W))

# Drawing petal
petal(flower_image, 90)
petal(flower_image, 0)
petal(flower_image, 45)
petal(flower_image, -45)

# Drawing center of flower
center_of_flower(flower_image, (W // 2, W // 2))

# Displays OpenGL 2D texture in the specified window
cv.imshow(flower_window, flower_image)
# Moves window to the specified position
cv.moveWindow(flower_window, 0, 200)

# Waits for a pressed key
cv.waitKey(0)
# Destroy all the windows
cv.destroyAllWindows()
