# 导入必要的库
import pyttsx3  # 用于本地语音合成
from gtts import gTTS  # 用于在线语音合成
import os  # 用于操作系统命令

# 创建一个语音引擎对象
engine = pyttsx3.init()

# 设置语言和速度
language = "zh"  # 中文
speed = 150  # 语速

# 设置语音引擎的属性
engine.setProperty("voice", language)
engine.setProperty("rate", speed)

# 获取可用的声音列表
voices = engine.getProperty("voices")

# 定义一个函数，用于将文本转换为语音并播放（本地）
def speak_local(text, voice):
    engine.setProperty("voice", voices[voice].id)  # 根据用户选择的声音设置语音引擎的属性
    engine.say(text)  # 将文本传递给语音引擎
    engine.runAndWait()  # 等待语音合成完成并播放

# 定义一个函数，用于将文本转换为语音并播放（在线）
def speak_online(text):
    tts = gTTS(text=text, lang=language)  # 创建一个gTTS对象，将文本和语言传递给它
    filename = "temp.mp3"  # 定义一个临时文件名，用于保存语音文件
    tts.save(filename)  # 将语音文件保存到临时文件中
    os.system(f"start {filename}")  # 使用操作系统命令打开临时文件并播放

# 定义一个函数，用于显示可用的声音列表并获取用户选择的声音
def choose_voice():
    print("请选择你想要的声音：")
    for i in range(len(voices)):  # 遍历可用的声音列表
        print(f"{i+1}. {voices[i].name}")  # 打印每个声音的序号和名称
    while True:
        choice = input("> ")  # 获取用户输入的选择
        try:
            voice = int(choice) - 1  # 将用户输入的选择转换为整数，并减一得到对应的索引值
            if voice in range(len(voices)):  # 如果索引值在可用的声音列表范围内，返回索引值
                return voice
            else:  # 否则，提示用户输入无效，并重新输入
                print("请输入有效的序号。")
        except:  # 如果用户输入的选择不能转换为整数，提示用户输入无效，并重新输入
            print("请输入有效的序号。")

# 定义一个函数，用于读取文本文件并返回文件内容
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:  # 使用utf-8编码打开文本文件
        text = f.read()  # 读取文件内容并赋值给text变量
    return text  # 返回文件内容

# 定义一个主函数，用于获取用户输入的文本或文件名并调用speak函数
def main():
    print("欢迎使用文本AI朗读器！")
    print("请输入你想朗读的文本，或者输入一个文本文件名，或者输入q退出。")
    print("请选择你想要使用的语音合成方式：1. 本地 2. 在线")
    while True:
        mode = input("> ")  # 获取用户输入的模式
        try:
            mode = int(mode)  # 将用户输入的模式转换为整数
            if mode in [1, 2]:  # 如果模式是1或2，跳出循环
                break
            else:  # 否则，提示用户输入无效，并重新输入
                print("请输入有效的序号。")
        except:  # 如果用户输入的模式不能转换为整数，提示用户输入无效，并重新输入
            print("请输入有效的序号。")
    while True:
        input_text = input("> ")  # 获取用户输入的文本或文件名
        if input_text == "q":  # 如果用户输入q，退出程序
            break
        elif input_text.endswith(".txt"):  # 如果用户输入以.txt结尾，认为是一个文本文件名，调用read_file函数读取文件内容，并赋值给text变量
            text = read_file(input_text)
        else:  # 否则，认为是一个文本，直接赋值给text变量
            text = input_text
        if mode == 1:  # 如果模式是1，表示使用本地语音合成
            voice = choose_voice()  # 调用choose_voice函数获取用户选择的声音
            speak_local(text, voice)  # 调用speak_local函数将文本转换为语音并播放（本地）
        elif mode == 2:  # 如果模式是2，表示使用在线语音合成
            speak_online(text)  # 调用speak_online函数将文本转换为语音并播放（在线）

# 调用主函数
if __name__ == "__main__":
    main()
