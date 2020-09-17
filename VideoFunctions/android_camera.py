import cv2
import numpy as np
import requests

# download ip webcam and start server
# after that write //shot.jpg and take a picture
url = "http://192.168.1.3:8080//shot.jpg"

while True:
    img_resp = requests.get(url)
    # We are writing this because we will retrieve the captured image from memory again.
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    # Bring it to the screen in color
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640,480))

    cv2.imshow("Android Camera", img)

    # Shorter way to exit if press 'esc'
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
