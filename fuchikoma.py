#from servodriver import ServoDriver

import numpy as np
from Adafruit_PWM_Servo_Driver import PWM
import traceback as traceback
import time
import sys
#sys.path.append("/home/pi/Desktop/NAVI")
import speech_recognition as sr
from espeak import espeak
from datetime import datetime
t = datetime.now().strftime('%k %M')

# Initialise the PWM device using the default address
pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

pwm.setPWMFreq(60)

class FUCHI:
#///////////////////////////////////////////motion
    def move(servo, angle):#, delta=170):
      #delay = max(delta * 0.003, 0.03)        # calculate delay
      zero_pulse = (servoMin + servoMax) / 2  # half-way == 0 degrees
      pulse_width = zero_pulse - servoMin     # maximum pulse to either side 
      pulse = zero_pulse + (pulse_width * angle / 80)
      #print("angle=%s pulse=%s" % (angle, pulse))
      pwm.setPWM(servo, 0, int(pulse))
      #time.sleep(delay)  # sleep to give the servo time to do its thing
      
    def mini(servo):
        #pwm.setPWM(servo, 0, servoMin)
        FUCHI.move(servo,-77)

    def plus(servo):
        #pwm.setPWM(servo,0, servoMax)
        FUCHI.move(servo, 77)

    def relax(servo):
        FUCHI.move(servo, 0)


'''while True:# continous rotation import the servodriver.py to use
    servos=ServoDriver()
    servos.continuous(0,continuous=True)
    servos.move(0,1500)'''#1000 1500 2000
