# VEX V5 Python Project
import sys
import vex
from vex import *

#region config
brain = vex.Brain()
#endregion config

pot = vex.Pot(brain.three_wire_port.e)

while True :
    print pot.value(vex.RotationUnits.DEG )
    sys.sleep(1)

print("*****end******")

