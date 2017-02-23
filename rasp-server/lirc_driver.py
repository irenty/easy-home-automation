#!/fsr/bin/env python
import time


def lirc_send(command):
    print("lirc is executing command {}".format(command))
    time.sleep(2)
