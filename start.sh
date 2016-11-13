#!/bin/sh
cd app/
python2.7 views.py &
cd ../driver/
python2.7 printer.py &

