#!/bin/sh

cd $(dirname "$0")
rm -f app/uploads/*

#core applications
sudo python2.7 app/views.py &
sudo python2.7 driver/printer.py &

#additional stuff
#sudo python2.7 creator/twitter.py
