# VEX V5 Python-Project with Competition Template

import sys

import vex

from vex import *


brain = vex.Brain()

dev   = vex.Devices()

motor = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, True)

con   = vex.Controller(vex.ControllerType.PRIMARY)


competition = vex.Competition()



def pre_auton():
    
pass

def autonomous():
   
''' motor.rotate_for_time (vex.DirectionType.FWD, 5, TimeUnits.SEC, 50, VelocityUnits.PCT )'''
   
print 'bye'


def drivercontrol():
    
while True:
        
print 'hi'
        
sys.sleep(1)
        
if con.buttonB.pressing():
            
motor.spin (vex.DirectionType.FWD, 40, vex.VelocityUnits.PCT)
        
elif con.buttonX.pressing(): 
            
motor.spin (vex.DirectionType.REV, 40, vex.VelocityUnits.PCT)
        
else:
            
motor.spin (vex.DirectionType.FWD, 0, vex.VelocityUnits.PCT)
        
print 'hi'
       



comp=vex.Competition()

comp.autonomous(autonomous)

comp.drivercontrol(drivercontrol)
