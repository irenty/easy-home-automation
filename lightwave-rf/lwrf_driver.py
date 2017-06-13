#!/fsr/bin/env python
import time
import sys


def lw_send(command):
    print("lwrf is executing command {}".format(command))
    time.sleep(2)

if __name__ == "__main__":
    command = '0031F46848'
    if len(sys.argv) == 2:
        command = sys.argv[1]
    lw_send(command)