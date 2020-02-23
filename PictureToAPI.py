import os
from google.cloud import vision
import cv2
import io

def getImageAnnotation(pics):
    credential_path = "C:/Users/rebec/github/HackHERS2020/HackHERS2020-a2ece6616d68.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
    for pic in pics:
        with io.open(pic, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)
        response = client.face_detection(image=image)
        faces = response.face_annotations

        for face in faces:
            return [likelihood_name[face.anger_likelihood], likelihood_name[face.joy_likelihood], likelihood_name[face.surprise_likelihood], likelihood_name[face.sorrow_likelihood]]

# pics = ["C:/Users/rebec/github/HackHERS2020/abs.jpg"]

#pics = ["C:/Users/rebec/github/HackHERS2020/stark.jpg", "C:/Users/rebec/github/HackHERS2020/media/angryHulk.jpg"]

#getImageAnnotation(pics)
