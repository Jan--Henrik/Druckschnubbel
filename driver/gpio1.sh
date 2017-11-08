#!/bin/bash

gpio export 23 out
touch "1.lock"
touch "2.lock"
sleep 3.9
gpio -g write 23 1
sleep 0.4
gpio -g write 23 0
rm "2.lock"
sleep 10
rm "1.lock"
