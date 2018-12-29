# VEX V5 Python-Project with Competition Template
#Imports
print("Checkpoint 0")
import sys
import vex
import math



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

print("*****end******")