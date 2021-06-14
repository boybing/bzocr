#-*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import aircv as ac
import os
import sys

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

def creatPic(pic):
    imsrc = ac.imread(pic)
    imobj = ac.imread("./base/sx.jpg")
    imobs = ac.imread("./base/b.jpg")

    imbig = Image.open(pic)#获取大图片
    imlit = Image.open("./base/sx.jpg")#获取大图片
    imlit3 = Image.open("./base/b.jpg")#获取大图片
    w , h = imbig.size
    w2, h2 = imlit.size
    w3, h3 = imlit3.size

    match_result = ac.find_template(imsrc,imobs,0.2)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    # print('位置1')
    # print(match_result)

    match_result2 = ac.find_template(imsrc,imobj,0.2)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    # print('位置2')
    # print(match_result2)

    filename = pic
    img = Image.open(filename)
    size = img.size
    # print(size)

    box = (0, int(match_result['result'][1])-int(h2//2), w, int(match_result['result'][1])+600)
    # print(box)
    img2 = img.crop(box)
    # region.save('2.jpg')

    box1 = (0, 240, w, int(match_result2['result'][1])-h3)
    # print(box)
    img1 = img.crop(box1)
    # region1.save('1.jpg')

    # img1 = Image.open( "1.jpg")
    w,h=img1.size
    # print(w,h)
    # img1 = img1.convert('RGBA')
    # img2 = Image.open( "2.jpg")
    w2,h2=img2.size
    # print(w2,h2)
    im5 = Image.new('RGB', (img2.width, img2.height-90))
    # im5.paste(img1,(0,0,img1.width,img1.height))
    box = (0, 40, img2.width, img2.height-50)
    # print(box)
    img2 = img2.crop(box)
    im5.paste(img2,(0,0,img2.width,img2.height))
    return im5

path_list=os.listdir(BASE_PATH)
pic1=''
picArr=[]
for filename in path_list:
    if os.path.splitext(filename)[1] == '.jpg':
        pic1=creatPic(filename)
        picArr.append(pic1)

imbg = Image.new('RGB', (pic1.width-120, pic1.height*len(picArr)))
for i in range(len(picArr)):
    if i<=4:
        imbg = Image.new('RGB', (pic1.width-120, pic1.height*len(picArr)))
    elif i<10:
        imbg = Image.new('RGB', (2*(pic1.width-120), pic1.height*5))
    else:
        pass
for i in range(len(picArr)):
    if i<=4:
        imbg.paste(picArr[i],(0,i*pic1.height,pic1.width,i*pic1.height+pic1.height))
        imbg.paste(picArr[i+5],(pic1.width-120,i*pic1.height,pic1.width+pic1.width-120,i*pic1.height+pic1.height))
    else:
        pass
imbg.save('output.png')
        # imbg = Image.new('RGB', (pic1.width-120, pic1.height))
        # imbg.paste(pic1,(0,0,pic1.width,pic1.height))
        # imbg.save(filename+'.png')
        
        # 从保存的路径载入ac
        # imsrc = ac.imread('./'+filename+'.png')
        # img = Image.open('./'+filename+'.png')
        # imobs = ac.imread("./base/b.jpg")
        # imlit = Image.open("./base/b.jpg")#获取大图片
        # 获得裁剪后图片的尺寸
        # w,h=pic1.size
        # w2, h2 = imlit.size
        # match_result = ac.find_template(imsrc,imobs,0.2)
        # box = (0, 0, w, h)
        # img2 = img.crop(box)
        # im2bg = Image.new('RGB', (img2.width, img2.height))
        # imbg.paste(img2,(0,0,img2.width,img2.height))        
        # im2bg.save(filename+'.png') 
        
