# coding=utf-8

from flask import *
import bzocr
import os
import time
import dockerInspect
import bztr
import mp4
import subprocess


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

###
# Routing for your application.
###

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-store"
    return r

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        img = request.files.get('photo').read()
        st=bzocr.img(img)
        with open('st.txt', 'ab') as f:
            f.write(st.encode('utf-8'))
            f.flush()
        f.close()

        return st
    else:
        return render_template('index.html')

@app.route("/v")
def video():
    return render_template("output.html")

@app.route("/s")
def show():
    return redirect('/static/output.mp4')

@app.route("/s1")
def show1():
    return redirect('/static/output1.mp4')

@app.route("/c")
def trans():
    if os.path.exists(BASE_DIR+'/static/output.mp4'):
        # 定义ffmpeg命令和参数的列表
        cmd = ['ffmpeg', '-i', BASE_DIR+'/static/output.mp4', '-vcodec', 'libx264', BASE_DIR+'/static/output1.mp4']
        cmd_str = ' '.join(cmd)
        # 调用subprocess.run函数，捕获异常
        try:
            os.system(cmd_str)
        except Exception as e:
            print(e)
        return "开始转换,若/s1不是空页面说明转换成功"
    else:
        return "请重试,文件未就绪"

@app.route('/sub', methods=['POST'])
def sub():
    parent=os.getcwd()
    os.chdir("static")
    os.chdir("file")
    try:
        os.remove("m.pdf")
        print(os.getcwd())
    except Exception as e:
        print(e)
    
    os.system("python mathsub1.py")
    os.chdir(parent)
    pdf_path = url_for('static', filename='file/m.pdf')
    return render_template('pdf.html', pdf_path=pdf_path)

@app.route('/word', methods=['POST'])
def word():
    # 获取表单提交的数据
    input = request.form.get('input')
    parent=os.getcwd()
    os.chdir("static")
    os.chdir("file")
    try:
        os.remove("m.pdf")
        print(os.getcwd())
    except Exception as e:
        print(e)
    
    os.system("python xieci.py "+input)
    os.chdir(parent)
    pdf_path = url_for('static', filename='file/m.pdf')
    return render_template('pdf.html', pdf_path=pdf_path)

@app.route('/word1', methods=['POST'])
def word1():
    # 获取表单提交的数据
    input = request.form.get('input')
    parent=os.getcwd()
    os.chdir("static")
    os.chdir("file")
    try:
        os.remove("m.pdf")
        print(os.getcwd())
    except Exception as e:
        print(e)
    
    os.system("python xieci2.py "+input)
    os.chdir(parent)
    pdf_path = url_for('static', filename='file/m.pdf')
    return render_template('pdf.html', pdf_path=pdf_path)

@app.route('/word2', methods=['POST'])
def word2():
    # 获取表单提交的数据
    input = request.form.get('input')
    parent=os.getcwd()
    os.chdir("static")
    os.chdir("file")
    try:
        os.remove("m.pdf")
        print(os.getcwd())
    except Exception as e:
        print(e)
    
    os.system("python xieci3.py "+input)
    os.chdir(parent)
    pdf_path = url_for('static', filename='file/m.pdf')
    return render_template('pdf.html', pdf_path=pdf_path)

@app.route('/mp3', methods=['POST'])
def mp3():
    # 获取表单提交的数据
    input = request.form.get('input')
    parent=os.getcwd()
    os.chdir("static")
    os.chdir("file")
    try:
        print(os.getcwd())
    except Exception as e:
        print(e)
    
    os.system("python reading.py "+input)
    os.chdir(parent)
    return render_template('mp3.html')

@app.route('/sub1', methods=['POST'])
def sub1():
    parent=os.getcwd()
    os.chdir("static")
    os.chdir("file")
    try:
        os.remove("m.pdf")
        print(os.getcwd())
    except Exception as e:
        print(e)
    
    os.system("python mathsub.py")
    os.chdir(parent)
    pdf_path = url_for('static', filename='file/m.pdf')
    return render_template('pdf.html', pdf_path=pdf_path)

