#!/bin/bash

gpio export 18 out

sleep 0.9
gpio -g write 18 1
sleep 0.4
gpio -g write 18 0
sleep 1.2
gpio -g write 18 1
sleep 0.4
gpio -g write 18 0
