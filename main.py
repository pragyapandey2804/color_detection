#using hsv colorspace to detect yellow color or any other color of choice
import cv2 
from PIL import Image

from util import get_limit

yellow = [0, 255, 255] # yellow in bgr

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlimit, upperlimit = get_limit(colors=yellow) # fetching h limits to stay in range of yellow color

    mask = cv2.inRange(hsv_image, lowerlimit, upperlimit) # it'll mask everycolor except the yellow and present it in white and rest in black

    mask_ = Image.fromarray(mask) # converting image from np array to pillow 

    bbox = mask_.getbbox() # making bounding boxes

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

