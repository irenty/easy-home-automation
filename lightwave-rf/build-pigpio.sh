#!/usr/bin/env bash

echo 'Copying custom LightwaveRF module to PIGPIO folder'
cp ./c-custom/custom.cext ~/PIGPIO/
cp ./c-custom/custom_lwrf.h ~/PIGPIO/

echo 'Stopping PIGPIO daemon'
sudo killall  pigpiod

echo 'Building PIGPIO'
cd ~/PIGPIO/
make

echo 'Installing PIGPIO'
sudo make install
