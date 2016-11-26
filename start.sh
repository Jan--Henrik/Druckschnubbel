#!/bin/sh

cd $(dirname "$0")

cd app/
sudo python2.7 views.py &
cd ../driver/
sudo python2.7 printer.py &

