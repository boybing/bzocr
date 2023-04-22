#encoding:utf-8

import sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('SIMSUN-Bold', r'./SIMSUN.ttf'))

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# 导入pypinyin库
from pypinyin import pinyin, Style

# 定义一些常量
PAGE_WIDTH, PAGE_HEIGHT = A4 # A4纸的宽高
MARGIN = 10 * mm # 边距
FONT_SIZE = 45 # 字体大小
FONT_NAME = "SIMSUN-Bold" # 字体名称
BOLD_FONT_NAME = FONT_NAME # 加粗字体名称
LINE_HEIGHT = FONT_SIZE * 2.0 # 行高
WORD_SPACING = 25 # 单词间距

# 定义一些函数
def draw_text(canvas, x, y, text, font_name, font_size):
    """在画布上绘制文本"""
    canvas.setFont(font_name, font_size)
    canvas.drawString(x, y, text)

def draw_pinyin(canvas, x, y, text, font_name, font_size):
    """在画布上绘制拼音"""
    canvas.setFont(font_name, font_size * 0.8)
    canvas.drawString(x + font_size * 0.2, y + font_size * 0.8+30, text)

def draw_word(canvas, x, y, word):
    """在画布上绘制一个单词及其拼音"""
    # 使用pypinyin库获取拼音，style=Style.TONE3表示用数字表示声调
    pinyin_list = pinyin(word)
    # 拼接拼音列表为字符串，用空格分隔
    pinyin_str = " ".join([item[0] for item in pinyin_list])
    draw_text(canvas, x, y, word, BOLD_FONT_NAME, FONT_SIZE)
    draw_pinyin(canvas, x, y, pinyin_str, FONT_NAME, FONT_SIZE-20)

def new_page(canvas):
    """创建一个新的页面"""
    canvas.showPage()
    canvas.translate(MARGIN, MARGIN) # 设置原点为左下角的边距处

def to_PDF(string):
    # 替换空格，回车，换行等字符为空字符串
    string = string.replace(" ", "").replace("\n", "").replace("\r", "")
    # 按照空字符串连接
    string = "".join(string)
    # 转换为数组
    array = list(string)
    # 打印结果
    print(array)

    # 创建一个canvas对象，指定文件名和纸张大小
    c = canvas.Canvas("m.pdf", pagesize=A4)

    # 设置原点为左下角的边距处
    c.translate(MARGIN, MARGIN)

    # 定义一些假数据，每个元素是一个汉字
    words = array 

    # 去除每个元素的空格
    words = [word.strip() for word in words] # 使用strip函数
    # 或者
    words = [word.replace(" ", "") for word in words] # 使用replace函数

    # 初始化一些变量，用于记录当前的位置和单词数
    x = -12
    y = PAGE_HEIGHT - MARGIN - LINE_HEIGHT -25 # 减去两个行高
    word_count = 0

    # 遍历每个单词，绘制在画布上，并更新位置和单词数
    for word in words:
        draw_word(c, x, y, word)
        x += FONT_SIZE + WORD_SPACING # 横向移动一个字的宽度加上单词间距
        word_count += 1 # 单词数加一
        if word_count == 64: # 如果单词数达到72，换页并重置位置和单词数
            new_page(c)
            x =  -12
            y = PAGE_HEIGHT - MARGIN - LINE_HEIGHT
            word_count = 0
        elif x > PAGE_WIDTH - MARGIN - FONT_SIZE: # 如果横向超出边界
        # 如果横向超出边界，换行并重置横坐标
            x =  -12
            y -= LINE_HEIGHT # 纵向移动一个行高

    # 保存PDF文件
    c.save()
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        string = sys.argv[1]
        filtered_string = re.sub(r'[^\u4e00-\u9fff]+', '', string)
        return filtered_string
        to_PDF(filtered_string)
    else:
        print("请提供一个字符串作为参数")
