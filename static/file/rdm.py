from PIL import Image, ImageDraw, ImageFont
import random

# 定义一个函数，用于生成一个退位减法题
def generate_subtraction():
    # 随机生成两个0到100之间的整数 
    a = random.randint(0, 100)
    b = random.randint(0, 100) 
    # 如果a小于b，交换a和b的值 
    if a < b:
        a, b = b, a
    return f'{a}减{b}', a - b

# 定义一个函数，用于生成一个进位加法题
def generate_addition():
    # 随机生成两个0到100之间的整数 
    a = random.randint(0, 100)
    b = random.randint(0, 100 - a) 
    return f'{a}加{b}', a + b

def rd():
    # 定义两个列表，分别用于存储题目和答案
    problems = []
    answers = []

    # 循环50次，生成50个减法题和50个加法题
    for i in range(2):
        # 调用函数，生成一个减法题和一个加法题
        subtraction_problem, subtraction_answer = generate_subtraction()
        addition_problem, addition_answer = generate_addition()
        
        # 把这两个题目和答案添加到列表中
        problems.extend([subtraction_problem, addition_problem])
        answers.extend([subtraction_answer, addition_answer])

    # 打乱题目和答案的顺序
    combined = list(zip(problems, answers))
    random.shuffle(combined)
    problems[:], answers[:] = zip(*combined)

    # 创建一张空白图片
    img = Image.new('RGB', (500, 500), color='white')
    draw = ImageDraw.Draw(img)

    # 设置字体和字号
    font = ImageFont.truetype('SIMSUN.ttf', 16)

    # 设置起始位置和间距
    x = 10 # 横坐标起始位置
    y = 10 # 纵坐标起始位置
    dy = 20 # 纵坐标间距

    # 循环遍历列表中的每个答案，并打印到图片中
    for i, answer in enumerate(answers):
        # 计算当前位置的纵坐标
        y_pos = y + i * dy 
        # 在当前位置打印一个答案  
        draw.text((x, y_pos), str(answer), fill='black', font=font)

    # 保存图片到本地  
    img.save('answers.png')

    # 打印出所有的题目
    for problem in problems:
        print(problem)
    return problems

if __name__ == '__main__':
    rd()
