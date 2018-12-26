# VEX V5 Python Project
import sys
import vex
from vex import *

#region config
brain       = vex.Brain();
Motor 		= vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
bumper_a    = vex.Bumper(brain.three_wire_port.a)
#endregion config

# Carefully now...

while True:
  # Creep back...
  dt.drive(vex.DirectionType.REV)
  sys.wait_for(bumper_a.pressing)
  # Ran into something, move away from it
  dt.drive(vex.DirectionType.FWD)
  sys.sleep(2)
  # Turn a bit to avoid it...
  dt.turn_for(vex.TurnType.LEFT, 77, vex.RotationUnits.DEG)
  # Ready to try again!


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