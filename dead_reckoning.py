import sys
import vex
import math

from math import *
from vex  import *

brain = vex.Brain();
motor_right = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
motor_left  = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
con         = vex.Controller(vex.ControllerType.PRIMARY)

con.set_deadband(10) #so that slight motion of controller does not disturb anything

dt = vex.Drivetrain(motor_left, motor_right, 319.1764, 292.1, vex.distanceUnits.mm)
knock_flags()

def knock_flags():
#	set our standard velocity
	dt.setVelocity(20,vex.velocityUnits.pct)

#	advance four feet
	dt.driveFor(vex.directionType.fwd,48,vex.distanceUnits.in)
	vex.sleep(1)

'''
#	retreat two feet
    
    dt.driveFor(vex.directionType.rev,24,vex.distanceUnits.in)
    vex.sleep(1)

#	set velocity a bit slower for more precision
    
    dt.setVelocity(10,vex.velocityUnits.pct);

#   turn to face a spot four feet to the right and two feet ahead
#   the result of calculating that angle has to be converted from radians to degrees by
#   multiplying by 180/pi
    
    dt.turnFor(vex.turnType.right,atan(48/24)*180/3.141592,vex.rotationUnits.deg)
    vex.sleep(1)

#   //increase velocity again

    dt.setVelocity(20,vex.velocityUnits.pct)

#   drive along the hypotenuse of the triangle we used to compute our turn
#   if the length of the triangle's sides are a, b, and c, they are related by
#   a^2 + b^2 = c^2, so c, the side we want, is the square root of a^2 + b^2
    
    dt.driveFor(vex.directionType.fwd,sqrt(24*24+48*48),vex.distanceUnits.in)

#   after finishing a driveFor or turnFor command, the motors will stop in Hold
#   mode. To make them relax, you must explicitly stop them with another brakeType.
    
    dt.stop(vex.brakeType.coast)

'''



###########################################
'''

The routine executed here is designed to score a 3 point swing during autonomous in the VRC Turning Point game from the red side. From a starting position in the net-side starting tile, facing the net-side wall, the robot advances four feet, toggling the low flag from its blue starting position (+1 swing) to a red scored position (+1). From there, it backs up, turns towards the middle low flag, and attempts to ram it and toggle it to red (+1). Assuming the robot drives true and doesn't fault by crossing the middle line, this should score three points!
Some of the more complicated math in this program comes in around getting to the middle low flag. As we go to make the turn towards it, all we know about its position is that it's 2 feet (24 inches) ahead of us and 4 feet (48 inches) to our right. Those two measurements can form the legs of a right triangle, though, so we can use some trigonometry to find both how far to turn and how far to drive. The angle relies on tan(angle) = opposite side length / close side length. Taking the arctangent (the opposite of the tangent) of both sides gives us: atan(tan(angle)) = angle = atan(O / A). For the distance to the low flag, we use the Pythagorean Theorem: a^2 + b^2 = c^2, where a and b are the lengths of the sides of a right triangle and c is the length of the hypotenuse. To get c, the distance we need to drive, we can take the square root of both sides.

Motor connections:

Port 15: right side drive motor (200 RPM)
Port 16: left side drive motor (200 RPM) 

Commands demonstrated:

Distance-based drivetrain drive commands
Angle-based drivetrain turn commands
Using functions from a standard library (math.atan and math.sqrt)
// VEX V5 C++ Project
#include "vex.h"
#include <cmath>

//#region config_globals
vex::brain      Brain;
vex::motor      motor_right(vex::PORT15, vex::gearSetting::ratio18_1, true);
vex::motor      motor_left(vex::PORT16, vex::gearSetting::ratio18_1, false);
vex::drivetrain dt(motor_left, motor_right, 319.1764, 292.1, vex::distanceUnits::mm);
//#endregion config_globals

using namespace vex;

int main(void) {
    //set our standard velocity
    dt.setVelocity(20,vex::velocityUnits::pct);
    //advance four feet
    dt.driveFor(vex::directionType::fwd,48,vex::distanceUnits::in);
    vex::sleep(1);
    //retreat two feet
    dt.driveFor(vex::directionType::rev,24,vex::distanceUnits::in);
    vex::sleep(1);
    //set velocity a bit slower for more precision
    dt.setVelocity(10,vex::velocityUnits::pct);
    //turn to face a spot four feet to the right and two feet ahead
    //the result of calculating that angle has to be converted from radians to degrees by
    //multiplying by 180/pi
    dt.turnFor(vex::turnType::right,atan(48/24)*180/3.141592,vex::rotationUnits::deg);
    vex::sleep(1);
    //increase velocity again
    dt.setVelocity(20,vex::velocityUnits::pct);
    //drive along the hypotenuse of the triangle we used to compute our turn
    //if the length of the triangle's sides are a, b, and c, they are related by
    //a^2 + b^2 = c^2, so c, the side we want, is the square root of a^2 + b^2
    dt.driveFor(vex::directionType::fwd,sqrt(24*24+48*48),vex::distanceUnits::in);
    //after finishing a driveFor or turnFor command, the motors will stop in Hold
    //mode. To make them relax, you must explicitly stop them with another brakeType.
    dt.stop(vex::brakeType::coast);
}
'''