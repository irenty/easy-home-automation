#!/fsr/bin/env python
import time
import sys


def lw_send(command):
    import time
    import pigpio
    import lwrfCustom

    print("lwrf is executing command {}".format(command))

    TX=25
    TX_REPEAT = 10

    pi = pigpio.pi() # Connect to local Pi.

    tx = lwrfCustom.tx(pi, TX) # Specify Pi, tx gpio, and baud.

    # print "Transmit testing sending", TX_TEST, TX_REPEAT, "times"
    tx.put(command, TX_REPEAT)

    start = time.time()

    time.sleep(1)
    tx.cancel()
    pi.stop()
    time.sleep(1)

if __name__ == "__main__":
    command = '0031F46848'
    if len(sys.argv) == 2:
        command = sys.argv[1]
    lw_send(command)