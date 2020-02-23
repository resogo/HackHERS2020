#Cap.py method captureImage()
#PictureToAPI.py method getImageAnnotation(pics)
#makeMatch.py method chooseMatch(data)
#swap2.py method swap(img1_file,img2_file)

import cv2
from PIL import Image
from Cap import captureImage
from PictureToAPI import getImageAnnotation
from swap2 import swap
from makeMatch import chooseMatch

image_file = [captureImage()]
#image_file = ["./media/stark.jpg"]
#anger, joy, surprise, sorrow
picture_data = getImageAnnotation(image_file)
emotion_ratings = picture_data[1]
box_data = picture_data[0]
superhero_file = chooseMatch(emotion_ratings)
result_image_path =swap(image_file[0], superhero_file, box_data)
result = cv2.imread(result_image_path, -1);
cv2.namedWindow("Smile", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Smile",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow('Smile',result)
cv2.waitKey()
