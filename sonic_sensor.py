<<<<<<< HEAD
# VEX V5 Python-Project with Competition Template
#Imports
print("Checkpoint 0")
=======
# VEX V5 Python Project
>>>>>>> c52da569e5a21585eac693bff3d03ddfd009d45d
import sys
import vex
from vex import *

# region config
brain = vex.Brain();
Motor = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
# dev         = vex.Devices()
# con         = vex.Controller(vex.ControllerType.PRIMARY)
sonar = vex.Sonar(brain.three_wire_port.c)


<<<<<<< HEAD
print("Checkpoint 1")
#Variables
brain       = vex.Brain()
dev         = vex.Devices()
con         = vex.Controller(vex.ControllerType.PRIMARY)

#output cable connected to port C and the inpur connected to port d
#output and input have to be on the consecutive ports in that order
#Sonar has two three wire connection - one is termed as input and the other
#as the output
sonar = vex.Sonar(brain.three_wire_port.c)
print("Checkpoint 2")
def autonomous():
    print("Checkpoint 3")
	while True :
	    print ( sonar.distance(vex.DistanceUnits.CM) )

	print("Checkpoint 4")
	

def drivercontrol():
    print("Checkpoint 6")

print("Checkpoint 7")
competition = vex.Competition()
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)
print("Checkpoint 8")
=======
# endregion config


def autonomous():
    while True:
        sonardistance = sonar.distance(DistanceUnits.IN)
        print(sonardistance)
        if sonardistance < 10:
            Motor.spin(vex.DirectionType.FWD, 0, vex.VelocityUnits.PCT)
        else:
            Motor.spin(vex.DirectionType.FWD, 40, vex.VelocityUnits.PCT)

        # if bumper_b.pressing() == 0:
        #     Motor.spin(vex.DirectionType.FWD, 40, vex.VelocityUnits.PCT)
        #
        # else:
        #     Motor.spin(vex.DirectionType.FWD, 0, vex.VelocityUnits.PCT)
        sys.sleep(1)


def drivercontrol():
    pass


competition = vex.Competition()
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)

# output cable connected to port C and the inpur connected to port d
# output and input have to be on the consecutive ports in that order
# Sonar has two three wire connection - one is termed as input and the other
# as the output
>>>>>>> c52da569e5a21585eac693bff3d03ddfd009d45d

print("*****end******")