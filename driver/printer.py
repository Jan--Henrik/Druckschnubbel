import subprocess
from PIL import Image
from os import listdir
from os.path import isfile, join


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
        self.filestr = self.filepath + "/" + self.file
        img = Image.open(self.filestr)

        if img.size[0] < img.size[1]:
            self.rotflag = True

        new_size = (
        self.printwidth * (self.printpercent - 2.0) / 100.0, self.printheight * (self.printpercent - 2.0) / 100.0)
        print(img.size, new_size, self.filestr)

        subprocess.call(
            "gm convert  {0} -verbose -resize {1}x{2} -gravity South -extent {3}x{4} -auto-orient {5}".format(
                self.filestr, new_size[0], new_size[1], self.printwidth, self.printheight, self.filestr), shell=True)

        subprocess.call("sh gpio.sh &", shell=True)
        subprocess.call("fbi --noverbose -d /dev/fb0 -T 7 -t 1 -1 {0}".format(self.filestr), shell=True)
        subprocess.call("rm -f {0}".format(self.filestr), shell=True)


class pollfiles():
    def __init__(self, path):
        self.path = path
        self.excec = execute(self.path, "")

    def run(self):
        while True:
            onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
            if len(onlyfiles) > 0:
                self.excec.run(onlyfiles[0])


if __name__ == '__main__':
    poll = pollfiles("../app/uploads")
    poll.run()
