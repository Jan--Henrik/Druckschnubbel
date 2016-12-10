#!/bin/python3.5

import urllib
import json
import shutil
import requests
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap


def getLink():
    url = "http://xkcd.com/info.0.json"
    page = urllib.request.urlopen(url).read()
    page = page.decode("utf-8")
    data = json.loads(page)
    imagelink = data['img']
    text = data['alt']
    return imagelink,text


def getFile(link):
    response = requests.get(link, stream=True)  # download and save
    with open('app/uploads/%s' % (link.replace("/", "")[15:]), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


def createText(text):
    message = wrap(text, 30)
    img = Image.new("RGB", (1280, 960), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf", 96)
    cnt = 0
    for line in message:
        draw.text((50, 96*cnt), line, (0, 0, 0), font=font)
        cnt += 1
    img.save("app/uploads/scretch%01s.png" % (len(line)))


def printXkcd():
    link,text = getLink()
    getFile(link)
    createText(text)


if __name__ == '__main__':
    printXkcd()

