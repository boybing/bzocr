# coding=utf-8

from flask import *
import bzocr
import os
import time

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

###
# Routing for your application.
###

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
        print(os.getcwd())
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
    app.run()
