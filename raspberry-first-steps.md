**Install OS - Copy OS image to Micro SD Card**

https://www.raspberrypi.org/documentation/installation/installing-images/

**Download Raspbian OS**

https://www.raspberrypi.org/downloads/raspbian/

RASPBIAN JESSIE LITE
https://www.raspberrypi.org/documentation/installation/installing-images/README.md

Etcher is an image writing tool that writes directly from the zip file.


**Run**
* Insert card to Raspberry PI.
* Plug in HDMI and connect to monitor
* Plug in Network cable
* Plug in USB keyboard
* Plug in Power cable
* Login user: pi / password: raspberry
* Network should work out of the box

**Setup ssh**

https://www.raspberrypi.org/documentation/remote-access/ssh/

**Enable ssh**

raspi-config can be used:

- Enter sudo raspi-config in a terminal window
- Select Interfacing Options
- Navigate to and select SSH
- Choose Yes
- Select Ok
- Choose Finish

**SSH without password**

* generate key
* copy public key to authorised keys:
```
cat  putty-rsa-key.pub >> ~/.ssh/authorized_keys
it has to be 1 line version of public key
chmod 600 ~/.ssh/authorized_keys
```

**Enable authorized_keys ssh**
```
vim /etc/ssh/sshd_config
AuthorizedKeysFile      %h/.ssh/authorized_keys
restart the ssh deamon
sudo service ssh restart
```

**Configure WIFI**

https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

Scan networks
```
sudo iwlist wlan0 scan
```

Add network details to config file
```
sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
add at the bottom:
network={
    ssid="testing"
    psk="testingPassword"
}
```

Restart wlan0
```
sudo wpa_cli reconfigure
```

**Check wlan0**
```
ifconfig wlan0
```
If the inet addr field has an address beside it, the Raspberry Pi has connected to the network.


**Install git**
```
sudo apt-get update
sudo apt-get install git
```

**Install pip**
```
sudo apt-get update
sudo apt-get install python-pip
```

**Install wiringpi tool to control gpio**

http://wiringpi.com/download-and-install/

Check if installed:
```
gpio -v
```

**Install wiringpi**

```
git clone git://git.drogon.net/wiringPi
cd ~/wiringPi
./build
```

**Test wiringPi**
```
gpio -v
gpio readall
gpio mode 0 out
gpio write 0 1
```


