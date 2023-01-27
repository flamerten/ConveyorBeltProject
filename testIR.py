DIR    = 16
STEP   = 20
EN     = 21
ROCKER = 26
BEAM   = 1

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(BEAM,GPIO.IN,pull_up_down = GPIO.PUD_UP)

for i in range(10):
    if(GPIO.input(BEAM) == GPIO.HIGH):
        print("High")
    else:
        print("Low")
    time.sleep(1)

print("Done")