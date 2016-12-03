#!/bin/sh

cd $(dirname "$0")
rm -f app/uploads/*

#cd app/
sudo python2.7 app/views.py &
#cd ../driver/
sudo python2.7 driver/printer.py &

sudo python2.7 creator/twitter.py
