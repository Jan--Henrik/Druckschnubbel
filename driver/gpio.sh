#!/bin/bash

gpio export 18 out

sleep 3.9
gpio -g write 18 1
sleep 0.4
gpio -g write 18 0
