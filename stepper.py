import RPi.GPIO as GPIO
import time

#Define GPIOs for the driver, rocker and the IR beam
DIR    = 16
STEP   = 20
EN     = 21
ROCKER = 26
BEAM   = 1

#affects the speed of the motor
DELAY_TIME = 5000 

def run_motor():
    GPIO.output(STEP,GPIO.HIGH)
    time.sleep(DELAY_TIME * 0.0000001)
    GPIO.output(STEP,GPIO.LOW)
    time.sleep(DELAY_TIME * 0.0000001)

GPIO.setmode(GPIO.BCM)

#enable the driver
GPIO.setup(EN,GPIO.OUT)
GPIO.output(EN,GPIO.LOW) 

#Setup the GPIOs
GPIO.setup(DIR,GPIO.OUT)
GPIO.setup(STEP,GPIO.OUT)
GPIO.setup(ROCKER,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BEAM,GPIO.IN,pull_up_down = GPIO.PUD_UP) #neccessary to pull up?

#Set the direction of the motor. Use GPIO.LOW/GPIO.HIGH
GPIO.output(DIR,GPIO.LOW)

while True:
    try:
        if(GPIO.input(BEAM) == GPIO.LOW): #beam broken and not high
            print("LOW") #beam broken do something
            time.sleep(2)
        else:
            if(GPIO.input(ROCKER) == GPIO.HIGH):
                run_motor()
    except:
        #Keyboard interupt to stop program
        print("Exception hit")
        break

GPIO.cleanup()
print("Done")
