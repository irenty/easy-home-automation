#!/fsr/bin/env python
import time
import sys


if __name__ == "__main__":

    import time
    import pigpio
    import lwrfCustom

    RX=24
    RX_REPEAT = 0

    pi = pigpio.pi() # Connect to local Pi.

    rx = lwrfCustom.rx(pi, RX, RX_REPEAT) # Specify Pi, rx gpio, and repeat.

    start = time.time()

    while (time.time()-start) < 20:
        if rx.ready():
            print "Received", rx.get()
        time.sleep(0.02)
    rx.cancel()
    pi.stop()
    time.sleep(2)