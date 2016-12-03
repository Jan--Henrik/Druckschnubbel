import os
import subprocess
import time
from os import listdir
from os.path import isfile, join

from PIL import Image


class execute():
    def __init__(self, filepath, file):
        self.filepath = filepath
        self.file = file
        self.filestr = ""

        self.printwidth = 1280
        self.printheight = 1024

        self.printpercent = 100

        self.rotflag = False

    def run(self, file):
        self.file = file
        self.filestr = self.filepath + self.file
        try:  # calculate new size
            img = Image.open(self.filestr)

            if img.size[0] < img.size[1]:
                self.rotflag = True

            new_size = (
                self.printwidth * (self.printpercent - 2.0) / 100.0,
                self.printheight * (self.printpercent - 2.0) / 100.0)

            subprocess.call(
                "gm convert  {0} -verbose -resize {1}x{2} -gravity South -extent {3}x{4} -auto-orient {5}".format(
                    self.filestr, new_size[0], new_size[1], self.printwidth, self.printheight, self.filestr),
                shell=True)  # convert image
            time.sleep(5)
            subprocess.call("sh driver/gpio.sh &", shell=True)  # toogle printer pin
            subprocess.call("fbi --noverbose -d /dev/fb0 -T 7 -t 6 -1 {0}".format(self.filestr),
                            shell=True)  # show image
            time.sleep(10)  # time the printer need to print
            subprocess.call("rm -f {0}".format(self.filestr), shell=True)  # remove the image
        except:
            print("Failed, I will try again")  # not so good errorhandling


class pollfiles():
    def __init__(self, path):
        self.path = path
        self.excec = execute(self.path, "")

    def run(self):
        while True:
            time.sleep(0.4)
            onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]  # list files in buffer
            if len(onlyfiles) > 0:
                self.excec.run(onlyfiles[0])  # start to print with 1 file


if __name__ == '__main__':
    poll = pollfiles("app/uploads/".format(os.getcwd()))
    poll.run()  # poll for files
