#Cap.py method captureImage()
#PictureToAPI.py method getImageAnnotation(pics)
#swap.py method swap(img1_file,img2_file)

from Cap import captureImage
from PictureToAPI import getImageAnnotation
from swap import swap

image_file = captureImage()
#anger, joy, surprise, sorrow
emotion_ratings = getImageAnnotation(image_file)
