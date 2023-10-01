# 导入必要的库
from gtts import gTTS  # 用于在线语音合成
from pydub import AudioSegment
import os  # 用于操作系统命令
import sys  # 用于获取命令行参数
import rdm

# 设置语言和速度
language = "zh"  # 中文
speed = 150  # 语速

# 定义一个函数，用于将文本转换为语音并播放（在线）
def speak_online(tt):
    # 将文本拆分为多个部分
    # 创建一个空的音频片段
    if tt =='rd':
        answer=rdm.rd()
        combined = AudioSegment.empty()
        for an in answer:
            tts = gTTS(text=an, lang="zh")
            tts.save("temp.mp3")
            speech = AudioSegment.from_mp3("temp.mp3")
            # 将语音添加到组合音频中
            combined += speech
            combined += AudioSegment.silent(duration=5000)
            combined.export("temp.mp3", format="mp3")
    else:
        combined = AudioSegment.empty()
        # 遍历每个部分
        tts = gTTS(text=tt, lang="zh")
        tts.save("temp.mp3")
        #speech = AudioSegment.from_mp3("temp.mp3")
        # 将语音添加到组合音频中
        #combined += speech
        #combined += AudioSegment.silent(duration=3000)
        #tts = gTTS(text='测试测试', lang="zh")
        #tts.save("tst1.mp3")
        #speech = AudioSegment.from_mp3("tst1.mp3")
        #combined += speech
        # 保存组合音频
        #combined.export("temp.mp3", format="mp3")

    

# 定义一个函数，用于读取文本文件并返回文件内容
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:  # 使用utf-8编码打开文本文件
        text = f.read()  # 读取文件内容并赋值给text变量
    return text  # 返回文件内容

# 定义一个主函数，用于获取用户输入的文本或文件名并调用speak函数
def creatMp3(input_text):

    if input_text.endswith(".txt"):  # 如果用户输入以.txt结尾，认为是一个文本文件名，调用read_file函数读取文件内容，并赋值给text变量
        text = read_file(input_text)
    else:  # 否则，认为是一个文本，直接赋值给text变量
        text = input_text

    speak_online(text)  # 调用speak_online函数将文本转换为语音并播放（在线）

# 调用主函数
if __name__ == "__main__":
    if len(sys.argv) > 1:  # 如果有命令行参数
        input_text = sys.argv[1]  # 获取第一个命令行参数作为输入文本
        creatMp3(input_text)  # 调用creatMp3函数并传递输入文本
