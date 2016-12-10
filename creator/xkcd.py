#!/bin/python3.5

import urllib
import json
import shutil
import requests
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap


def getLink():
    page = urllib.request.urlopen("http://xkcd.com/info.0.json").read().decode("utf-8") # download page and decode
    data = json.loads(page) # parse json
    imagelink = data['img'] # fetch the imagelink
    text = data['alt'] # fetch the mouseover text
    return imagelink,text


def getFile(link):
    response = requests.get(link, stream=True)  # download and save
    with open('app/uploads/%s' % (link.replace("/", "")[15:]), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file) # move from tmp to app/uploads/
    del response # delete the tmp file


def createText(text):
    message = wrap(text, 30) # create the mouseover text
    img = Image.new("RGB", (1280, 960), "white") # create an image object
    draw = ImageDraw.Draw(img) # make it drawable
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 96) # load font
    cnt = 0
    for line in message:
        draw.text((50, 96*cnt), line, (0, 0, 0), font=font) # split lines and draw onto the image
        cnt += 1
    img.save("app/uploads/scretch%01s.png" % (len(line))) # save it with an "uniqe" name


def printXkcd(): # if used as library
    link,text = getLink()
    getFile(link)
    createText(text)


if __name__ == '__main__': # if used as single programm
    printXkcd()

