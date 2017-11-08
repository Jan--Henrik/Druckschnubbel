#!/bin/bash

gpio export 24 out
touch "2.lock"
touch "1.lock"
sleep 3.9
gpio -g write 24 1
sleep 0.4
gpio -g write 24 0
rm "1.lock"
sleep 10
rm "2.lock"
