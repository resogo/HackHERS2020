import glob
from PIL import Image, ImageDraw, ImageFilter
import pandas
import numpy as np

def swap(img1_file,img2_file):
    df = pandas.read_csv('./data.csv',encoding="utf-8-sig")
    img1 = Image.open(img1_file)
    img2 = Image.open(img2_file)
    #i=df[df['image_location']==img1_file]
    #j=df[df['image_location']==img2_file]
    #box1 = i['box']
    #box2 = j['box']
    #print(df.at[img1_file,'box'])
    index = df.index[df['image_location']==img1_file]
    index = index[0]
    box1 = df.at[index,'box']
    box1 = box1.replace(" ","")
    box1 = box1.strip('[]')
    print(box1)
    corners = np.fromstring(box1, dtype=int, sep=',')
    print(corners)
    print(type(corners))
    imCrop = img1.crop((corners[0],corners[1],corners[2],corners[3]))
    imCrop.save('./media/surprisedThorcropped.jpg')
img1_file = './media/camp.jpg'
img2_file = './media/captainMarvel.jpg'
swap(img2_file,img2_file)
