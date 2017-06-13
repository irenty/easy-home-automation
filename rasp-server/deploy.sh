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
chmod +x ./run.sh
cp ./run.sh $server_folder

echo "Now execute run.sh"