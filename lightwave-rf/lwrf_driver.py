#!/fsr/bin/env python
import sys


def lw_send(command):
    import time
    import pigpio
    import lwrfCustom

    print("lwrf is executing command {}".format(command))

    TX=4
    TX_REPEAT = 10

    pi = pigpio.pi() # Connect to local Pi.

    tx = lwrfCustom.tx(pi, TX) # Specify Pi, tx gpio, and baud.

    tx.put(command, TX_REPEAT)

    time.sleep(1)
    tx.cancel()
    pi.stop()
    time.sleep(1)

if __name__ == "__main__":
    command = '0031F46848'
    if len(sys.argv) == 2:
        command = sys.argv[1]
    lw_send(command)