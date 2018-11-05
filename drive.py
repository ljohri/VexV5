 5
1





 
Message List
programming
You created this channel on October 14th. This is the very beginning of the programming channel.
 Set a purpose Add an app Invite others to this channel

GreenLight [10:10 AM]
joined #programming along with 4 others.

GreenLight [10:15 AM]
@channel - we will use the Robot Mesh with Python as the base programming platform; robot mesh is web based - https://www.vexrobotics.com/rm-studio-edr.html
VEX Robotics
Robot Mesh Studio
USD
$9,999.00
WEBSITE
vexrobotics.com
there is a paid version which can be installed on the computer but we do not need it
https://www.robotmesh.com/studio  - is the starting url for the studio; you will have to create your own account
robotmesh.com
Robot Mesh - Robotics Controllers and Kits
Default Description

GreenLight [10:24 AM]
starter code
Untitled 
"""
To make a copy of this program that you can edit, click the gear icon labeled
Options in the top right, and click "Copy project".
"""
import vex
you would have to install serial driver (Studio will remind you of that) if you want to transfer your program to Cortex computer on the robot

GreenLight [6:13 PM]
@channel - the basic code snippet is as above

GreenLight [7:28 PM]
Untitled 
import vex
import sys
​
#region config
left  = vex.Motor(1)

GreenLight [9:23 AM]
@channel - there is virtual robot here- https://www.robotmesh.com/hoc2017  (vex EDR) can you write a program to move it around all the 4 corners and come back to it's starting position
robotmesh.com
Hour of Code 2017
Default Description
@channel - on that page click on start coding now
@channel - you have to write in blockly but it shows the generated Python code - the translation is fairly simple

GreenLight [7:30 PM]
@channel - all the joystick controls are listed here - you will have to assign buttons for arm up and down as well as opening and closing of the claw