@app.route('/sub2', methods=['POST'])
def sub2():
    parent=os.getcwd()
    os.chdir("static")
    os.chdir("file")
    try:
        os.remove("m.pdf")
        print(os.getcwd())
    except Exception as e:
        print(e)
    
    os.system("python mathmorethan.py")
    os.chdir(parent)
    pdf_path = url_for('static', filename='file/m.pdf')
    return render_template('pdf.html', pdf_path=pdf_path)

@app.route('/submit', methods=['POST'])
def submit():
    array_param = request.form['array_param'].split(',')

    font_size = request.form['font_size']
    interval_time = request.form['interval_time']

    cmd = ['rm', '-rf', BASE_DIR+'/static/output.mp4',BASE_DIR+'/static/output1.mp4']
    cmd_str = ' '.join(cmd)
    try:
        os.system(cmd_str)
    except Exception as e:
        print(e)
    # 定义ffmpeg命令和参数的列表
    cmd = ['python', BASE_DIR+'/mp4.py']+array_param+['-f',str(font_size)]+['-d',str(interval_time)]
    cmd_str = ' '.join(cmd)
    try:
        os.system(cmd_str)
    except Exception as e:
        print(e)
    return '运行/s查看视频/c视频转换/s1转换后的视频可直接播放 参数：{} '.format(array_param)

@app.route('/trr', methods=['GET', 'POST'])
def trr():
    if request.method == "GET":
        try:
            st = bztr.getTr()
            os.system("rm -rf tr.txt")
            os.system("touch tr.txt")
            with open('tr.txt', 'w') as f:
                f.write(st[0])
                f.flush()
            f.close()
            return st[1]
        except Exception as e:
            e.__suppress_context__
            return "更新失败！"

@app.route('/tr', methods=['GET', 'POST'])
def tr():
    if request.method == "GET":
        resp=""
        try:
            with open('tr.txt', 'r') as f:
                resp=f.read()
            f.close()
        except Exception as e:
            e.__suppress_context__
        return render_template('tracker.html',info=resp)

@app.route('/d', methods=['GET', 'POST'])
def docker():
    if request.method == "POST":
        img = request.files.get('file').read()
        st=dockerInspect.dockerformate(img)

        return st

@app.route('/pic', methods=['GET', 'POST'])
def picAdd():
    if request.method == "POST":
        files=request.files.getlist('pic')
        for file in files:
            filename=file.filename
            filetype=filename.split('.')[-1]
            print('文件类型:'+filetype)
            uploadpath=os.getcwd()+os.sep+'static/file'
            if not os.path.exists(uploadpath):
                os.mkdir(uploadpath)
            filename=str(time.time())+'.'+filetype
            print("文件名:"+filename)
            file.save(uploadpath+os.sep+filename)
        print(os.getcwd())
        parent=os.getcwd()
        os.chdir("static")
        os.chdir("file")
        try:
            os.remove("output.png")
            print(os.getcwd())
        except Exception as e:
            print(e)
        
        os.system("python imageCard.py")
        for filename in os.listdir(os.getcwd()):
            if os.path.splitext(filename)[1] == '.jpg':
                os.remove(filename)
        os.chdir(parent)
        # os.chdir(os.path.dirname(os.pardir()))
        # os.chdir(os.pardir())
        # print(os.getcwd())
 
        return "文件上传成功 static/file/output.png"
    else:
        return render_template('pic.html')

@app.route('/bf', methods=['GET'])
def bf():
        try:
            with open('st.txt', 'r') as f:
                st = f.read()
            f.close()
            return st
        except:
            return '不存在历史内容!'


@app.route('/cl', methods=['GET'])
def cl():
        print(os.getcwd())
        os.system('rm -f ./st.txt')
        return '内容已清空'


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
