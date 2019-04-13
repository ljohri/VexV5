# VEX V5 Python-Project with Competition Template
#Imports
print("Checkpoint 0")
import sys
import vex
from vex import *

# region config
brain = vex.Brain()
Motor = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
# dev         = vex.Devices()
# con         = vex.Controller(vex.ControllerType.PRIMARY)
sonar = vex.Sonar(brain.three_wire_port.c)


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

print("*****end******")