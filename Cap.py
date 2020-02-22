import numpy as np
import cv2

Image = cv2.VideoCapture(0)
Key = cv2.waitKey(20)

while(True):
    ret, frame = Image.read()
    cv2.imshow("Smile",frame)
    cv2.imwrite('abs.jpg', frame)
    Image.release()
    break

cv2.destroyAllWindows()
