import glob
from PIL import Image, ImageDraw, ImageFilter
import pandas
import numpy as np

def swap(img1_file,img2_file, box_data):
    df = pandas.read_csv('./data.csv',encoding="utf-8-sig")
    img1 = Image.open(img1_file)
    img2 = Image.open(img2_file)
    #i=df[df['image_location']==img1_file]
    #j=df[df['image_location']==img2_file]
    #box1 = i['box']
    #box2 = j['box']
    #print(df.at[img1_file,'box'])
    #index = df.index[df['image_location']==img1_file]
    #index = index[0]
    #box1 = df.at[index,'box']
    #box1 = box1.replace(" ","")
    #box1 = box1.strip('[]')
    #corners = np.fromstring(box1, dtype=int, sep=',')
    #print(corners)
    imCrop = img1.crop((box_data[0],box_data[1],box_data[2],box_data[3]))


    # make a copy the image so that
    # the original image does not get affected
    Image2copy = img2.copy()
    #find where to paste
    index2 = df.index[df['image_location']==img2_file]
    index2 = index2[0]
    box2 = df.at[index2,'box']
    box2 = box2.replace(" ","")
    box2 = box2.strip('[]')

    corners2 = np.fromstring(box2, dtype=int, sep=',')
    imCrop2 = img2.crop((corners2[0],corners2[1],corners2[2],corners2[3]))
    #img_size = ((box_data[2]-box_data[0]),box_data[3]-box_data[1])
    img2_size = ((corners2[2]-corners2[0]),corners2[3]-corners2[1])
    imCrop = imCrop.resize(img2_size)
    # paste image giving dimensions
    Image2copy.paste(imCrop, (corners2[0],corners2[1]))
    Image2copy = Image2copy.resize((1556,881))
    # save the image
    Image2copy.save('./media/swapped.jpg')
    return './media/swapped.jpg'
