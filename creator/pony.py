#!/bin/python2.7

from random import randint
import time
import os
import urllib
import requests
import shutil


infile = "/home/janhenrik/Druckschnubbel/creator/topscore.pony"

def getLink(infile):
    with open(infile,'r') as target:
        content = target.read()
    content = content.split('\n')
    link = content[randint(0,len(content)-2)]
    return link

def getFile(link):
    adress = "https:%s" % (link)
    response = requests.get(adress, stream=True)
    with open('/home/janhenrik/Druckschnubbel/app/uploads/%s' % (link.replace("/","")[:10]), 'wb') as out_file:
       shutil.copyfileobj(response.raw, out_file)
    del response

def printPony():
    link = getLink(infile)
    getFile(link)

