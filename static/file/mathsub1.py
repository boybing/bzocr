#encoding:utf-8
import random
# 导入reportlab模块，用于打印PDF文件
from reportlab.pdfgen import canvas

# 定义一个函数，用于生成一个退位减法题
def generate_subtraction():
    # 随机生成两个0到20之间的整数 
    a = random.randint(10, 20)
    b = random.randint(1, 9) 
    # 如果a小于b，交换a和b的值 
    if a < b:
      a, b = b, a
    return f'{a} - {b} ='

# 定义一个列表，用于存储已经生成的减法题
problems = []

# 循环100次，生成100个减法题
for i in range(100):
  # 调用函数，生成一个减法题
  problem = generate_subtraction()
  # # 如果这个减法题已经在列表中，重新生成一个
  # while problem in problems:
  #   problem = generate_subtraction()
  # 把这个减法题添加到列表中
  problems.append(problem)

# 创建一个A4纸大小的PDF文件
c = canvas.Canvas("m.pdf", pagesize=(595.27,841.89))

# 设置字体和字号
c.setFont("Helvetica", 16)

# 设置起始位置和间距
x = 50 # 横坐标起始位置
y = 800 # 纵坐标起始位置
dx = 100 # 横坐标间距
dy = -30 # 纵坐标间距

# 循环遍历列表中的每个减法题，并打印到PDF文件中
for i, problem in enumerate(problems):
  # 计算当前位置的横坐标和纵坐标
  x_pos = x + (i % 5) * dx # 每5列换行
  y_pos = y + (i // 5) * dy # 每20行换页
  # 如果纵坐标小于50，创建一个新的页面，并重置纵坐标为800
  if y_pos < 50:
    c.showPage()
    y_pos = 800 
  # 在当前位置打印一个减法题  
  c.drawString(x_pos, y_pos, problem)

# 结束PDF文件并保存到本地  
c.save()