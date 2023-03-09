# encoding:utf-8
import PIL.Image, PIL.ImageDraw, PIL.ImageFont
import cv2
import numpy as np
import os
import json

from pip import main

# 定义一个对外方法，接收数组、文字大小、显示时间作为参数，并生成视频文件
def generate_video(strings, font_size, duration):
    BASE_PATH=os.path.dirname(os.path.abspath(__file__)) 
    # 创建一个空列表，存储生成的图片对象 
    images = []

    # 遍历字符串数组，并调用string_to_image函数将每个字符串转换为图片对象，并添加到列表中 
    for string in strings:
        image = string_to_image(string, font_size)
        images.append(image)

    # 调用images_to_video函数将图片列表转换为视频，并保存为output.mp4文件 
    images_to_video(images,duration,BASE_PATH+"/output.mp4") 

# 定义一个函数，将字符串转换为图片，并返回图片对象
def string_to_image(string, font_size):
    BASE_PATH=os.path.dirname(os.path.abspath(__file__)) 
    font_path = BASE_PATH+"/arial.ttf" # 字体文件路径
    bg_color = (0, 0, 0) # 背景颜色，RGB格式
    image_size = (640, 480) # 图片尺寸，宽度和高度
    # 创建一个空白的图片对象，使用背景颜色填充
    image = PIL.Image.new("RGB", image_size, bg_color)
    # 创建一个绘图对象，用于在图片上绘制文字
    draw = PIL.ImageDraw.Draw(image)
    # 创建一个字体对象，用于指定文字的字体和大小
    font = PIL.ImageFont.truetype(font_path, int(font_size))
    # 计算文字的宽度和高度，并居中对齐
    text_width, text_height = draw.textsize(string, font)
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2
    # 在图片上绘制文字，使用指定的字体和颜色
    draw.text((x, y), string, font=font, fill=(255, 255 ,255))
    # 返回图片对象
    return image

# 定义一个函数，将图片列表转换为视频，并保存为mp4文件
def images_to_video(images,duration,filename):
 
    BASE_PATH=os.path.dirname(os.path.abspath(__file__)) 
    frame_rate = 24 # 视频帧率，每秒显示多少张图片
    # 获取第一张图片的尺寸，并创建一个视频写入对象，指定输出文件名、编码器、帧率和尺寸 
    width,height=images[0].size 
    video_writer=cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*"mp4v"),frame_rate,(width,height))
    
    for image in images:
        # 将每张图片转换为numpy数组，并按BGR顺序排列颜色通道（opencv默认使用BGR格式）
        array=np.array(image)[:,:,::-1]
        # 将每张图片重复写入视频文件多次，根据帧率和持续时间计算重复次数 
        repeat_times=int(frame_rate*duration)
        for _ in range(repeat_times):
            video_writer.write(array)

    video_writer.release() 

def gv():
    with open("array.json", "r") as f:
        lst = json.load(f)
    with open("font_size.json", "r") as f:
        ft = json.load(f)
    with open("interval_time.json", "r") as f:
        it = json.load(f)
    generate_video(lst, int(ft[0]), int(it[0]))

if __name__ == '__main__':
    generate_video(["str","test"], 2, 2)

# import PIL.Image, PIL.ImageDraw, PIL.ImageFont
# import cv2
# import numpy as np
# import os

# BASE_PATH=os.path.dirname(os.path.abspath(__file__)) 
# # 定义一些参数，可以根据需要修改
# font_size = 32 # 文字大小
# font_color = (255, 255, 255) # 文字颜色，RGB格式
# font_path = BASE_PATH+"/arial.ttf" # 字体文件路径
# bg_color = (0, 0, 0) # 背景颜色，RGB格式
# image_size = (640, 480) # 图片尺寸，宽度和高度
# frame_rate = 24 # 视频帧率，每秒显示多少张图片
# duration = 2 # 每张图片显示的时间，单位秒

# # 定义一个函数，将字符串转换为图片，并返回图片对象
# def string_to_image(string):
#     # 创建一个空白的图片对象，使用背景颜色填充
#     image = PIL.Image.new("RGB", image_size, bg_color)
#     # 创建一个绘图对象，用于在图片上绘制文字
#     draw = PIL.ImageDraw.Draw(image)
#     # 创建一个字体对象，用于指定文字的字体和大小
#     font = PIL.ImageFont.truetype(font_path, font_size)
#     # 计算文字的宽度和高度，并居中对齐
#     text_width, text_height = draw.textsize(string, font)
#     x = (image_size[0] - text_width) // 2
#     y = (image_size[1] - text_height) // 2
#     # 在图片上绘制文字，使用指定的字体和颜色
#     draw.text((x, y), string, font=font, fill=font_color)
#     # 返回图片对象
#     return image

# # 定义一个函数，将图片列表转换为视频，并保存为mp4文件
# def images_to_video(images, filename):
#     # 获取第一张图片的尺寸，并创建一个视频写入对象，指定输出文件名、编码器、帧率和尺寸
#     width, height = images[0].size 
#     video_writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*"mp4v"), frame_rate, (width,height))
    
#     for image in images:
#         # 将每张图片转换为numpy数组，并按BGR顺序排列颜色通道（opencv默认使用BGR格式）
#         array = np.array(image)[:,:,::-1]
#         # 将每张图片重复写入视频文件多次，根据帧率和持续时间计算重复次数 
#         repeat_times = int(frame_rate * duration)
#         for _ in range(repeat_times):
#             video_writer.write(array)

#     video_writer.release() 

# # 定义一个数组，存储要输入的字符串 
# strings = ["Hello", "World", "This", "Is", "A", "Test"]

# # 创建一个空列表，存储生成的图片对象 
# images = []

# # 遍历字符串数组，并调用string_to_image函数将每个字符串转换为图片对象，并添加到列表中 
# for string in strings:
#      image = string_to_image(string)
#      images.append(image)

# # 调用images_to_video函数将图片列表转换为视频，并保存为output.mp4文件 
# images_to_video(images,BASE_PATH+"/output.mp4")