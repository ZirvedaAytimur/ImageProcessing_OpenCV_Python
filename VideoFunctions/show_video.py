import cv2

# use webcam
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture("antalya.mp4")

while True:
    # if it reads frames correctly ret will be True
    ret, frame = cap.read()

    # if video stop break
    if ret == 0:
        break

    # mirror effect
    # 1 y-axis
    frame = cv2.flip(frame, 1)

    # cv2.imshow("Webcam", frame)
    cv2.imshow("Antalya", frame)

    # show every frame 10 ms
    # if press 'q' stop record
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
