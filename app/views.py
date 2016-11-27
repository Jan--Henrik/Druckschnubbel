import os
import shutil
import subprocess
import sys
import urllib

import requests
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

sys.path.append("../creator/")
from scretchcard import createCard
from pony import printPony

debug = False  # if true it will run on localhost

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'  # uploadfolder
app.config['ALLOWED_EXTENSIONS'] = ['png', 'jpg', 'jpeg', 'gif']  # alowed file extensions


def allowed_file(filename):  # routine for file extensions
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html',
                           Dateitypen=str(app.config['ALLOWED_EXTENSIONS']).replace("[", "").replace("]", "").replace(
                               "'", "").replace(",", ", "))


@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("file")  # get file
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # check for unallowed chars and fix the filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # save file
    return redirect(url_for('printing'))


@app.route('/scratchcard')  # routine for the scretchcard input
def scratchcard():
    return render_template('scratchcard.html')


@app.route('/scr', methods=['POST'])  # routine to render the scretchcard
def scratchcard_receive():
    text = request.form['text']
    createCard(text)
    return redirect(url_for('printing'))


@app.route('/url', methods=['POST'])  # routine for url input
def url():
    adress = request.form['text']
    response = requests.get(adress, stream=True)  # response library allows http/https
    with open('app/uploads/%s' % (adress.replace("/", "")[15:]), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return redirect(url_for('printing'))


@app.route('/xkcd')  # routine for the newest xkcd comic strip
def xkcd():
    filename, msg = urllib.urlretrieve("http://imgs.xkcd.com/comics/xkcde.png")  # url for the newest one
    os.system("cp %s %s" % (filename, "app/uploads"));
    return redirect(url_for('printing'))


@app.route('/pony')  # routine for the random pony script
def pony():
    printPony()
    return redirect(url_for('printing'))


@app.route('/miku')  # routine for the hatsune miku image
def miku():
    subprocess.call("/home/janhenrik/Druckschnubbel/creator/./yandere.sh hatsune_miku", shell=True)
    return redirect(url_for('printing'))


@app.route('/templates/printing.html')  # printing wait page
def printing():
    return render_template('printing.html')


@app.errorhandler(404)  # 404 error handling
def page_not_found(error):
    return render_template('err404.html'), 404


@app.route('/templates/error.html')  # general error handling
def err():
    return render_template('error.html'), 404


if __name__ == '__main__':
    if debug == False:
        app.run(
            host="0.0.0.0",  # listen to all ip's
            port=int("80"),  # needs root :/
            debug=False
        )
    else:
        app.run(
            debug=True
        )
