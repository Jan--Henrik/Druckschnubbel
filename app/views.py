import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import sys
sys.path.append( "../creator/" )
from scretchcard import createCard
import urllib
from shutil import copyfile

debug = False

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html',
                           Dateitypen=str(app.config['ALLOWED_EXTENSIONS']).replace("[", "").replace("]", "").replace("'", "").replace(",", ", "))

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("file")
    for file in uploaded_files:
      print(file)
      if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # check for unallowed chars
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('printing'))


@app.route('/templates/scratchcard.html')
def scratchcard():
    return render_template('scratchcard.html')


@app.route('/templates/', methods=['POST'])
def scratchcard_receive():
    text = request.form['text']
    createCard(text)
    print("done")
    return redirect(url_for('printing'))


@app.route('/', methods=['POST'])
def url():
    text = request.form['text']
    filename,msg = urllib.urlretrieve(text)
    os.system("cp %s %s" % (filename,"/home/janhenrik/Druckschnubbel/app/uploads"));
    return redirect(url_for('printing'))


@app.route('/templates/printing.html')
def printing():
    return render_template('printing.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('err404.html'), 404


@app.route('/templates/error.html')
def err():
    return render_template('error.html'), 404


if __name__ == '__main__':
    if debug == False:
        app.run(
            host="0.0.0.0",
            port=int("80"),
            debug=False
        )
    else:
        app.run(
            debug=True
        )
