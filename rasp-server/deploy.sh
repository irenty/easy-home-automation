#!/usr/bin/env bash


server_folder=~/rasp-server

echo 'Creating rasp-server folder'
rm -rvf $server_folder
mkdir -p $server_folder

cp ./server.py $server_folder
cp ./../lightwave-rf/lwrfCustom.py $server_folder
cp ./../lightwave-rf/lwrf_driver.py $server_folder