# VEX V5 Python-Project with Competition Template
import sys
import vex
from vex import *

#region config
brain = vex.Brain();

#prints on the  Brin screen
brain.screen.print_("hello");

#endregion config


# Creates a competition object that allows access to Competition methods.
competition = vex.Competition()

def pre_auton():
    # All activities that occur before competition start
    # Example: setting initial positions
    #example code for debug messages on the brain screeen
    for i in range(0, 10):
        brain.screen.print_( "Number %d" % i)

    # Here we're using the built-in str function to convert the integer to a string
    for j in range(10, 20):
        brain.screen.print_( "Number " + str(j))
    pass

def autonomous():
    # Place autonomous code here
    pass

def drivercontrol():
    # Place drive control code here, inside the loop
    while True:
        # This is the main loop for the driver control.
        # Each time through the loop you should update motor
        # movements based on input from the controller.
        
        pass

# Do not adjust the lines below

# Set up (but don't start) callbacks for autonomous and driver control periods.
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)

# Run the pre-autonomous function.
pre_auton()


# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.