GreenLight [7:35 PM]
@channel code for moving the arm up and down
Code for moving the arm up and down 
#code for moving arm up and down
import vex
​
#region config
brain   = vex.Brain();
@channel - similar code can be used for opening and closing the claw
@channel - you can use this as a starting code to modify and see the change in behaviour
clawbot complete code 
import vex
​
"""
Hit the "Copy Project" button in the "Options" menu to make a copy of this
project that you can edit!

GreenLight [10:22 AM]
@channel - for today :  goto https://www.robotmesh.com/studio and create your account
robotmesh.com
Robot Mesh - Robotics Controllers and Kits
Default Description
@channel - step 2 : sign on and then create a new project with the following code
@channel - step 2 : sign on and then create a new project with the following code 
import vex
import sys
​
#region config
left  = vex.Motor(1)
Use VEX EDR as your target platform
Use Python as the language
@channel - copy paste the code above into the blank project you have created

Vijayant [5:43 PM]
@channel python api documentation - https://www.robotmesh.com/docs/vexcortex-python/html/index.html

GreenLight [7:02 PM]
@channel starting V5 code with debugging on the LCD 0f the Brain ; the battery is functional again and so we are much better for the demo; need to test all the motors etc.
debug strings on the LCD 
# VEX V5 Python-Project with Competition Template
import sys
import vex
from vex import *
​
#region config
brain = vex.Brain();
brain.screen.print_("hello");
​
#endregion config
​
​
# Creates a competition object that allows access to Competition methods.
competition = vex.Competition()
​
def pre_auton():
  # All activities that occur before competition start
  # Example: setting initial positions
  for i in range(0, 10):
    brain.screen.print_( "Number %d" % i)
​
  # Here we're using the built-in str function to convert the integer to a string
  for j in range(10, 20):
    brain.screen.print_( "Number " + str(j))
  pass
​
def autonomous():
  # Place autonomous code here
  pass
​
def drivercontrol():
  # Place drive control code here, inside the loop
  while True:
    # This is the main loop for the driver control.
    # Each time through the loop you should update motor
    # movements based on input from the controller.
    
    pass
​
# Do not adjust the lines below
​
# Set up (but don't start) callbacks for autonomous and driver control periods.
competition.autonomous(autonomous)
competition.drivercontrol(drivercontrol)
​
# Run the pre-autonomous function.
pre_auton()
drivercontrol()
​
# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.
Collapse 
there are two ways to print the debug strings - either you can print on your debug computer by using print but need to have the USB cable connected or use the code from above to print on the Brain LCD

GreenLight [9:24 AM]
@channel - goal for this week is navigation using the left joystick alone - including turning, forward and backward motion; find deficiencies in climbing the platform and propose a mechanical design to resolve them; one idea would be to xmit power from front wheel to the back through a set of gears or alternatively use tank treads.  see you at @630 PM Sunday:
@Swasti @Anirudh - pl look at https://www.robotmesh.com/vex-robotics/structure?p=3  and then figure out what all things we need to order to make the structural changes
robotmesh.com
Structure - VEX EDR
Default Description

GreenLight [8:36 AM]
@channel - we will start to use github for code sharing @Vijayant - can you bring up @Anirudh upto speed on git hub; the repo we would be using is - https://github.com/ljohri/VexV5.git  ; it is public repo so he would have access as soon as sign-on is created
GitHub
ljohri/VexV5
turning point competition. Contribute to ljohri/VexV5 development by creating an account on GitHub.

Sparsh [8:50 AM]
# VEX V5 Python-Project with Competition Template
#Imports
import sys
import vex
import math
from vex import *
from math import *

#Variables
dev=        vex.Devices()
motor_right = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
motor_left  = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
con         = vex.Controller(vex.ControllerType.PRIMARY)
brain = vex.Brain()
print("hello....")
print(dev.number())
con.set_deadband(10)

#Procedures
def pre_auton():
   # All activities that occur before competition start
   # Example: setting initial positions
   pass
def autonomous():
   pass
def drivercontrol():
   while True:
       y_axis  = con.axis3.position()
       x_axis  = con.axis4.position()

       if (y_axis==0) and (x_axis==0):
           left_power=0
           right_power=0

       if x_axis==0:
           left_power  = y_axis
           right_power = left_power

       if y_axis==0:
           if x_axis>0:
               left_power  = x_axis
               right_power = 0
           else:
               right_power = (x_axis)*(-1)
               left_power  = 0

       if (y_axis>0) and (x_axis>0):
           left_power  = math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  )
           angle       = math.atan(y_axis/x_axis)
           right_power = int((angle/(3.1415926536/2)) * left_power)
           left_power  = int(left_power)

       if (y_axis>0) and (x_axis<0):
           right_power = math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  )
           angle       = math.atan(y_axis/  (-1*x_axis) )
           left_power  = int( (angle/(3.1415926536/2))*right_power )
           right_power = int( right_power )

       if (y_axis<0) and (x_axis<0):
           right_power = (math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  ))
           angle       = math.atan( y_axis/x_axis )
           left_power  = int((angle/(3.1415926536/2)) *right_power)* (-1)
           right_power = int(right_power)* (-1)

       if (y_axis<0) and (x_axis>0):
           right_power = (math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  ))
           angle       = math.atan( (y_axis* (-1) )/x_axis )
           left_power  = int((angle/(3.1415926536/2)) *right_power)* (-1)
           right_power = int(right_power)* (-1)

       print("left_power: ", left_power, "| right_power: ", right_power)
       motor_left.spin (vex.DirectionType.FWD, left_power, vex.VelocityUnits.PCT)
       motor_right.spin(vex.DirectionType.FWD, right_power, vex.VelocityUnits.PCT)

#main section
drivercontrol()

# Do not adjust the lines below
# Set up (but don't start) callbacks for autonomous and driver control periods.
# Run the pre-autonomous function.
# Robot Mesh Studio runtime continues to run until all threads and
# competition callbacks are finished.

Sparsh [4:14 PM]
latest code 
# VEX V5 Python-Project with Competition Template
#Imports
import sys
import vex
import math
from vex import *
from math import *
#Variables
dev=    vex.Devices()
motor_right = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
motor_left = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
motor_arm_up  = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, True)
motor_arm_down  = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO18_1, True)
con     = vex.Controller(vex.ControllerType.PRIMARY)
brain = vex.Brain()
print("hello....")
print(dev.number())
con.set_deadband(10)
#Procedures
def pre_auton():
  # All activities that occur before competition start
  # Example: setting initial positions
  pass
def autonomous():
  pass
def drivercontrol():
  while True:
    y_axis = con.axis3.position()
    x_axis = con.axis4.position()
    
    if (y_axis==0) and (x_axis==0):
      left_power=0
      right_power=0
      
    if x_axis==0:
      left_power = y_axis
      right_power = left_power
      
    if y_axis==0:
      if x_axis>0:
        left_power = x_axis
        right_power = 0
      else:
        right_power = (x_axis)*(-1)
        left_power = 0
        
    if (y_axis>0) and (x_axis>0):
      left_power = math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis) )
      angle    = math.atan(y_axis/x_axis)
      right_power = int((angle/(3.1415926536/2)) * left_power)
      left_power = int(left_power)
      
    if (y_axis>0) and (x_axis<0):
      right_power = math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis) )
      angle    = math.atan(y_axis/ (-1*x_axis) )
      left_power = int( (angle/(3.1415926536/2))*right_power )
      right_power = int( right_power )
    
    if (y_axis<0) and (x_axis<0):
      right_power = (math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis) ))
      angle    = math.atan( y_axis/x_axis )
      left_power = int((angle/(3.1415926536/2)) * right_power)* (-1)
      right_power = int(right_power)* (-1)
    
    if (y_axis<0) and (x_axis>0):
      left_power = (math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis) ))
      angle    = math.atan( (y_axis* (-1) )/x_axis )
      right_power = int((angle/(3.1415926536/2)) * left_power)* (-1)
      left_power = int(left_power)* (-1)
    
    print("left_power: ", left_power, "| right_power: ", right_power)
    motor_left.spin (vex.DirectionType.FWD, left_power, vex.VelocityUnits.PCT)
    motor_right.spin(vex.DirectionType.FWD, right_power, vex.VelocityUnits.PCT)
    
    if (con.buttonL1 == True):
      motor_arm_up.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
      print("You pressed L1! Congratulations!")
    if (con.buttonL2 == True):
      motor_arm_down.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
#main section
drivercontrol()
while True:
  brain.screen.print_("The End")