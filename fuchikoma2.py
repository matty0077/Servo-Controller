#!/usr/bin/python
from __future__ import division
import sys
#////////////////servo
import PCA9685
from Adafruit_PWM_Servo_Driver import PWM
pwm = PWM(0x40)
pwm.setPWMFreq(60)

#///////////
import time
import atexit

class FUCHIKOMA:
    delay = max(170 * 0.0017, 0.017)  #0.002 0.02      # calculate delay for proper movement. change to fractions of a second(.078) to speed up but reduce accuracy of movement
    # Configure min and max servo pulse lengths
    servo_min = 150  # Min pulse length out of 4096
    servo_max = 600  # Max pulse length out of 4096
    def move(self, servo, angle, delta=170):#120
      zero_pulse = (self.servo_min + self.servo_max) / 2  # half-way == 0 degrees
      pulse_width = zero_pulse - self.servo_min     # maximum pulse to either side 
      pulse = zero_pulse + (pulse_width * angle / 80)
      #print("angle=%s pulse=%s" % (angle, pulse))
      pwm.setPWM(servo, 0, int(pulse))
      time.sleep(self.delay)#.078 self.delay
      pwm.setPWM(servo, 0, 0)
      #pwm.set_pwm_freq(pulse)#60)#good fo servo

    ###########GENERAL USE
    def mini(self, servo):
        self.move(servo,-77)

    def plus(self, servo):
        self.move(servo, 77)

    def relax(self, servo):
        self.move(servo, 0)
#/////////////////cut power to all servos==total relax
    def servo_lax(self):
        i=0
        while i<16:
            pwm.setPWM(i, 0, 0)
            i+=1

#################################REFINED USE
    ############claw
    def bite(self):
        self.delay = max(170 * 0.0017, 0.017)  # calculate delay for proper movement
        #self.delay=.078 #dirty delay for quick, jolty movement
        self.move(0,-75)
    def bopen(self):
        self.delay = max(170 * 0.0017, 0.017)  # calculate delay for proper movement
        #self.delay=.078 #dirty delay for quick, jolty movement
        self.move(0,75)
        
    #########locks
    def lok(self):
        self.delay = max(170 * 0.0017, 0.017)  # calculate delay for proper movement
        #self.delay=.078 #dirty delay for quick, jolty movement
        self.move(1,75)
        
    def lopen(self):
        self.delay = max(170 * 0.0017, 0.017)  # calculate delay for proper movement
        #self.delay=.078 #dirty delay for quick, jolty movement
        self.move(1,-75)
        
    #########watergun
    def shoot(self):
        self.delay = max(170 * 0.0017, 0.017)  # calculate delay for proper movement
        #self.delay=.078 #dirty delay for quick, jolty movement
        self.move(2,-75)
        time.sleep(.15)
        self.load()
        
    def load(self):
        self.delay = max(170 * 0.0017, 0.017)  # calculate delay for proper movement
        #self.delay=.078 #dirty delay for quick, jolty movement
        self.move(2,75)

        
F=FUCHIKOMA()


