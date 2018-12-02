# VEX V5 Python-Project with Competition Template
#Imports
import sys
import vex
import math




#Variables
brain       = vex.Brain()
dev         = vex.Devices()
con         = vex.Controller(vex.ControllerType.PRIMARY)

#output cable connected to port C and the inpur connected to port d
#output and input have to be on the consecutive ports in that order
sonar = vex.Sonar(brain.three_wire_port.c)

while True :
    print sonar.distance(vex.DistanceUnits.MM)
    sys.sleep(1)

print("*****end******")