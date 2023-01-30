from TMC_Stepper import TMCSteppper
import RPi.GPIO as GPIO
import time

#Define GPIOs for the 2 drivers, rocker and the IR beam
ROL_DIR    = 16
ROL_STEP   = 20
ROL_EN     = 21
ROL_DELAY_TIME = 5000 * 0.0000001

CUR_DIR    = 17
CUR_STEP   = 27
CUR_EN     = 22
CUR_DELAY_TIME = 2500 * 0.0000001 #made 2x speed of roller?

CUR_STEPS = 2000 #number of microsteps that the 

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
        #check if beam has been broken AND rocker switch is turned on 
        if( (GPIO.input(BEAM) == GPIO.LOW) and (GPIO.input(ROCKER) == GPIO.HIGH) ):
            print("Beam hit")
            for i in range(CUR_STEPS):
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