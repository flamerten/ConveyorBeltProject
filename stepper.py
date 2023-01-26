DIR    = 16
STEP   = 20
EN     = 21
ROCKER = 26
BEAM   = 12


DELAY_TIME = 5000 #affects the speed of the stepper motor

import RPi.GPIO as GPIO
import time

def run_motor():
    GPIO.output(STEP,GPIO.HIGH)
    time.sleep(DELAY_TIME * 0.0000001)
    GPIO.output(STEP,GPIO.LOW)
    time.sleep(DELAY_TIME * 0.0000001)

GPIO.setmode(GPIO.BCM)

#enable the driver
GPIO.setup(EN,GPIO.OUT)
GPIO.output(EN,GPIO.LOW) 

GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)

GPIO.setup(ROCKER,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BEAM,GPIO.IN)

#change this depending on the direction of the belt
GPIO.output(DIR,GPIO.LOW)

while True:
    try:
        if(GPIO.input(ROCKER) == GPIO.HIGH):
            run_motor()
        elif(GPIO.input(BEAM) == GPIO.LOW):            #if the beam is broken, no longer high
            time.sleep(10)                             #delay for 10s
        #else -> don't move at all
    except:
        print("Exception hit")
        break


GPIO.cleanup()
print("Done")
