import RPi.GPIO as GPIO
import time

class TMCSteppper:
    def __init__(self, EN, STEP, DIR, StepDelay,bcm_mode = True):
        # First 3 are various pins, last parameter is the default delay between each steps.
        self.ENABLE = EN
        self.STEP = STEP
        self.DIR = DIR
        self.StepDelay = StepDelay

        GPIO.setmode(GPIO.BCM if bcm_mode == True else GPIO.board)

        for pin in [self.ENABLE,self.STEP,self.DIR]:
            GPIO.setup(pin,GPIO.OUT)
    
    def EnableMotor(self):
        GPIO.output(self.ENABLE,GPIO.LOW)
    
    def DisableMotor(self):
        GPIO.output(self.ENABLE,GPIO.HIGH)
    
    def SetDirection(self,direction):
        GPIO.output(self.DIR,GPIO.HIGH if direction else GPIO.LOW)

    def MoveMotor(self,step_delay = 0):
        #not toos sure why i cant use self.StepDelay as a basic parameter
        step_delay = self.StepDelay if step_delay == 0 else step_delay
        
        GPIO.output(self.STEP,GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(self.STEP,GPIO.LOW)
        time.sleep(step_delay)