# VEX V5 Python Project
# import sys
import vex
from vex import *

# region config
brain = vex.Brain();
Motor = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
bumper_b = vex.Bumper(brain.three_wire_port.b)


# endregion config


def autonomous():
    while True:
        print(bumper_b.pressing())
        if bumper_b.pressing() == 0:
            Motor.spin(vex.DirectionType.FWD, 40, vex.VelocityUnits.PCT)

        else:
            Motor.spin(vex.DirectionType.FWD, 0, vex.VelocityUnits.PCT)
        sys.sleep(1)


def drivercontrol():
    pass


competition = vex.Competition()
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)