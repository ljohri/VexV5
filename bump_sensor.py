# VEX V5 Python Project
import sys
import vex
from vex import *

#region config
brain       = vex.Brain();
Motor 		= vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
bumper_a    = vex.Bumper(brain.three_wire_port.a)
#endregion config


def autonomous():
	while True:
		if bumper_a.pressing()==False:
			Motor.spin(vex.DirectionType.FWD, 40, vex.VelocityUnits.PCT)
	pass	

def drivercontrol():
	pass


competition = vex.Competition()
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)