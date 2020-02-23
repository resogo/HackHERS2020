#Cap.py method captureImage()
#PictureToAPI.py method getImageAnnotation(pics)
#makeMatch.py method chooseMatch(data)
#swap2.py method swap(img1_file,img2_file)

from PIL import Image
from Cap import captureImage
from PictureToAPI import getImageAnnotation
from swap import swap

image_file = captureImage()
#anger, joy, surprise, sorrow
picture_data = getImageAnnotation(image_file)
emotion_ratings = picture_data[1]
box_data = picture_data[0]
superhero_file = chooseMatch(emotion_ratings)
result_image =swap(image_file, superhero_file, box_data)
Image.show(result_image)
