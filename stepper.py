DIR = 16
STEP = 20
EN = 21
ROCKER = 26

DELAY_TIME = 5000

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
GPIO.output(DIR,GPIO.LOW)
GPIO.setup(STEP,GPIO.OUT)
GPIO.setup(ROCKER,GPIO.IN)

#change this depending on the direction of the belt
GPIO.output(DIR,GPIO.LOW)

for i in range(2000):
    run_motor()

GPIO.cleanup()
print("Done")
