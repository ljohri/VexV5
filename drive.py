# VEX V5 Python-Project with Competition Template
#Imports
import sys
import vex
import math
from vex import *
from math import *

#Variables
dev=        vex.Devices()
motor_right = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
motor_left  = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
con         = vex.Controller(vex.ControllerType.PRIMARY)
brain = vex.Brain()
print("hello....")
print(dev.number())
con.set_deadband(10)

#Procedures
def pre_auton():
   # All activities that occur before competition start
   # Example: setting initial positions
   pass
def autonomous():
   pass
def drivercontrol():
   while True:
       y_axis  = con.axis3.position()
       x_axis  = con.axis4.position()

       if (y_axis==0) and (x_axis==0):
           left_power=0
           right_power=0

       if x_axis==0:
           left_power  = y_axis
           right_power = left_power

       if y_axis==0:
           if x_axis>0:
               left_power  = x_axis
               right_power = 0
           else:
               right_power = (x_axis)*(-1)
               left_power  = 0

       if (y_axis>0) and (x_axis>0):
           left_power  = math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  )
           angle       = math.atan(y_axis/x_axis)
           right_power = int((angle/(3.1415926536/2)) * left_power)
           left_power  = int(left_power)

       if (y_axis>0) and (x_axis<0):
           right_power = math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  )
           angle       = math.atan(y_axis/  (-1*x_axis) )
           left_power  = int( (angle/(3.1415926536/2))*right_power )
           right_power = int( right_power )

       if (y_axis<0) and (x_axis<0):
           right_power = (math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  ))
           angle       = math.atan( y_axis/x_axis )
           left_power  = int((angle/(3.1415926536/2)) *right_power)* (-1)
           right_power = int(right_power)* (-1)

       if (y_axis<0) and (x_axis>0):
           right_power = (math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  ))
           angle       = math.atan( (y_axis* (-1) )/x_axis )
           left_power  = int((angle/(3.1415926536/2)) *right_power)* (-1)
           right_power = int(right_power)* (-1)

       print("left_power: ", left_power, "| right_power: ", right_power)
       motor_left.spin (vex.DirectionType.FWD, left_power, vex.VelocityUnits.PCT)
       motor_right.spin(vex.DirectionType.FWD, right_power, vex.VelocityUnits.PCT)

#main section
drivercontrol()

# Do not adjust the lines below
# Set up (but don't start) callbacks for autonomous and driver control periods.
# Run the pre-autonomous function.
# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.