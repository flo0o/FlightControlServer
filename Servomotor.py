# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
#from __future__ import division
import time

# Import the PCA9685 module.
#import Adafruit_PCA9685

# Configure min and max servo pulse lengths
servo_min = 330  # Min pulse length out of 4096
servo_max = 510  # Max pulse length out of 4096
servo_mid = 420  # Max pulse length out of 4096
servo_min2 = 280  # Min pulse length out of 4096
servo_max2 = 480  # Max pulse length out of 4096
servo_mid2 = 400  # Max pulse length out of 4096
servo_min3 = 0  # Min pulse length out of 4096
servo_max3 = 500  # Max pulse length out of 4096
servo_mid3 = 250  # Max pulse length out of 4096
optifrequ = 66
hoehe_max = 480
hoehe_mid = 400
hoehe_min = 280

cur_X = servo_mid #initial value of servo motor
cur_X2 = servo_mid2 #initial value of servo motor
cur_X3 = servo_min3 #initial value of servo motor
#b = raw_input("frequency? ")
#b = int(float(b))
#pwm.setPWMFreq(60)

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
def setup():
    #pwm = Adafruit_PCA9685.PCA9685()
    #pwm.set_pwm_freq(optifrequ)

# Alternatively specify a different address and/or bus:
# pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)



        print('Moving servo on channel 0, press Ctrl-C to quit...')

def ServoUp():
        global cur_X
        cur_X += 5
        if cur_X >servo_max:
                cur_X = servo_max
        #pwm.set_pwm(0, 0, cur_X)

def ServoDown():
        global cur_X

        cur_X -= 5
        if cur_X < servo_min:
            cur_X = servo_min
        #pwm.set_pwm(0,0 cur_X)

def ServoSetpoint(setpoint):
        global cur_X
        cur_X = int(setpoint[0])
        if cur_X < servo_min:
            cur_X = servo_min
        if cur_X > servo_max:
            cur_X = servo_max
        # pwm.set_pwm(0,0 cur_X)


def ServoSetpoint2(setpoint):
    global cur_X2
    cur_X2 = int(setpoint[0])
    if cur_X2 < servo_min2:
        cur_X2 = servo_min2
    if cur_X2 > servo_max2:
        cur_X2 = servo_max2
    # pwm.set_pwm(1,0 cur_X2)
def ServoSetpoint3(setpoint):
        global cur_X3
        cur_X3 = int(setpoint[0])
        if cur_X3 < servo_min3:
            cur_X3 = servo_min3
        if cur_X3 > servo_max3:
            cur_X3 = servo_max3
        # pwm.set_pwm(2,0 cur_X3)
def close():
    cur_X = servo_mid
    #pwm.set_pwm(0,0 cur_X)

if __name__ == '__main__':
        setup()


