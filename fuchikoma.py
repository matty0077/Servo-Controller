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

class FUCHI:#our controller class
#///////////////////////////////////////////motion(automatically calibrates to he zero point on our servos)
    def move(servo, angle):#, delta=170):
      #delay = max(delta * 0.003, 0.03)        # calculate delay
      zero_pulse = (servoMin + servoMax) / 2  # half-way == 0 degrees
      pulse_width = zero_pulse - servoMin     # maximum pulse to either side 
      pulse = zero_pulse + (pulse_width * angle / 80)
      #print("angle=%s pulse=%s" % (angle, pulse))
      pwm.setPWM(servo, 0, int(pulse))
      #time.sleep(delay)  # sleep to give the servo time to do its thing
      
    def mini(servo):
        #servo is the slot the servo is plugged into from 0-15
        #-77 is a little less than a 180 rotation to make sure we dont damage our servo
        FUCHI.move(servo,-77)

    def plus(servo):
        #77 is a safe rotation in the OPPOSITE direction
        #change the numbers to modify rotational degrees
        FUCHI.move(servo, 77)

    def relax(servo):
        #puts us back on zero.
        FUCHI.move(servo, 0)


#///////////test code
#-77° on our servos.
FUCHI.mini(0)
Time.sleep(.25)
FUCHI.mini(1)
Time.sleep(.25)

#77° the opposite way
FUCHI.plus(0)
Time.sleep(.25)
FUCHI.plus(1)
Time.sleep(.25)

#back to zero point.
#youll only want to attach your servo to anything
#after its been set to zero. So your not constantly adjusting your construction.
#so run this test on every servo you plan to use!
FUCHI.relax(0)
Time.sleep(.25)
FUCHI.relax(1)
Time.sleep(.25)
