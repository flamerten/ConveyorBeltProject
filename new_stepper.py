import TMC_Stepper
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

RollerStepper = TMC_Stepper(EN,STEP,DIR,DELAY_TIME*0.0000001)

RollerStepper.setDirection(True)
RollerStepper.EnableMotor()

GPIO.setup(ROCKER,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BEAM,GPIO.IN,pull_up_down = GPIO.PUD_UP) #neccessary to pull up?

while True:
    try:
        if(GPIO.input(BEAM) == GPIO.LOW): #beam broken and not high
            print("LOW") #beam broken do something
            time.sleep(2)
        else:
            if(GPIO.input(ROCKER) == GPIO.HIGH):
                RollerStepper.MoveMotor()
    except:
        #Keyboard interupt to stop program
        print("Exception hit")
        break

GPIO.cleanup()
print("Done")