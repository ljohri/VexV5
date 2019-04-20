# VEX V5 Python Project
import sys
import vex
from vex import *

def bumper_test() :
    if ( bumper.pressing() == 1 ):
        print "bumper pressing\n"
def test() :
    while True:
        bumper_test()
        print sonar.distance()
        sys.sleep(1)

def gyro_reset():
    gyro_base = gyro.value()

def gyro_get_value() :
    return gyro.value() - gyro_base 

def myclock_reset():
    time_base = sys.clock()

def  get_myclock():
    retrun sys.clock()-time_base 

def log_values() :
    buf = str(get_myclock()) + "\t" + str(motor_left_speed) + "\t" + \
        str(motor_right_speed) + "\t" + \
        str(gyro_get_value) +"\t" + str(motor_left.rotation()) +"\t" + \
        str( motor_left.rotation() + "\n")
    vex.BrainSDCard.appendfile(FILE, buf)        
    
MAX_SPEED = 40
FACTOR = 0.7
ANGLE_TURN = 10
FILE = "data.txt"
    
#region main
brain = vex.Brain()

motor_right        = vex.Motor(vex.Ports.PORT13, vex.GearSetting.RATIO18_1, True)
motor_left         = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, False)
motor_left_speed = MAX_SPEED
motor_right_speed_factor = FACTOR

myclock_reset()
gyro_base = 0
str="   \n"
bumper = vex.Bumper(brain.three_wire_port.b)
gyro = vex.Gyro(brain.three_wire_port.a)
sonar = vex.Sonar(brain.three_wire_port.c)
sys.sleep(1) #allow sonar,gyro to calibrate
vex.BrainSDCard.savefile(FILE, str)	

while (motor_right_speed >= 0 ):
    #loop initialization
    gyro_reset()
    motor_right.reset_rotation()
    motor_left.reset_rotation()
    motor_right_speed = motor_left_speed * motor_right_speed_factor
    
    #set motorns to start the turn
    motor_right.set_velocity(motor_right_speed)
    motor_left.set_velocity(motor_left_speed)
    
    #wait for the turn to complete
    while ( gyro_get_value() <= ANGLE_TURN ):
        log_values()
        sys.sleep(0.1)
    #reduce factor for the next loop
    motor_right_speed_factor = motor_right_speed_factor-0.1
    if sonar.value() < 100 or bumper.pressing() :
        sys.exit()

#endregion main