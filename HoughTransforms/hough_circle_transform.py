import cv2
import numpy as np

coins = cv2.imread("coins.jpg")
# since the shapes are not clear in this picture, our rate of getting results is poor
balls = cv2.imread("balls.jpg")

coins_gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
balls_gray = cv2.cvtColor(balls, cv2.COLOR_BGR2GRAY)

coins_blur = cv2.medianBlur(coins_gray, 5)
balls_blur = cv2.medianBlur(balls_gray, 5)

# cv2.HOUGH_GRADIENT -> detection method
# 1 -> resolution ratio
# coins_blur.shape[0] / 4 -> minimum distance between detected circles
# param1(gradient), param2(threshold) -> method-specific defined parameters
circle_Coins = cv2.HoughCircles(coins_blur, cv2.HOUGH_GRADIENT, 1, coins.shape[0] / 4, param1=200, param2=10,
                                minRadius=15, maxRadius=89)

circles_Balls = cv2.HoughCircles(balls_blur, cv2.HOUGH_GRADIENT, 1, balls.shape[0] / 4, param1=200, param2=10,
                                 minRadius=15, maxRadius=89)

if circle_Coins is not None:
    circle_Coins = np.uint16(np.around(circle_Coins))
    for i in circle_Coins[0, :]:
        cv2.circle(coins, (i[0], i[1]), i[2], (0, 255, 0), 2)

if circles_Balls is not None:
    circles_Balls = np.uint16(np.around(circles_Balls))
    for i in circles_Balls[0, :]:
        cv2.circle(balls, (i[0], i[1]), i[2], (0, 255, 0), 2)

cv2.imshow("Coins", coins)
cv2.imshow("Balls", balls)
cv2.waitKey(0)
cv2.destroyAllWindows()
