#!/bin/python3.5

from random import randint
import subprocess
import time
import os

infile = sys.argv[1]


def getLink(infile):
    with open(infile,'r') as target:
        content = target.read()
    content = content.split('\n')
    link = content[randint(0,len(content)-2)]
    return link

def getFile(link):
    filename,msg = urllib.urlretrieve("https://derpicdn.net{1}".format(link[link.find(".")+1:],link))
    os.system("cp %s %s" % (filename,"/home/janhenrik/Druckschnubbel/app/uploads"));

t = WriteFile(outString)
t.start()

while(1):

    link = getLink(infile)
    getFile(link)

    time.sleep(7)

