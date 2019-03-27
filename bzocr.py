# encoding: utf-8

from aip import AipOcr

client = AipOcr('15854510', 'DYLmXvRDpqk3B2bnHNtWadbU', 'eYbdehM0QLQIgH0CwiaKleVcDcioDXKG')

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def img(imgg):
    image = imgg

    """ 调用通用文字识别, 图片参数为本地图片 """
    rs=client.basicGeneral(image);
    arrStr=''
    for words in rs['words_result']:
        arrStr=arrStr+'\n'+words['words'].replace(' ','')

    return arrStr