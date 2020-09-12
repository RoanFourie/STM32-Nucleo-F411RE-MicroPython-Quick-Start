from pyb import LED
import time

led = LED(1)

while True:
    led.toggle()
    time.sleep(1)