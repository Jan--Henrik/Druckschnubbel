#!/bin/python2.7

import shutil
from random import randint

import requests

infile = "/home/janhenrik/Druckschnubbel/creator/data/topscore.pony"  # pony image link list


def getLink(infile):
    with open(infile, 'r') as target:
        content = target.read()
    content = content.split('\n')
    link = content[randint(0, len(content) - 2)]  # choose random image
    return link


def getFile(link):
    adress = "https:%s" % (link)  # create link
    response = requests.get(adress, stream=True)  # download and save
    with open('app/uploads/%s' % (link.replace("/", "")[15:]), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


def printPony():
    link = getLink(infile)
    getFile(link)
