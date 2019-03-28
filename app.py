# coding=utf-8

from flask import *
import bzocr
import os

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

@app.route('/bf', methods=['GET'])
def bf():
        with open('st.txt', 'r') as f:
            st=f.read()
        f.close()
        return st

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
