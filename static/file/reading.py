# 导入必要的库
from gtts import gTTS  # 用于在线语音合成
import os  # 用于操作系统命令

# 设置语言和速度
language = "zh"  # 中文
speed = 150  # 语速

# 定义一个函数，用于将文本转换为语音并播放（在线）
def speak_online(text):
    tts = gTTS(text=text, lang=language)  # 创建一个gTTS对象，将文本和语言传递给它
    filename = "temp.mp3"  # 定义一个临时文件名，用于保存语音文件
    tts.save(filename)  # 将语音文件保存到临时文件中

# 定义一个函数，用于读取文本文件并返回文件内容
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:  # 使用utf-8编码打开文本文件
        text = f.read()  # 读取文件内容并赋值给text变量
    return text  # 返回文件内容

# 定义一个主函数，用于获取用户输入的文本或文件名并调用speak函数
def creatMp3(input_text):

    if input_text == "q":  # 如果用户输入q，退出程序
        pass
    elif input_text.endswith(".txt"):  # 如果用户输入以.txt结尾，认为是一个文本文件名，调用read_file函数读取文件内容，并赋值给text变量
        text = read_file(input_text)
    else:  # 否则，认为是一个文本，直接赋值给text变量
        text = input_text
        speak_online(text)  # 调用speak_online函数将文本转换为语音并播放（在线）

# 调用主函数
if __name__ == "__main__":
    creatMp3('111')
