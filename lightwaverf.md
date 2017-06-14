**Control LightwaveRF switches**

The 433Mhz transmitters are units where you can just turn the signal off and on via GPIO in the case of a Raspberry Pi. They do not understand how to transmit the code sequences needed to control the LightwaveRF equipment. So programming is necessary to do that.

Use Python version of https://github.com/roberttidey/LightwaveRF

Requires pigpio

**Install pigpio**
```
http://abyz.co.uk/rpi/pigpio/download.html
wget abyz.co.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
sudo make install
```

this will install pigpio.py interface for your python programs

```
copying build/lib.linux-armv7l-2.7/pigpio.py -> /usr/local/lib/python2.7/dist-packages
byte-compiling /usr/local/lib/python2.7/dist-packages/pigpio.py to pigpio.pyc
```

**Starting/Stopping pigpio daemon:**
```
sudo pigpiod
sudo killall pigpiod
```

**Tesing pigpio (runs python test, make sure pigpiod is running)**
```
./x_pigpio.py
```
