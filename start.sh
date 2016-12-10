#!/bin/sh

cd $(dirname "$0")
rm -f app/uploads/*

#core applications
sudo python3 app/views.py &
sudo python3 driver/printer.py &

#additional stuff
#sudo python2.7 creator/twitter.py
