#!/usr/bin/env bash


server_folder=~/rasp-server

echo 'Deleting old rasp-server folder'
rm -rvf $server_folder

echo 'Creating rasp-server folder'
mkdir -p $server_folder

echo 'Copying server files'
cp ./server.py $server_folder

echo 'Copying dummy lirc driver'
cp ./lirc_driver.py $server_folder

echo 'Copying real lwrf driver'
cp ./../lightwave-rf/lwrfCustom.py $server_folder
cp ./../lightwave-rf/lwrf_driver.py $server_folder

echo 'Copying run script'
cp ./run.sh $server_folder
chmod +x $server_folder/run.sh

echo "Now go to $server_folder and execute run.sh"