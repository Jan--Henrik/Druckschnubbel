#!/bin/python3

from PIL import Image
import time
import sys

def printCyber(length):
    imgwhite = img = Image.new("RGB", (1280, 960), "white") # create an image object
    for x in range(0,length):
        imgwhite.save("app/uploads/imgw.png")
        #time.sleep(10)
        for y in range(1,6):
            img = Image.open("creator/data/cyber%i.png" % (y))
            img.save("app/uploads/cyber%i.png" % (y))
            #time.sleep(10)
        imgwhite.save("app/uploads/imgw.png")
        #time.sleep(10)


if __name__ == '__main__': # if used as single programm
    printCyber(int(sys.argv[1]))

