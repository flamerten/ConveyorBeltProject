from TMC_Stepper import TMCSteppper
import RPi.GPIO as GPIO
import time

#Define GPIOs for the 2 drivers, rocker and the IR beam
ROL_DIR    = 16
ROL_STEP   = 20
ROL_EN     = 21
ROL_DELAY_TIME = 5000 * 0.0000001

CUR_DIR    = 16
CUR_STEP   = 20
CUR_EN     = 21
CUR_DELAY_TIME = 2500 * 0.0000001 #made 2x speed of roller?

ROCKER = 26
BEAM   = 1

#Declare driver objects for each stepper driver
RollerStepper  = TMCSteppper(ROL_EN,ROL_STEP,ROL_DIR,ROL_DELAY_TIME)
CurtainStepper = TMCSteppper(CUR_EN,CUR_STEP,CUR_DIR,CUR_DELAY_TIME) 

RollerStepper.SetDirection(True)
RollerStepper.EnableMotor()

CurtainStepper.SetDirection(True)
RollerStepper.EnableMotor()

GPIO.setup(ROCKER,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(BEAM,GPIO.IN,pull_up_down = GPIO.PUD_UP)

while True:
    try:
        if(GPIO.input(BEAM) == GPIO.LOW): #beam broken and not high
            print("Beam hit")
            for i in range(2000):
                CurtainStepper.MoveMotor()
        else:
            if(GPIO.input(ROCKER) == GPIO.HIGH):
                RollerStepper.MoveMotor()
    except:
        #Keyboard interupt to stop program
        print("Exception hit")
        break

GPIO.cleanup()
print("Done")