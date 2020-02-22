import os
from google.cloud import vision
import pandas
import io

def getImageAnnotation(pics):
    credential_path = "C:/Users/rebec/github/HackHERS2020/HackHERS2020-a2ece6616d68.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    img_loc = []
    anger = []
    joy = []
    surprise = []
    sorrow = []
    box = []
    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
    for pic in pics:
        with io.open(pic, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)
        response = client.face_detection(image=image)
        faces = response.face_annotations

        for face in faces:
            img_loc.append(pic)
            anger.append(likelihood_name[face.anger_likelihood])
            joy.append(likelihood_name[face.joy_likelihood])
            surprise.append(likelihood_name[face.surprise_likelihood])
            sorrow.append(likelihood_name[face.sorrow_likelihood])
            vertices = []
            for vertex in face.bounding_poly.vertices:
                vertices.append([vertex.x, vertex.y])
            box.append(vertices)
    df = pandas.DataFrame(data={"image_location": img_loc, "anger": anger, "joy": joy, "surprise": surprise, "sorrow": sorrow, "box": box})
    df.to_csv("./data.csv", sep=',',index=False)
def getFilesInFolder(folder):
    pics = []
    directory = os.fsencode(folder)

    for file in os.listdir(directory):
         filename = os.fsdecode(file)
         if filename.endswith(".jpg"):
             path_str = os.path.join(directory.decode("utf-8"), filename)
             pics.append(path_str)
    print(pics)
    return pics

pics = getFilesInFolder(".\\media")
getImageAnnotation(pics)
